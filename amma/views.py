from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
import string
import secrets
from .models import Massages, Spa, Spafortwo
import datetime
# Create your views here.


# ----------------------------------
# главная страница
def index_page(request):
    from .models import Application
    from .forms import ApplicationForm

    message = ''
    form = ApplicationForm

    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_phone_number = request.POST.get('client_phone_number')
        client_message = request.POST.get('client_message')

        mail = send_mail(
            'Заявка на запись',
            f'{client_name}, {client_phone_number}, {client_message}',
            'zemanqwe@gmail.com',
            ['lev.tokmakovich@mail.ru'],
            fail_silently=True
        )

        if mail:
            # создание новой записи в бд
            Application.objects.create(
                client_name=client_name,
                client_phone_number=client_phone_number,
                client_message=client_message,
            )
            message = (
                'Ваша заявка успешно доставлена'
                ' и принята в обработку!'
            )

            context = {
                'message': message,
                'form': ApplicationForm,
            }
            return render(request, 'amma/index_page.html', context)
        else:
            message = (
                'В настоящий момент мы не можем обработать вашу заявку.'
                ' Пожалуйста, повторите попытку позже.'
            )
            context = {
                'message': message,
                'form': ApplicationForm,
            }
            return render(request, 'amma/index_page.html', context)

    context = {
        'message': message,
        'form': ApplicationForm,
    }
    return render(request, 'amma/index_page.html', context)


# ----------------------------------
# основная страница цен и услуг
def prices_page(request):
    return render(request, 'amma/services.html', context={})


# ----------------------------------
# страница, содержащая в себе список всех доступных серитификатов
def certificates_page(request):
    from .models import ActiveCertificate

    certificates_list = ActiveCertificate.objects.all()

    context = {
        'certificates_list': certificates_list
    }
    return render(request, 'amma/certificate.html', context)


def aboniment_page(request):
    from .models import ActiveAboniment

    certificates_list = ActiveAboniment.objects.all()

    context = {
        'certificates_list': certificates_list
    }
    return render(request, 'amma/aboniment.html', context)


# ----------------------------------
# страница подтверждения оплаты и занесения оплаты в бд
def certificate_s(request):

    context = {
        'message': 'sss'
    }
    return render(request, 'amma/print.html', context)


# ----------------------------------
# страница выбранного сертификата
def cur_certificate(request, id_certificate):
    from .models import ActiveCertificate
    from .models import Certificate
    from .forms import CertificateForm

    certificate_info = ActiveCertificate.objects.filter(
        id_certificate=id_certificate
    )
    certificate_cat = ActiveCertificate.objects.filter(
        id_certificate=id_certificate
    ).values('certificate_name')

    errors_count = 0
    pref_count = 0
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        price = request.POST.get('price')
        certificate = (ActiveCertificate.objects.filter(
            id_certificate=id_certificate))

        # проверка почты
        if email == '':
            errors_count += 1
        for letter in email:
            if letter == '@':
                pref_count += 1

        if errors_count == 0 and pref_count == 1:
            # создание 15значного номера сертификата
            letters_and_digits = string.ascii_letters + string.digits
            certificate_number = ''.join(secrets.choice(
                letters_and_digits) for i in range(15))

            # отправка сертификата на почту
            context = {
                'name': name,
                'number': certificate_number,
                'certificate': certificate
            }
            mail = send_mail(
                'Сертификат AMMA',
                (
                    f'thanks, {name}! '
                ),
                'zemanqwe@gmail.com',
                [email],
                fail_silently=True,
                html_message=get_template(f'email/certificate1.html').render(context)
            )

            if mail:
                Certificate.objects.create(
                    name=name,
                    email=email,
                    price=price,
                    certificate_number=certificate_number,
                    certificate_category=certificate_cat,
                )
                return redirect('certificate_s')

            else:
                context = {
                    'certificate': certificate_info,
                    'form': CertificateForm,
                    'error_message': (
                        f'В настоящий момент мы не можем '
                        f'выпустить для вас сертификат. '
                        f'Попробуйте повторить попытку позже'
                    )
                }
                return render(request, 'amma/cur_certificate_page.html', context)

        else:
            context = {
                'certificate': certificate_info,
                'form': CertificateForm,
                'error_message': 'Проверьте правильность введённых вами данных'
            }
            return render(request, 'amma/cur_certificate_page.html', context)

    context = {
        'certificate': certificate_info,
        'form': CertificateForm
    }
    return render(request, 'amma/cur_certificate_page.html', context)


