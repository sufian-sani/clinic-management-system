from time import timezone
from django.shortcuts import render
from .models import *
from django.utils import timezone
from appointments.models import *
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import HttpResponseRedirect
from django.urls import reverse


from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from django.template.loader import render_to_string 

# Create your views here.
def index(request):
    doctor_profile = Doctorprofile.objects.all()
    slider_all = Slider.objects.all()

    pricingplan = Pricingplan.objects.all()
    pointofservice = Pointofservice.objects.all()

    # all_pricingplan = []

    # for i in pricingplan:
    #     all_pricingplan.append(i)
    #     for j in pointofservice:
    #         if i == j.pricingplan:
    #             all_pricingplan.append(j.point_of_service)

    # print(all_pricingplan)

    context ={
        'doctor_profile':doctor_profile,
        'slider_all':slider_all,
        'pricingplan':pricingplan,
        'pointofservice':pointofservice,
    }
    return render(request, 'index.html', context)


def treatment(request):
    return render(request, 'treatment.html')

def treatmentDetails(request,slug):
    treatments = Treatment.objects.get(slug=slug)
    treatmentImageGallery = TreatmentImageGallery.objects.filter(treatment=treatments)

    context ={
        'treatments':treatments,
        'treatmentImageGallery':treatmentImageGallery,
    }
    return render(request, 'treatmentdetails.html',context )

def MembershipPlansDetails(request,slug):
    membership_plans = MembershipPlan.objects.get(slug=slug)
    membershipBannerImage = MembershipBannerImage.objects.filter(membership_plans=membership_plans)
    membershipDescription = MembershipDescription.objects.filter(membership_plans=membership_plans)
    
    context ={
        'membership_plans':membership_plans,
        'membershipBannerImage':membershipBannerImage,
        'membershipDescription':membershipDescription,
    }
    
    return render(request, 'membershipplansdetails.html',context )

def PatientSafetyDetails(request,slug):
    patientsafety = PatientSafety.objects.get(slug=slug)
    date = timezone.now()
    context ={
        'patientsafety':patientsafety,
        'date':date,
    }
    print(date)
    
    return render(request, 'patientsafety.html',context )

def alldoctor(request):
    doctor_list = Doctorprofile.objects.all()
    context ={
        'doctor_list':doctor_list,
    }
    return render(request, 'subpage/alldoctor.html',context)


def doctordetails(request, slug):
    doctor_details = Doctorprofile.objects.get(slug=slug)
    context ={
        'doctor_details':doctor_details,
    }
    return render(request, 'subpage/doctor_details.html',context)

def contactus(request):
    return render(request, 'subpage/contact.html')

def aboutus(request):
    return render(request, 'subpage/aboutus.html')

def membershipform(request,slug):
    membership_plans = MembershipPlan.objects.get(slug=slug)
    membershipBannerImage = MembershipBannerImage.objects.filter(membership_plans=membership_plans)
    membershipDescription = MembershipDescription.objects.filter(membership_plans=membership_plans)

    email_admin = 'sufian@universeinfotech.net'

    if request.method == 'POST':
        serviceid = request.POST['serviceid']
        servicename = request.POST['servicename']
        customerid = request.POST['customerid']
        customerid__account = customerid
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cnumber = request.POST['cnumber']
        message = request.POST['message']

        customerpass = request.POST['customerpass']
        # customerpass = request.POST.cleaned_data['customerpass']

        # print(customerpass)

        user_customer = Membershipcustomer(service_id=serviceid, service_name=servicename, customer_id=customerid,customer_name=cname, customer_email=cemail, customer_number=cnumber, customer_message=message)
        if User.objects.filter(username=customerid).exists():
            messages.error(request, "This username is already taken")
        elif customerid__account == customerid:
            user = User.objects.create_user(customerid__account, cemail, customerpass)
            user.set_password(customerpass)
            if serviceid:
                userprofile_e = Profile.objects.create(user_id=user.id,service_id=serviceid, service_name=servicename)
                userprofile_e.save()
            user.save()
        
        messages.success(request, "Message sent." )

        subject = "Your Username and Password" 
        body = {
        'full_name': cname,
        'packagename': servicename,
        'username': customerid__account, 
        'password':  customerpass, 
        }
        message_email = "\n".join(body.values())

        # message = render_to_string('acc_active_email.html', {  
        #     'user': user,  
        #     'full_name': cname,
        #     'packagename': servicename,
        # }) 

        try:
            send_mail = EmailMessage(subject, message_email, to=[cemail])
            # send_mail = EmailMessage(subject, message_email, to=[cemail])
            # send_mail(subject, message_email, settings.EMAIL_HOST_USER, [cemail])
            send_mail.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')


        user_customer.save()
        
    
    context ={
        'membership_plans':membership_plans,
        'membershipBannerImage':membershipBannerImage,
        'membershipDescription':membershipDescription,
    }
    return render(request, 'subpage/membershipform.html',context)


def membershiplogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        print(username, password)

    return render(request, 'subpage/memberloginfrom.html')
    
