from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from tinymce.models import HTMLField

from PIL import Image
from .utilities import rescale_image
from django.core.files.uploadedfile import SimpleUploadedFile

from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


# class ProjectDetailContent(models.Model):
#
#    main_title = models.CharField(max_length=100, blank=True, null=True, default='Project')
#    sub_title = models.CharField(max_length=100, blank=True, null=True, default='Project')
#    short_intro = models.TextField(
#        max_length=540, default='We see your project from start to finish.', blank=False, null=False)
#
#    def __str__(self):
#        """
#        String for representing the Service object (in Admin site etc.)
#        """
#        return self.main_title
#

class Industry(models.Model):
    #project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='industries')
    industry = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ["industry"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.industry

    def get_absolute_url(self):
        """
        Returns the url to access a particular project instance.
        """
        return reverse('project-in-industry', args=[str(self.id)])


class Department(models.Model):
    department = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ["department"]

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.department

    def get_absolute_url(self):
        """
        Returns the url to access a particular project instance.
        """
        return reverse('department', args=[str(self.id)])


class Project(models.Model):
    """
    Model representing a project (a specific project).
    """
    title = models.CharField(max_length=200, default='')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    client = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=400, blank=True, null=True)
    summary = models.TextField(max_length=400, blank=True, null=True)
    project_article = HTMLField('content', default='')
    industry = models.ForeignKey(Industry,
                                 on_delete=models.CASCADE)

    service = models.ForeignKey('Service',
                                on_delete=models.CASCADE, related_name='type_of_service',  blank=True, null=True)

    #get_industry = Industry.industry.objects.all
    #industry = models.CharField(choices=get_industry, default='construction')
    # imgs = models.ImageField(upload_to='projectimages/mainproject',
    #                         default='serviceimages/None/no-img.jpg')
    project_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    class Meta:
        ordering = ["-project_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular project instance.
        """
        return reverse('project-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        #self.slug = '%i-%s' % (self.id, slugify(self.title))
        self.slug = '%s' % (slugify(self.title))
        '''
        self.project_images = [
            self.project_image1,
            self.project_image2,
            self.project_image3,
            self.project_image4,
            self.project_image5,
            self.project_image6
        ]
        # for project_img in project_images_to_resize:
        #    if project_img:
        #        image = project_img
        #        self.project_img = rescale_image(self, image)
        '''
        super(Project, self).save(*args, **kwargs)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/gallery/',
                              default='img/home/logo-transparent.png')


class Service(models.Model):
    """
    Model representing each service.
    """

    # Fields
    project = models.ManyToManyField(Project, related_name='services')
    service_title = models.CharField(max_length=100, help_text="Title of service")
    service_article = HTMLField('content')
    service_date = models.DateField(null=True, blank=True)
    service_image1 = models.ImageField(
        upload_to='serviceimages/',
        null=True, blank=True)

    # Metadata

    class Meta:
        ordering = ["service_title"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of service.
        """
        return reverse('service-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Service object (in Admin site etc.)
        """
        return self.service_title

    def save(self, *args, **kwargs):
        if self.service_image1:
            image = self.service_image1
            service_image1 = rescale_image(self, image)
        super(Service, self).save(*args, **kwargs)


class Staff(models.Model):
    """
    Model representing each staff.
    """

    # Fields
    name = models.CharField(max_length=100, help_text="Name of staff")
    position = models.CharField(max_length=100, help_text="Name of Job Position")
    order_of_appearance_on_website = models.IntegerField(
        help_text="Enter Desired Order of appearance on website")
    qualification = models.CharField(max_length=200, help_text="Enter Job Qualification")
    cv = HTMLField('content')
    staff_passport = models.ImageField(
        upload_to='staffimages/', default='staffimages/None/no-img.jpg')
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["order_of_appearance_on_website"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of staff profile.
        """
        return reverse('staff-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the profile object (in Admin site etc.)
        """
        return self.name


class Home(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    title = models.CharField(max_length=20, help_text="Main Home Title")
    location = models.CharField(max_length=20, help_text="Main Project Location")
    about_us = HTMLField('content')

    # Metadata

    class Meta:
        ordering = ["-title"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of home.
        """
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the home object (in Admin site etc.)
        """
        return self.title


class Press(models.Model):
    """
    Model for Press Releases
    """

    # Fields
    title = models.CharField(max_length=20, help_text="Enter title for press")
    article = HTMLField('content')
    date = models.DateField(null=True, blank=True)
    # Metadata

    class Meta:
        ordering = ["date"]

    # Methods
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of press.
        """
        return reverse('press-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the press object (in Admin site etc.)
        """
        return self.title
