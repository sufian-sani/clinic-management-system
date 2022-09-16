from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('treatments/', treatment, name='treatments'),
    # path('appointment/', appointment, name='appointment'),
    path('treatments/<slug>/', treatmentDetails, name='treatments-details'),
    path('membership_plans/<slug>/', MembershipPlansDetails, name='membershipplans-details'),
    path('patientsafety/<slug>/', PatientSafetyDetails, name='patientsafety-details'),
    path('alldoctor/', alldoctor, name='alldoctor'),
    path('alldoctor/<slug>/', doctordetails, name='doctordetails'),
    path('contact-us/', contactus, name='contactus'),
    path('about-us/', aboutus, name='aboutus'),
    path('about-us/', aboutus, name='aboutus'),
    path('member-ship-form/<slug>/', membershipform, name='membershipform'),
    path('membership-login-form/', membershiplogin, name='membershiplogin'),
]