def cur_aboniment(request, id_aboniment):
    from .models import ActiveAboniment
    from .models import Aboniment
    from .forms import AbonimentForm

    aboniment_info = ActiveAboniment.objects.filter(
        id_aboniment=id_aboniment
    )
    aboniment_cat = ActiveAboniment.objects.filter(
        id_aboniment=id_aboniment
    ).values('aboniment_name')
    aboniment_price = ActiveAboniment.objects.filter(id_aboniment=id_aboniment).values('price')

    errors_count = 0
    pref_count = 0
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        certificate = (ActiveAboniment.objects.filter(
            id_aboniment=id_aboniment))

        # проверка почты
        if email == '':
            errors_count += 1
        for letter in email:
            if letter == '@':
                pref_count += 1

        if errors_count == 0 and pref_count == 1:
            # создание 15значного номера абонимента
            letters_and_digits = string.ascii_letters + string.digits
            aboniment_number = ''.join(secrets.choice(
                letters_and_digits) for i in range(15))

            # отправка сертификата на почту
            context = {
                'name': name,
                'number': aboniment_number,
                'certificate': certificate
            }
            mail = send_mail(
                'Сертификат AMMA',
                (
                    f'thanks, {name}! '
                ),
                'zemanqwe@gmail.com',
                [email],
                fail_silently=True,
                html_message=get_template(f'email/certificate1.html').render(context)
            )

            if mail:
                Aboniment.objects.create(
                    name=name,
                    email=email,
                    price=aboniment_price,
                    aboniment_number=aboniment_number,
                    aboniment_category=aboniment_cat,
                )
                return redirect('certificate_s')

            else:
                context = {
                    'certificate': aboniment_info,
                    'form': AbonimentForm,
                    'error_message': (
                        f'В настоящий момент мы не можем '
                        f'выпустить для вас сертификат. '
                        f'Попробуйте повторить попытку позже'
                    )
                }
                return render(request, 'amma/cur_certificate_page.html', context)

        else:
            context = {
                'certificate': aboniment_info,
                'form': AbonimentForm,
                'error_message': 'Проверьте правильность введённых вами данных'
            }
            return render(request, 'amma/cur_aboniment_page.html', context)

    context = {
        'certificate': aboniment_info,
        'form': AbonimentForm,
    }
    return render(request, 'amma/cur_certificate_page.html', context)


def massages_page(request):

    context = {
        'massages_list': Massages.objects.all()
    }
    return render(request, 'amma/massage.html', context)


def cur_massage_page(request, id_serv):
    serv_info = Massages.objects.filter(id_serv=id_serv)

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/cur_serv_page.html', context)


