from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us/', views.about),
    path('home/', views.home, name='home'),  # Додано URL-адресу для сторінки "/home"
    path('signup/', views.signup, name='signup'),
    path('send-connection-request/<int:receiver_id>/', views.send_connection_request, name='send_connection_request'),
    path('accept-connection-request/<int:connection_id>/', views.accept_connection_request, name='accept_connection_request'),
    path('reject-connection-request/<int:connection_id>/', views.reject_connection_request, name='reject_connection_request'),
    path('my-network/', views.my_network, name='my_network'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]

