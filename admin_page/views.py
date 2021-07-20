from django.shortcuts import render, redirect
from .forms import UserForm, WorkersForm, ActionForm
from django.contrib.auth import authenticate, login, logout
from amma.models import Application, Certificate, Reviews, Workers, Payed, Aboniment, Actions

# Create your views here.


def login_admin_page(request):
    if request.user.is_authenticated:
        return redirect('admin_control_page')

    error_message = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('admin_control_page')
            else:
                error_message = ('Данный пользователь недоступен.'
                                 ' Обратитесь к администратору')
        else:
            error_message = 'Неверное имя пользователя или пароль'

    context = {
        'form': UserForm,
        'error_message': error_message,
    }
    return render(request, 'admin_page/login_admin_page.html', context)


def admin_control_page(request):
    if not request.user.is_authenticated:
        return redirect('login_admin_page')

    applications_list = Application.objects.all()

    context = {
        'applications_list': applications_list.order_by('-id_application'),
    }
    return render(request, 'admin_page/admin_control_page.html', context)


def admin_reviews_page(request):
    if not request.user.is_authenticated:
        return redirect('login_admin_page')

    reviews_list = Reviews.objects.all()

    context = {
        'reviews_list': reviews_list.order_by('-id_review')
    }
    return render(request, 'admin_page/reviews_page.html', context)


def admin_reviews_update(request, id_review):
    Reviews.objects.filter(id_review=id_review).update(status='Сохранён')
    return redirect('admin_reviews_page')


def admin_reviews_delete(request, id_review):
    Reviews.objects.filter(id_review=id_review).delete()
    return redirect('admin_reviews_page')


def admin_payment_page(request):
    if not request.user.is_authenticated:
        return redirect('login_admin_page')

    context = {
        'payment_list': Payed.objects.all().order_by('-id_payed')
    }
    return render(request, 'admin_page/payment_page.html', context)


def admin_payment_update(request, id_payed):
    Payed.objects.filter(id_payed=id_payed).update(use_status='Использован')
    return redirect('admin_payment_page')


def admin_certificates_page(request):
    if not request.user.is_authenticated:
        return redirect('login_admin_page')

    certificates_list = Certificate.objects.all()

    context = {
        'certificates_list': certificates_list.order_by('-id_certificate'),
    }
    return render(request, 'admin_page/admin_certifications_page.html', context)


def admin_certificate_status_update(request, id_certificate):
    Certificate.objects.filter(id_certificate=id_certificate).update(status='закрыт')
    return redirect('admin_certificates_page')


def admin_aboniment_page(request):
    if not request.user.is_authenticated:
        return redirect('login_admin_page')

    aboniment_list = Aboniment.objects.all()

    context = {
        'aboniment_list': aboniment_list.order_by('-id_aboniment'),
    }
    return render(request, 'admin_page/aboniment_page.html', context)


def workers(request):
    workers_list = Workers.objects.all()
    message = ''

    if request.method == 'POST':
        form = WorkersForm(request.POST, request.FILES)

        if form.is_valid:
            worker_create = form.save()

            if worker_create:
                message = 'Поле сотрудника успешно создано!'
            else:
                message = ('При создании поля сотрудника возникли проблемы. '
                           'Проверьте корректность введённых данных и, '
                           'если проблема не исчезнет, обратитесь к '
                           'администратору.')
            return redirect('workers')

    form = WorkersForm
    context = {
        'message': message,
        'form': WorkersForm,
        'workers_list': workers_list
    }
    return render(request, 'admin_page/workers.html', context)


def workers_delete(request, id_worker):
    Workers.objects.filter(id_worker=id_worker).delete()
    return redirect('workers')


def actions(request):
    message = ''
    form = ActionForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
        else:
            message = 'Проверьте правильность введённых даных'

    context = {
        'actions_list': Actions.objects.all().order_by('-id_action'),
        'form': ActionForm,
        'message': message,
    }
    return render(request, 'admin_page/actions_page.html', context)


def actions_delete(request, id_action):
    Actions.objects.filter(id_action=id_action).delete()
    return redirect('actions')
