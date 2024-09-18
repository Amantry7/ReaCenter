from django.shortcuts import render, redirect

from apps.secondary.models import About, Methods, Institution, ContactRequest
# Create your views here.
def about(request):
    about = About.objects.latest('id')
    return render(request, 'aboutUs.html', locals())

def contact(request):
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        appointment_date = request.POST.get('appointment_date')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        # Сохраняем данные в базу данных
        ContactRequest.objects.create(
            name=name,
            last_name=last_name,
            appointment_date=appointment_date,
            phone=phone,
            description=description
        )

        # Перенаправляем на страницу контактов
        return redirect('contact')  # Измените 'contact' на правильный URL

    # Для GET-запросов отображаем страницу с формой
    return render(request, 'contact.html', locals())

def methods(request):
    method = Methods.objects.latest('id')
    top_institution = Institution.objects.filter(text_position='top')
    bottom_institution = Institution.objects.filter(text_position='bottom')
    return render(request, 'metodika.html', locals())
