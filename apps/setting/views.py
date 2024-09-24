from django.shortcuts import render, get_object_or_404, redirect

from apps.setting.models import Treat, Service, Reviews, TreatResult, Employe, VideoReview, WriteReview, Setting
from apps.secondary.models import Consultation
# Create your views here.


def index(request):
    setting = Setting.objects.latest('id')
    treat = Treat.objects.all()[:6]
    service = Service.objects.all()[:6]
    reviews = Reviews.objects.all()
    return render(request, 'base/index.html', locals())


def what_we(request):
    setting = Setting.objects.latest('id')
    treat = Treat.objects.all()
    result = TreatResult.objects.all()
    return render(request, 'whatWe.html', locals())


def what_we_detail(request, id):
    setting = Setting.objects.latest('id')
    treat = Treat.objects.all()
    treat_detail = get_object_or_404(Treat, id=id)
    result = TreatResult.objects.all()
    return render(request, 'whtatWeSelect.html', locals())


def emploes(request):
    setting = Setting.objects.latest('id')
    emploe = Employe.objects.all()
    return render(request, 'emploes.html', locals())


def emploes_detail(request, id):
    setting = Setting.objects.latest('id')
    emploe = get_object_or_404(Employe, id=id)
    return render(request, 'emploesById.html', locals())


def review(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        # Получаем данные из POST-запроса
        name = request.POST.get('name')
        first_name = request.POST.get('first_name')
        text = request.POST.get('text')

        # Создаем новый отзыв и сохраняем его в базе данных
        Reviews.objects.create(
            name=name,
            first_name=first_name,
            text=text
        )

        # Перенаправление или сообщение об успешном создании
        return redirect('review')  # Замените на нужный URL

    # Если GET-запрос
    review = Reviews.objects.filter(is_approved=True)
    video_review = VideoReview.objects.all()
    write_review = WriteReview.objects.all()
    return render(request, 'revues.html', locals())


def service(request):
    setting = Setting.objects.latest('id')
    service = Service.objects.all()
    consult = Consultation.objects.latest('id')
    return render(request, 'service.html', locals())


def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    setting = Setting.objects.latest('id')
    consult = Consultation.objects.latest('id')
    rec_service = Service.objects.all()[:2]
    all_service = Service.objects.all()
    return render(request, 'serviceSelected.html', locals())
