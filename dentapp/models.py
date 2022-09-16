from audioop import reverse
from distutils.command import upload
from email.mime import image
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField

from django.forms import ImageField
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

# Create your models here.


# Treatment start

class Treatment(models.Model):
    title = models.CharField(max_length=50)
    slug  = models.SlugField(blank=True) 
    short_Description  = RichTextUploadingField()
    long_description = RichTextUploadingField()
    image = models.ImageField(upload_to='Treatmentimage')
    icon_image  = models.ImageField()

    def __str__(self):
        return self.title

class TreatmentImageGallery(models.Model):
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    after_image = models.ImageField(upload_to='TreatmentImageGallery')
    before_image = models.ImageField(upload_to='TreatmentImageGallery')
    
    def __str__(self):
        return self.treatment.title + '//' + self.title

# Treatment end

# MembershipPlan start

class MembershipPlan(models.Model):
    title = models.CharField(max_length = 150)
    slug  = models.SlugField(unique = True)
    image = models.ImageField(upload_to='MembershipImg')
    
    def __str__(self):
        return self.title


class MembershipBannerImage(models.Model):
    membership_plans  = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='MembershipImg')

    def __str__(self):
        return self.membership_plans.title

class MembershipDescription(models.Model):
    membership_plans  = models.ForeignKey(MembershipPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    description = RichTextUploadingField()


# MembershipPlan end
    

# PATIENT SAFETY start

class PatientSafety(models.Model):
    title = models.CharField(max_length = 150)
    slug  = models.SlugField(blank=True)
    image = models.ImageField(upload_to='PatientSafety')
    short_description  = models.TextField()
    long_description = RichTextUploadingField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'PatientSafety'
        verbose_name_plural = 'PatientSafeties'

class Slider(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='slider')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'




class Pricingplan(models.Model):
    image = models.ImageField(upload_to='pricingplan')
    name = models.CharField(max_length = 150)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pricing Plan'
        verbose_name_plural = 'Pricing Plan'

class Pointofservice(models.Model):
    # pricingplan = models.OneToOneField(Pricingplan,on_delete=models.CASCADE)
    pricingplan = models.ForeignKey(Pricingplan, on_delete=models.CASCADE)
    point_of_service = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.pricingplan) + " - " + self.point_of_service

    class Meta:
        verbose_name = 'Point Of Service'
        verbose_name_plural = 'Point Of Service'

class Membershipcustomer(models.Model):
    service_id = models.CharField(max_length = 150)
    service_name = models.CharField(max_length = 150)
    customer_id = models.CharField(max_length = 150, unique = True)
    customer_name = models.CharField(max_length = 150)
    customer_email = models.EmailField(max_length = 150, unique = True)
    customer_number = models.CharField(max_length = 150, unique = True)
    customer_message = models.CharField(max_length = 150)

    def __str__(self):
        return self.customer_name

    class Meta:
        verbose_name = 'Membership Customer'
        verbose_name_plural = 'Membership Customer'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    service_id = models.CharField(max_length = 150, blank=True, null=True)
    service_name = models.CharField(max_length = 150, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance,)

# @receiver(post_save, sender=User)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()



