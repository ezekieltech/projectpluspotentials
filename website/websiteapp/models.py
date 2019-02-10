from django.db import models
from django.urls import reverse

from PIL import Image
from .utilities import rescale_image
from django.core.files.uploadedfile import SimpleUploadedFile

from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# Create your models here.


class Project(models.Model):
    """
    Model representing a project (a specific project).
    """
    title = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    #author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the project")
    project_article = models.TextField(max_length=1000, help_text="Enter prject article")
    project_date = models.DateField(null=True, blank=True)
    project_image1 = models.ImageField(
        upload_to='projectimages/', default='projectimages/None/no-img.jpg')
    project_image2 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')
    project_image3 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')
    project_image4 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')
    project_image5 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')
    project_image6 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')
    project_image7 = models.ImageField(
        upload_to='projectimages/gallery/', default='projectimages/gallery/None/no-img.jpg')

    SERVICE = (
        ('con', 'construction'),
        ('bui', 'building'),
        ('rea', 'real estate')
    )
    project_service = models.CharField(max_length=3, choices=SERVICE, blank=True,
                                       default='og', help_text='What is project service description')

    INDUSTRY = (
        ('og', 'Oil and Gas'),
        ('ed', 'Education'),
        ('po', 'Power'),
        ('el', 'electrical')
    )
    industry = models.CharField(max_length=2, choices=INDUSTRY, blank=True,
                                default='og', help_text='Client in what Industry?')
    #genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    class Meta:
        ordering = ["project_date"]

    def get_absolute_url(self):
        """
        Returns the url to access a particular project instance.
        """
        return reverse('project-detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        project_images_to_resize = [
            self.project_image1,
            self.project_image2,
            self.project_image3,
            self.project_image4,
            self.project_image5,
            self.project_image6,
            self.project_image7
        ]
        for project_img in project_images_to_resize:
            if project_img:
                image = project_img
                self.project_img = rescale_image(self, image)
        super(Project, self).save(*args, **kwargs)


class Service(models.Model):
    """
    Model representing each service.
    """

    # Fields
    service_title = models.CharField(max_length=20, help_text="Title of service")
    service_article = models.TextField(max_length=1000, help_text='Enter article here')
    service_summary = models.CharField(max_length=200, help_text="Summary for service")
    service_date = models.DateField(null=True, blank=True)
    service_image1 = models.ImageField(
        upload_to='serviceimages/',
        default='serviceimages/None/no-img.jpg')

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
    order_of_appearance_on_website = models.IntegerField(max_length=2)
    qualification = models.CharField(max_length=100, help_text="Enter Job Qualification")
    cv = models.TextField(max_length=1000, help_text='Enter article here')
    staff_passport = models.ImageField(
        upload_to='staffimages/', default='staffimages/None/no-img.jpg')

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
    about_us = models.TextField(max_length=1000, help_text='About Project Plus Potentials')

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
    article = models.TextField(max_length=100, help_text="Enter title for press")
    date = models.DateField(null=True, blank=True)
    # Metadata

    class Meta:
        ordering = ["-title"]

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
