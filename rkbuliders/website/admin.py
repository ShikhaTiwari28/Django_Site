from django.contrib import admin
from website.models import SliderImage, AboutUs, ContactInfo, WhatIsVastu, Project, Review, Query
# Register your models here.


class MainSliderAdmin(admin.ModelAdmin):
    """
        Admin class for Main sliser
    """
    list_display = ('title', 'description', 'image', 'datetime')


class AboutUsAdmin(admin.ModelAdmin):
    """
        Admin for about us
    """
    list_display = ('description', 'sidebar_description', 'image', 'datetime')

    def has_add_permission(self, request):
        base_add_permission = super(AboutUsAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not AboutUs.objects.exists()
        return False


class ContactInfoAdmin(admin.ModelAdmin):
    """
        Admin for Contact Info
    """
    list_display = ('email', 'phone', 'address_line1', 'address_line2', 'latitude', 'longitude', 'country')

    def has_add_permission(self, request):
        base_add_permission = super(ContactInfoAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not ContactInfo.objects.exists()
        return False


class ProjectAdmin(admin.ModelAdmin):
    """
        Admin for Project
    """
    list_display = ('project_type', 'title', 'image', 'datetime')


class WhatIsVastuAdmin(admin.ModelAdmin):
    """
        WhatIsVastu Admin
    """
    list_display = ('answer1', 'answer2', 'answer3', 'datetime')

    def has_add_permission(self, request):
        base_add_permission = super(WhatIsVastuAdmin, self).has_add_permission(request)
        if base_add_permission:
            return not WhatIsVastu.objects.exists()
        return False

class ReviewAdmin(admin.ModelAdmin):
    """
        Admin for review model
    """
    list_display = ('name', 'description', 'designation', 'image', 'datetime')


class QueryAdmin(admin.ModelAdmin):
    """
        QueryAdmin for Query model
    """
    list_display = ('name', 'email', 'message', 'datetime')

admin.site.register(SliderImage, MainSliderAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(WhatIsVastu, WhatIsVastuAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Query, QueryAdmin)