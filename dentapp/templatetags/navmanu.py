from django import template
from dentapp.models import *

register = template.Library()


@register.filter()
def treatments(request):
    return Treatment.objects.all()

@register.filter()
def membership_plans(request):
    return MembershipPlan.objects.all()

@register.filter()
def patientsafety(request):
    return PatientSafety.objects.all()


