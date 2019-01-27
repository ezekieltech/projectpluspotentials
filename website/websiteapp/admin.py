from django.contrib import admin

from websiteapp.models import Project, Service, Staff, Press, Home


# Register your models here.
# admin.site.register(Project)
# admin.site.register(Service)
# admin.site.register(Staff)
# admin.site.register(Home)

# Define the admin class


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'industry', 'project_service')


# Register the admin class with the associated model
admin.site.register(Project, ProjectAdmin)

# Register the Admin classes for Book using the decorator


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for BookInstance using the decorator


@admin.register(Press)
class PressAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Home using the decorator


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Service using the decorator


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