def cur_massage_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed

    serv = Massages.objects.filter(id_serv=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def spa_page(request):

    context = {
        'massages_list': Spa.objects.all()
    }
    return render(request, 'amma/massage.html', context)


def cur_spa_page(request, id_serv):
    serv_info = Spa.objects.filter(id_serv=id_serv)

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/cur_serv_page.html', context)


def cur_spa_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed

    serv = Spa.objects.filter(id_serv=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def spa_for_two_page(request):

    context = {
        'massages_list': Spafortwo.objects.all()
    }
    return render(request, 'amma/massage.html', context)


def cur_spa_for_two_page(request, id_serv):
    serv_info = Spafortwo.objects.filter(id_serv=id_serv)

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/cur_serv_page.html', context)


def cur_spa_for_two_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed

    serv = Spafortwo.objects.filter(id_serv=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def reviews(request):
    from .models import Reviews
    from .forms import ReviewForm

    message = ''
    form = ReviewForm

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        review = request.POST.get('review')

        if form.is_valid:
            new_review = Reviews.objects.create(
                name=name,
                email=email,
                review=review
            )

            if new_review:
                message = ('Спасбо за ваш отзыв! Он '
                           'будет направлен на проверку администратором.')
            else:
                message = ('К сожалению, в настоящий момент мы не можем '
                           'принять на рассмотрение ваш отзыв. '
                           'Пожалуйста, повторите попытку позже.')

            return render(request, 'amma/reviews_page.html', context={
                'reviews_list': Reviews.objects.all(),
                'message': message,
                'form': form
            })
        else:
            message = 'Проверьте правильность заполнения полей'

    return render(request, 'amma/reviews_page.html', context={
        'reviews_list': Reviews.objects.all(),
        'message': message,
        'form': form
    })


def appli_online_page(request):
    from .models import Application
    from .forms import ApplicationForm

    message = ''
    form = ApplicationForm

    if request.method == 'POST':
        client_name = request.POST.get('client_name')
        client_phone_number = request.POST.get('client_phone_number')
        client_message = request.POST.get('client_message')

        mail = send_mail(
            'Заявка на запись',
            f'{client_name}, {client_phone_number}, {client_message}',
            'zemanqwe@gmail.com',
            ['lev.tokmakovich@mail.ru'],
            fail_silently=True
        )

        if mail:
            # создание новой записи в бд
            Application.objects.create(
                client_name=client_name,
                client_phone_number=client_phone_number,
                client_message=client_message,
            )
            message = (
                'Ваша заявка успешно доставлена'
                ' и принята в обработку!'
            )

            context = {
                'message': message,
                'form': ApplicationForm,
            }
            return render(request, 'amma/appli_online_page.html', context)
        else:
            message = (
                'В настоящий момент мы не можем обработать вашу заявку.'
                ' Пожалуйста, повторите попытку позже.'
            )
            context = {
                'message': message,
                'form': ApplicationForm,
            }
            return render(request, 'amma/appli_online_page.html', context)

    context = {
        'message': message,
        'form': ApplicationForm,
    }
    return render(request, 'amma/appli_online_page.html', context)


def workers_page(request):
    from .models import Workers

    context = {
        'workers_list': Workers.objects.all()
    }
    return render(request, 'amma/workers_page.html', context)


def gallery_page(request):
    from .models import Photo

    photo_list = Photo.objects.all()

    context = {
        'photo_list': photo_list,
    }
    return render(request, 'amma/gallery.html', context)


def hamam_page(request):
    from .models import Hamam
    serv_info = Hamam.objects.all()

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/hamam_page.html', context)


def cur_hamam_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed
    from .models import Hamam

    serv = Hamam.objects.filter(id_hamam=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def salt_page(request):
    from .models import Salt
    serv_info = Salt.objects.all()

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/salt_page.html', context)


def cur_salt_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed
    from .models import Salt

    serv = Salt.objects.filter(id_salt=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def hidromassage_page(request):
    from .models import Hidromassage
    serv_info = Hidromassage.objects.all()

    context = {
        'serv_info': serv_info
    }
    return render(request, 'amma/hidromassage.html', context)


def cur_hidromassage_page_mail(request, id_serv, price, time):
    from .forms import PayedForm
    from .models import Payed
    from .models import Hidromassage

    serv = Hidromassage.objects.filter(id_hidromassage=id_serv)
    serv_name = serv[0].name
    serv_price = price

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        context = {
            'name': name,
            'serv': serv_name,
            'price': price,
            'time': time,
        }

        send_mail(
            'Сертификат AMMA',
            f'thanks, {name}! ',
            'zemanqwe@gmail.com',
            [email],
            fail_silently=True,
            html_message=get_template(f'email/serv1.html').render(context)
        )

        Payed.objects.create(name=name,
                             email=email,
                             sum=price,
                             time=time,
                             status=f'{serv_name} - Оплачен')

        return redirect('certificate_s')

    context = {
        'form': PayedForm,
        'serv': serv_name,
        'price': serv_price,
        'time': time,
    }
    return render(request, 'amma/cur_massage_page_mail.html', context)


def actions_page(request):
    from .models import Actions

    context = {
        'actions_list': Actions.objects.all()
    }
    return render(request, 'amma/actions_page.html', context)
