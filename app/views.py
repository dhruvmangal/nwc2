# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from .models import Job, Jobseeker,JobCategory
from .forms import LoginForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def jobs(request):
    latest_jobs= Job.objects.order_by('-job_date')[:10]
    context= {'latest_jobs':latest_jobs}
    if request.method == 'GET':
        if request.GET.get('job_category'):
            job_category= request.GET.get('job_category')
            cox= {'job_category': job_category}
        else:
             cox=   {'job_category': 'All'}
    else:
        cox=   {'job_category':'All'}

    return render(request, 'jobseeker/jobs.html',context, cox)    

def candidates(request):  
    latest_candidates= Jobseeker.objects.all() [:10]
    context= {'latest_candidates': latest_candidates}

    return render(request, 'employer/candidates.html', context)

def login(request):
    if request.method== 'POST':
        if request.POST.get('phone') and request.post.get('password'):
            jobseeker= Jobseeker.objects.filter(jobseeker_phone= request.POST.get('phone') )
            if len(Jobseeker)==0:
               return render(request, 'jobseeker/log-mob.html')  
            else:
                request.session['phone']= request.POST.get('mobile')
                return render(request, 'jobseeker/jobs.html')
        else:        
           return render(request, 'jobseeker/log-mob.html')

    else:    
        return render(request, 'jobseeker/log-mob.html') 

def signup(request):
    if request.method =='POST':
        if request.POST.get('submit'):
            phone= request.POST.get('phone')
            request.session['register_phone']= phone 
            return redirect('/app/user_details1/')
            
        else:    
             return render(request, 'jobseeker/signup.html')
    else:
        return render(request, 'jobseeker/signup.html')                   
       

def category(request):
    category= JobCategory.objects.all()
    context= {'category':category}
    return render(request, 'jobseeker/cat-mob.html', context)    

def jobview(request, job_id):
    try:
        job= Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        raise Http404("Job does not exists")

    context= {'job': job}       
    return render(request, 'jobseeker/jobview.html', context)


def user_details1(request):
    return render(request, 'userdetails.html')

def loginForm(request):
    if request.method =='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            user= Jobseeker.objects.get(phone=form.cleaned_data['phone'])
    return render(request, 'jobseeker/login.html')       


def filter(request):
    return render(request, 'jobseeker/filters.html')     

def location(request):
    return render(request, 'jobseeker/location.html')    