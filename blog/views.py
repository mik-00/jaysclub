from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .forms import PostsForm
from .models import Posts

class BlogListView(LoginRequiredMixin, ListView):
    """
    View that displays all blog Posts in a list.
    """
    model = Posts
    context_object_name = "posts"
    template_name = "blog/blog_list.html"
    login_url = "/login"

    def get_queryset(self):
        """ Display Posts from newest to oldest. """
        return Posts.objects.order_by("-created")

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View that allows a user to create a Post.
    """
    model = Posts
    form_class = PostsForm
    success_url = "/blog"
    template_name = "blog/post_form.html"
    login_url = "/login"

    def form_valid(self, form): 
        """ 
        If form is valid, saves Post and associates it with the user, then 
        redirects to the success URL. 
        """
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View that handles deleting a Post and displays deletion confirmation prompt.
    """
    model = Posts
    success_url = "/blog"
    template_name = "blog/post_delete.html"
    login_url = "/login"

    def test_func(self): 
        """ Ensures the user deleting is the same as the author. """
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for editing a Post by the User. 
    """
    model = Posts
    form_class = PostsForm
    success_url = '/blog'
    template_name = "blog/post_form.html"
    login_url = "/login"

    def test_func(self): 
        """ Ensures the user editing is the same as the author. """
        report = self.get_object()
        if self.request.user == report.user:
            return True
        return False

class PostDetailView(LoginRequiredMixin, DetailView):
    """
    View for displaying an individual Post's title and body of text in full.
    """
    model = Posts
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    login_url = "/login"