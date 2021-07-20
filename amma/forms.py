from django.forms import ModelForm, TextInput, NumberInput, Textarea
from .models import Application, Certificate, Reviews, Payed, Aboniment


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['client_name', 'client_phone_number', 'client_message']

        widgets = {
            'client_name': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Ваше имя*',
            }),
            'client_phone_number': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Ваш контактный номер телефона*',
            }),
            'client_message': TextInput(attrs={
                'class': 'zeman_form_text_input',
                'placeholder': 'Сообщение',
            })
        }


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'email', 'price']

        widgets = {
            'name': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Имя пользователя абонемента',
            }),
            'email': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Почта для отправки сертификата*',
            }),
            'price': NumberInput(attrs={
                'class': 'zeman_form_price_input',
                'placeholder': 'Сумма, доступная по абонементу*',
            })
        }


class AbonimentForm(ModelForm):
    class Meta:
        model = Aboniment
        fields = ['name', 'email']

        widgets = {
            'name': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Имя пользователя абонемента',
            }),
            'email': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Почта для отправки абонимента*',
            })
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'review']

        widgets = {
            'name': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Ваше имя*',
            }),
            'email': TextInput(attrs={
                'class': 'zeman_form_element_input',
                'placeholder': 'Почта для обратной связи*',
            }),
            'review': Textarea(attrs={
                'class': 'zeman_form_text_input',
                'placeholder': 'Текст отзыва*',
            })
        }


class PayedForm(ModelForm):
    class Meta:
        model = Payed
        fields = ['name', 'email']

        widgets = {
            'name': TextInput(attrs={
                'class': 'cur_serv_form_el',
                'placeholder': 'Ваше имя*',
            }),
            'email': TextInput(attrs={
                'class': 'cur_serv_form_el',
                'placeholder': 'Ваша почта*',
            }),
        }
