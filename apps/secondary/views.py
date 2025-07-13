from django.shortcuts import render, redirect, get_object_or_404

from apps.setting.models import Setting, Treat, Service, Reviews, MainSlider
from apps.secondary.models import About, Methods, Institution, ContactRequest, News
# Create your views here.


def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    setting = Setting.objects.latest('id')
    method = Methods.objects.latest('id')
    top_institution = Institution.objects.filter(text_position='top')
    bottom_institution = Institution.objects.filter(text_position='bottom')
    return render(request, 'aboutUs.html', locals())


def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        appointment_date = request.POST.get('appointment_date')
        phone = request.POST.get('phone')
        description = request.POST.get('description')
        
        # Получаем информацию о городе
        city_type = request.POST.get('type')
        city = 'Ош' if city_type == 'admin' else 'Бишкек'

        # Сохраняем данные в базу данных
        ContactRequest.objects.create(
            name=name,
            last_name=last_name,
            appointment_date=appointment_date,
            phone=phone,
            description=description,
            city=city
        )

        # Перенаправляем на страницу контактов
        return redirect('contact')  # Измените 'contact' на правильный URL

    # Для GET-запросов отображаем страницу с формой
    return render(request, 'contact.html', locals())


def methods(request):
    setting = Setting.objects.latest('id')
    method = Methods.objects.latest('id')
    top_institution = Institution.objects.filter(text_position='top')
    bottom_institution = Institution.objects.filter(text_position='bottom')
    return render(request, 'metodika.html', locals())

def news(request):
    setting = Setting.objects.latest('id')
    treat = Treat.objects.all()[:6]
    service = Service.objects.all()[:6]
    reviews = Reviews.objects.all()
    news_list = News.objects.filter(is_published=True)[:6]  # Получаем последние 6 опубликованных новостей
    try:
        main_slider = MainSlider.objects.first()
    except MainSlider.DoesNotExist:
        main_slider = None
    return render(request, 'news.html', locals())

def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news_item = get_object_or_404(News, id=id, is_published=True)
    return render(request, 'news_detail.html', locals())