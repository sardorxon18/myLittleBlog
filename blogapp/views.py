from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import MyPost


# Create your views here.
class BlogListView(ListView):
    model = MyPost
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = MyPost
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = MyPost
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = MyPost  # Add the model
    template_name = "post_edit.html"  # Specify the template
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = MyPost
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
