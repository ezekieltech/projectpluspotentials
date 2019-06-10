from django.contrib import admin

from websiteapp.models import Project, Service, Staff, Press, Home, ProjectImage, Industry, Department

# Register your models here.
# admin.site.register(Project)
# admin.site.register(Service)
# admin.site.register(Staff)
# admin.site.register(Home)

# Define the admin class


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 4
    max_num = 7


class DepartmentInline(admin.TabularInline):
    model = Department
    #radio_fields = {"project": admin.VERTICAL}


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    model = Department


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'project_article')
    inlines = [ProjectImageInline]
    exclude = ['industry']


#@admin.register(ProjectDetailContent)
# class ProjectDetailContentAdmin (admin.ModelAdmin):
#    model = ProjectDetailContent
#
#    def has_add_permission(self, request):
#        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


# Register the admin class with the associated model
admin.site.register(Project, ProjectAdmin)

#@admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#list_display = ['title', 'client', 'location', 'service']


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'qualification', 'department', 'order_of_appearance_on_website']


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
