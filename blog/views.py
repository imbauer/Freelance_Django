from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
import os

def home(request):

    # What you want the button to do.
    paypal_dict_01 = {
        "business": "sb-o81vn645225@business.example.com",
        "amount": "1.10",
        "currency_code": "CAD",
        "item_name": "basic",
        "invoice": request.user + "-basic-" + User.objects.get(username=request.user).profile.invoice_count,
        "notify_url": "https://mywickeddjangoapp.herokuapp.com/paypal/",
        "return": "https://mywickeddjangoapp.herokuapp.com/paypal-return/",
        "cancel_return": "https://mywickeddjangoapp.herokuapp.com/paypal-cancel/",
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    form_01 = PayPalPaymentsForm(initial=paypal_dict_01)

    paypal_dict_02 = {
        "business": "sb-o81vn645225@business.example.com",
        "amount": "2.20",
        "currency_code": "CAD",
        "item_name": "standard",
        "invoice": "unique-invoice-standard-04",
        "notify_url": "https://mywickeddjangoapp.herokuapp.com/paypal/",
        "return": "https://mywickeddjangoapp.herokuapp.com/paypal-return/",
        "cancel_return": "https://mywickeddjangoapp.herokuapp.com/paypal-cancel/",
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    form_02 = PayPalPaymentsForm(initial=paypal_dict_02)

    paypal_dict_03 = {
        "business": "sb-o81vn645225@business.example.com",
        "amount": "3.30",
        "currency_code": "CAD",
        "item_name": "unlimited",
        "invoice": "unique-invoice-unlimited-04",
        "notify_url": "https://mywickeddjangoapp.herokuapp.com/paypal/",
        "return": "https://mywickeddjangoapp.herokuapp.com/paypal-return/",
        "cancel_return": "https://mywickeddjangoapp.herokuapp.com/paypal-cancel/",
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }
    form_03 = PayPalPaymentsForm(initial=paypal_dict_03)

    # context = {
    #     'posts': Post.objects.all(),
    #     'form': form
    # }

    context = {"form_01": form_01, "form_02": form_02, "form_03": form_03}

    return render(request, 'blog/home.html', context)

@csrf_exempt
def paypal_return(request):
    context = {'post': request.POST, 'get': request.GET, 'method': request.method, 'user': request.user, 'body': request.body, 'path': request.path}
    request.user.profile.tokens = request.user.profile.tokens + 1;
    t = User.objects.get(username=request.user)
    t.profile.tokens = t.profile.tokens + 1  # change field
    t.profile.invoice_count = t.profile.invoice_count + 1
    t.save() # this will update only
    return render(request, 'blog/paypal_return.html', context)

@csrf_exempt
def paypal_cancel(request):
    context = {'post': request.POST, 'get': request.GET}
    return render(request, 'blog/paypal_cancel.html', context)


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
