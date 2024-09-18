from django.shortcuts import render, get_object_or_404

from apps.setting.models import Treat, Service, Reviews, TreatResult, Employe, VideoReview, WriteReview
from apps.secondary.models import Consultation
# Create your views here.
def index(request):
    treat = Treat.objects.all()[:6]
    service = Service.objects.all()[:6]
    reviews = Reviews.objects.all()
    return render(request, 'base/index.html', locals())

def what_we(request):
    treat = Treat.objects.all()
    result = TreatResult.objects.all()
    return render(request, 'whatWe.html', locals())

def emploes(request):
    emploe = Employe.objects.all()
    return render(request, 'emploes.html', locals())

def emploes_detail(request, id):
    emploe = get_object_or_404(Employe, id=id)
    return render(request, 'emploesById.html', locals())

def review(request):
    review = Reviews.objects.all()
    video_review = VideoReview.objects.all()
    write_review = WriteReview.objects.all()
    return render(request, 'revues.html', locals())

def service(request):
    service = Service.objects.all()
    consult = Consultation.objects.latest('id')
    return render(request, 'service.html', locals())

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    consult = Consultation.objects.latest('id')
    rec_service = Service.objects.all()[:2]
    all_service = Service.objects.all()
    return render(request, 'serviceSelected.html', locals())