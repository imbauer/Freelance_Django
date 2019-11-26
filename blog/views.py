from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
import os

def home(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "sb-o81vn645225@business.example.com",
        "amount": "1.00",
        "currency_code": "CAD",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id1",
        "notify_url": "https://mywickeddjangoapp.herokuapp.com/paypal/",
        "return": "https://mywickeddjangoapp.herokuapp.com/paypal-return/",
        "cancel_return": "https://mywickeddjangoapp.herokuapp.com/paypal-cancel/",
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }


    form = PayPalPaymentsForm(initial=paypal_dict)

    # context = {
    #     'posts': Post.objects.all(),
    #     'form': form
    # }

    context = {"form": form}

    return render(request, 'blog/home.html', context)

@csrf_exempt
def paypal_return(request):
    context = {'post': request.POST, 'get': request.GET}
    return render_to_response('blog/paypal_return.html', context)

def paypal_cancel(request):
    context = {'post': request.POST, 'get': request.GET}
    return render_to_response('blog/paypal_cancel.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def paypal_register(request):
    return render(request, 'blog/paypal_register.html')
