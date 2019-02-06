from django.shortcuts import render
from django.views import generic

# send mail with contact form
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

from .models import Project, Press, Staff, Home, Service

# Create your views here.


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    projects = Project.objects.all().count()
    press = Press.objects.all().count()
    # Available books (status = 'a')
    # num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    # num_authors=Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'projects': projects, 'press': press})


class ProjectListView(generic.ListView):
    model = Project
    paginate_by = 10
    template_name = 'list_page.html'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'detail_page.html'


class ServiceListView(generic.ListView):
    model = Service
    paginate_by = 10
    template_name = 'list_page.html'


class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'detail_page.html'


class StaffListView(generic.ListView):
    model = Staff
    paginate_by = 10
    #template_name = 'list_page.html'


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
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return render(request, 'success.html')
