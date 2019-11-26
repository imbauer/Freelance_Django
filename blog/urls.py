from django.urls import path
from django.conf.urls import include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    # path('', PostListView.as_view(), name='blog-home'),
    path('', views.home, name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('paypal_register/', views.paypal_register, name='paypal-register'),
    path('paypal-return/', views.paypal_return),
    path('paypal-cancel/', views.paypal_cancel),
    path('a-very-hard-to-guess-url/', include('paypal.standard.ipn.urls')),
]
