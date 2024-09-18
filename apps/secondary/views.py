from django.shortcuts import render

from apps.secondary.models import About, Methods, Institution
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    return render(request, 'aboutUs.html', locals())

def contact(request):
    return render(request, 'contact.html', locals())

def methods(request):
    method = Methods.objects.latest('id')
    top_institution = Institution.objects.filter(text_position='top')
    bottom_institution = Institution.objects.filter(text_position='bottom')
    return render(request, 'metodika.html', locals())
