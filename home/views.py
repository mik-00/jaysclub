from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView, DetailView, UpdateView, ListView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ReportsForm
from .models import Reports

class HomeView(ListView):
    """
    View that displays the home page containing today's date, the site's latest 
    reports, a game schedule table, and a live score SportsRadar widget.
    """
    model = Reports
    template_name = "home/welcome.html"
    extra_context = {"today": datetime.today()}
    context_object_name = "reports_list"

    def get_queryset(self):
        """ Show last 6 Reports with admin approval. """
        reports = Reports.objects.filter(admin_approved=True).order_by("-created")[:6]
        return reports
    
class ReportListView(ListView):
    """
    View that displays all Reports in a list.
    """
    model = Reports
    context_object_name = "reports_list"
    template_name = "home/report_list.html"
    login_url = "/login"

    def get_queryset(self):
        """ Show only Reports with admin approval in order from newest to oldest. """
        return Reports.objects.filter(admin_approved=True).order_by("-created")

class AuthorizedView(LoginRequiredMixin, TemplateView):
    """
    View that displays the message users see when entering forbidden areas of the site.
    """
    template_name = "home/authorized.html"
    login_url = "/login"

class LoginInterfaceView(LoginView):
    """
    View that allows Users to log in with their credentials.
    """
    template_name = "home/login.html"

class LogoutInterfaceView(LogoutView):
    """
    View that displays the log out farewell message.
    """
    template_name = "home/loggedout.html"

class SignupView(CreateView):
    """
    View that creates a new User and displays sign up form interface.
    """
    form_class = UserCreationForm
    template_name = "home/register.html"
    success_url = "/"

    def get(self,request, *args, **kwargs): 
        """ Only allow non-signed-in Users to see the sign up page. """
        if self.request.user.is_authenticated:
            return redirect("home")
        return super().get(request, *args, **kwargs)
    
class ReportCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView, SuccessMessageMixin):
    """
    View that allows a user to create a Report.
    """
    model = Reports
    form_class = ReportsForm
    success_url = "/"
    template_name = "home/report_form.html"
    login_url = "/login"
    success_message = "Submission successful"

    def form_valid(self, form):
        """ 
        If form is valid, saves Post and associates it with the user, then 
        redirects to the success URL. 
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def test_func(self): 
        """ Ensures the user creating a report has a superuser role. """
        if self.request.user.is_superuser:
            return True
        return False

    def get_success_message(self):
        return self.success_message

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View that handles deleting a Report and displays deletion confirmation prompt.
    """
    model = Reports
    success_url = "/"
    template_name = "home/report_delete.html"
    login_url = "/login"

    def test_func(self): 
        """ Ensures the user deleting is the same as the author. """
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing of a current Report by the User. 
    """
    model = Reports
    form_class = ReportsForm
    success_url = "/"
    template_name = "home/report_form.html"
    login_url = "/login" 

    def test_func(self): 
        """ Ensures the user editing is the same as the author. """        
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

class ReportDetailView(DetailView):
    """
    View for displaying an individual Report's image, title, and body of text in full.
    """
    model = Reports
    context_object_name = "report"
    template_name = "home/report_detail.html"
