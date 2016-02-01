from django.shortcuts import render, HttpResponse
from add_job.models import Job
from .form import JobForm
from crispy_forms.helper import FormHelper

def index(request):
    return render(request, "index.html")

def search_form(request):
    return render(request, 'add_job/search_form.html')

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        jobs = Job.objects.filter(stanowisko__icontains=q)
        return render(request, 'add_job/search_results.html',
                      {'jobs': jobs, 'query': q})
    else:
        return HttpResponse('Pleas submit a search term')

def add_job_form(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'add_job/add_job_form.html')
    else:
        form = JobForm()
    return render(request, 'add_job/add_job_form.html', {'form': form})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'add_job/job_list.html', {'jobs': jobs})

def job_details(request, offset):
    job = Job.objects.get(stanowisko=offset)
    return render(request, 'add_job/job_details.html', {'job': job})