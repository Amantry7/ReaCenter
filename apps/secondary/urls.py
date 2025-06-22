from django.urls import path

from apps.secondary.views import about, contact, methods, news

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('methods/',methods, name='methods' ),
    path('news', news, name='news')
]
