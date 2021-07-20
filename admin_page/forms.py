from django.forms import ModelForm, TextInput, FileInput
from django.contrib.auth.models import User
from amma.models import Workers, Actions


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'input_username',
                'placeholder': 'Username...',
            }),
            'password': TextInput(attrs={
                'class': 'input_password',
                'placeholder': 'Password...',
                'type': 'password',
            })
        }


class WorkersForm(ModelForm):
    class Meta:
        model = Workers
        fields = ['worker_img', 'worker_name', 'worker_desc']

        widgets = {
            'worker_img': FileInput(attrs={
                'class': 'input_worker_img',
                'value': 'Фотография',
            }),
            'worker_name': TextInput(attrs={
                'class': 'input_worker_name',
                'placeholder': 'Имя',
            }),
            'worker_desc': TextInput(attrs={
                'class': 'input_worker_desc',
                'placeholder': 'Описание',
            })
        }


class ActionForm(ModelForm):
    class Meta:
        model = Actions
        fields = ['action_img', 'action_name']

        widgets = {
            'action_img': FileInput(attrs={
                'class': 'input_worker_img',
                'value': 'Фотография',
            }),
            'action_name': TextInput(attrs={
                'class': 'input_worker_name',
                'placeholder': 'Название акции',
            })
        }