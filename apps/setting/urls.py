from django.urls import path

from apps.setting.views import index, what_we, what_we_detail, emploes, emploes_detail, review, service, service_detail
urlpatterns = [
    path('', index, name='index'),
    path('whatwe/', what_we, name='what_we'),
    path('whatwe/<int:id>/', what_we_detail, name='what_we_detail'),
    path('emploes/', emploes, name='emploes'),
    path('employe/<int:id>/', emploes_detail, name='emploe_detail'),
    path('reviews/', review, name='review'),
    path('service/', service, name='service'),
    path('service/<int:id>/', service_detail, name='service_detail')
]
