from django.shortcuts import render, redirect, HttpResponse
from app_tech_man.models import *
import requests
import geonamescache


# Create your views here.

def index(request):
    return render(request, 'index.html')


def sign_up_jobSeeker_page(request):
    return render(request, 'sign_up_jobSeeker.html')


def sign_in_jobSeeker_page(request):
    return render(request, 'sign_in_jobSeeker.html')

def sing_in_employer_page(request):
    return render(request, 'sing_in_Employer.html')



def post_job_page(request):
    return render(request, 'post_job.html')


def find_job_page(request):
    return render(request, 'find_job.html')

def sign_up_Employer_page(request):
    return render(request, 'sign_up_Employer.html')



def jobSeeker_registration(request):
    new_user = JobSeeker.objects.create(
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
        email = request.POST['email'],
        password = request.POST['password'],
        )
    request.session['id'] = new_user.id
    request.session['first_name'] = new_user.first_name
    return redirect('/tech_&_man/dashboard_jobseeker')


def dashboard_jobseeker(request):
    return render(request, 'dashboard_jobSeeker.html')



def employer_registration(request):
    Employer.objects.create(
        first_name = request.POST['firstName'],
        last_name = request.POST['lastName'],
        email = request.POST['email'],
        password = request.POST['password'],
        )
    return redirect('/tech_&_man/dashboard_employer')


def dashboard_employer(request):
    return render(request, 'dashboard_employer.html')


    # gc = geonamescache.GeonamesCache()
    # us_states = gc.get_us_states_by_names()
    # context = {
    #     'us_states' : us_states
    # }


