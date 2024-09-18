from django.urls import path

from apps.secondary.views import about, contact, methods

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('methods/',methods, name='methods' )
]
