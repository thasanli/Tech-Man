from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post_job', views.post_job_page),
    path('find_job', views.find_job_page),
    path('sign_up_employer', views.sign_up_Employer_page),
    path('sign_up_jobSeeker', views.sign_up_jobSeeker_page),
    path('sign_in_jobSeeker', views.sign_in_jobSeeker_page),
    path('sign_in_employer', views.sing_in_employer_page),
    path('jobSeeker_registration', views.jobSeeker_registration),
    path('employer_registration', views.employer_registration),
    path('dashboard_jobseeker', views.dashboard_jobseeker), #redirect 
    path('dashboard_employer', views.dashboard_employer)

]