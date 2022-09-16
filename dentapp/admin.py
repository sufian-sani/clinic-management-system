from atexit import register
from django.contrib import admin
from .models import *
# Register your models here.


# Treatment

class TreatmentImgGalleryAdmin(admin.StackedInline):
    model = TreatmentImageGallery
    min_num = 2
    extra = 1

class TreatmentAdmin(admin.ModelAdmin):
    inlines = [TreatmentImgGalleryAdmin]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Treatment,TreatmentAdmin)



# MembershipPlan

class MembershipBannerImageAdmin(admin.StackedInline):
    model = MembershipBannerImage
    min_num = 2
    extra = 0

class MembershipDiscriptionAdmin(admin.StackedInline):
    model = MembershipDescription
    min_num = 2
    extra = 2

class MembershipPlansAdmin(admin.ModelAdmin):
    inlines = [MembershipBannerImageAdmin, MembershipDiscriptionAdmin]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(MembershipPlan,MembershipPlansAdmin)


# PatientSafety

class PatientSafetyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(PatientSafety,PatientSafetyAdmin)

admin.site.register(Slider)

admin.site.register(Pointofservice)
admin.site.register(Pricingplan)

admin.site.register(Membershipcustomer)
admin.site.register(Profile)