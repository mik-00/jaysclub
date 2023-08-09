from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('new', views.PostCreateView.as_view(), name='post_new'),
    path('<int:pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name="post_update"),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name="post_delete"),
]