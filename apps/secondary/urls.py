from django.urls import path

from apps.secondary.views import about, contact, methods, news, news_detail, scientific_work

urlpatterns = [
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('methods/',methods, name='methods' ),
    path('news/', news, name='news'),
    path('news/<int:id>/', news_detail, name='news_detail'),
    path('scientific-work/', scientific_work, name='scientific_work')
]
