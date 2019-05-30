from django.shortcuts import render
from django.views import generic

# send mail with contact form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.paginator import Paginator
from infinite_scroll_pagination import paginator

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Project, Press, Staff, Home, Service, Industry, Department

# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    projects = Project.objects.all()
    projects = projects[0:4]
    press = Press.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable

    all_services = Service.objects.all()
    services = all_services[0:4]

    return render(
        request,
        'index.html',
        context={'projects': projects, 'press': press, 'services': services})


class ProjectListView(generic.ListView):
    model = Project
    model2 = Industry
    paginate_by = 8
    template_name = 'list_page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['industry_list'] = Industry.objects.all()
        context['service_list2'] = Service.objects.all()

        return context


class ProjectDetailView(generic.DetailView):
    model = Project
    #paginate_by = 1
    template_name = 'detail_page.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        project_service = self.get_object().service
        project_list = Project.objects.filter(
            service__service_title__icontains=project_service)
        paginator = Paginator(project_list, 5)
        page = self.request.GET.get('page')
        context['each_project'] = paginator.get_page(page)
        return context


class ServiceListView(generic.ListView):
    model = Service
    template_name = 'list_page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['industry_list'] = Industry.objects.all()
        context['project_list2'] = Project.objects.all()
        context['count_civil_projects'] = Project.objects.filter(
            service__service_title__icontains='Civil/')[:4]
        context['count_electrical_projects'] = Project.objects.filter(
            service__service_title__icontains='electrical')[:4]
        context['count_mgt_projects'] = Project.objects.filter(
            service__service_title__icontains='project')[:4]
        context['activate_link'] = 'active'
        return context


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'detail_page.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['industry_list'] = Industry.objects.all()
        context['project_list2'] = Project.objects.all()
        context['count_civil_projects'] = Project.objects.filter(
            service__service_title__icontains='Civil/')
        context['count_electrical_projects'] = Project.objects.filter(
            service__service_title__icontains='electrical')
        context['count_mgt_projects'] = Project.objects.filter(
            service__service_title__icontains='project')
        context['activate_link'] = 'active'
        return context


class IndustryDetailView(generic.DetailView):
    model = Industry
    template_name = 'detail_page.html'


class IndustryListView(generic.ListView):
    model = Industry
    template_name = 'list_page.html'


class StaffListView(generic.ListView):
    model = Staff
    paginate_by = 10
    #template_name = 'list_page.html'

    def get_context_data(self, **kwargs):
        context = super(StaffListView, self).get_context_data(**kwargs)
        all_services = Service.objects.all()
        context['services'] = all_services[0:3]
        context['departments'] = Department.objects.all()
        return context


class StaffDetailView(generic.DetailView):
    model = Staff


def emailView(request):
    print('This is the request: ')
    print(request)
    if request.method == 'GET':
        form = request.POST
    else:
        form = request.POST
        if form:
            subject = form['subject']
            from_email = form['from_email']
            message = form['message']
            try:
                #sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                send_mail(subject, message, from_email, ['admin@projectpluspotentials.com'])
                print('###I got here')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return render(request, 'success.html')
