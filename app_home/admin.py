from django.contrib import admin
from .models import *


# Visitor Admin
class VisitorAdmin(admin.ModelAdmin):
    list_display = ("visit_date", "location", "ip_address")
    search_fields = ("ip_address", "location")
    list_filter = ("visit_date",)

# Service Admin
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("last_edited", "name_1", "description_1", "name_2", "description_2")
    search_fields = ("name_1", "name_2", "name_3", "name_4")
    list_filter = ("last_edited",)

# About Us Admin
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("last_edited", "year_1", "sub_heading_1", "year_2", "sub_heading_2")
    search_fields = ("year_1", "year_2", "year_3", "year_4")
    list_filter = ("last_edited",)

# Projects Admin
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ("last_edited", "project_name_1", "brief_1", "project_name_2", "brief_2")
    search_fields = ("project_name_1", "project_name_2", "project_name_3")
    list_filter = ("last_edited",)

# Team Admin
class TeamAdmin(admin.ModelAdmin):
    list_display = ("last_edited", "name_1", "title_1", "name_2", "title_2")
    search_fields = ("name_1", "name_2", "name_3")
    list_filter = ("last_edited",)

# Footer Contact Info Admin
class FooterContactInfoAdmin(admin.ModelAdmin):
    list_display = ("email", "phone", "address")
    search_fields = ("email", "phone", "address")
    list_filter = ("email", "phone")

# Registering models with their respective admin classes
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(service, ServiceAdmin)
admin.site.register(about_us, AboutUsAdmin)
admin.site.register(projects, ProjectsAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(FooterContactInfo, FooterContactInfoAdmin)
