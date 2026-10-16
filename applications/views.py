from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JobApplicationForm
from .models import JobApplication

@login_required
def dashboard(request):
    qs = JobApplication.objects.filter(user=request.user)
    query = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()
    if query:
        qs = qs.filter(Q(company__icontains=query) | Q(role__icontains=query) | Q(notes__icontains=query))
    if status:
        qs = qs.filter(status=status)
    counts = {row['status']: row['total'] for row in JobApplication.objects.filter(user=request.user).values('status').annotate(total=Count('id'))}
    context = {
        'applications': qs,
        'query': query,
        'selected_status': status,
        'total_count': JobApplication.objects.filter(user=request.user).count(),
        'interview_count': counts.get('INTERVIEW', 0),
        'offer_count': counts.get('OFFER', 0),
        'rejected_count': counts.get('REJECTED', 0),
        'status_choices': JobApplication.STATUS_CHOICES,
    }
    return render(request, 'applications/dashboard.html', context)

@login_required
def application_create(request):
    form = JobApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        messages.success(request, 'Job application added.')
        return redirect('dashboard')
    return render(request, 'applications/application_form.html', {'form': form, 'page_title': 'Add application'})

@login_required
def application_edit(request, pk):
    item = get_object_or_404(JobApplication, pk=pk, user=request.user)
    form = JobApplicationForm(request.POST or None, instance=item)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Job application updated.')
        return redirect('dashboard')
    return render(request, 'applications/application_form.html', {'form': form, 'page_title': 'Edit application'})

@login_required
def application_delete(request, pk):
    item = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Job application deleted.')
        return redirect('dashboard')
    return render(request, 'applications/application_confirm_delete.html', {'item': item})
