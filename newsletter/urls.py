from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('newsletters/', views.newsletter_list, name='newsletter_list'),
    path('newsletters/create/', views.newsletter_create, name='newsletter_create'),
    path('newsletters/<int:pk>/edit/', views.newsletter_edit, name='newsletter_edit'),
    path('newsletters/<int:pk>/delete/', views.newsletter_delete, name='newsletter_delete'),
    path('newsletters/<int:pk>/send/', views.send_newsletter, name='send_newsletter'),
     path('unsubscribe/<str:token>/', views.unsubscribe, name='unsubscribe'),
]