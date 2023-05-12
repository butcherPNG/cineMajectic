from django import forms
from django.contrib.auth.forms import UserCreationForm
from myapp1.models import User, SearchQuery


class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='', required=True, max_length=254,
                            widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    phone_number = forms.CharField(label='', max_length=20, required=True,
                           widget=forms.TextInput(attrs={'placeholder': '+7(XXX)XXX-XX-XX'}))
    email = forms.EmailField(label='', required=True, max_length=254,
                             widget=forms.TextInput(attrs={'placeholder': 'example@yandex.ru'}))
    password1 = forms.CharField(label='', required=True, max_length=254,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', required=True, max_length=254,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))


    #name = forms.CharField(label='', required=True, max_length=254,
                           #widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    #name = forms.CharField(label='Имя', required=True, max_length=254)
    #surname = forms.CharField(label='', required=True, max_length=254,
                              #widget=forms.TextInput(attrs={'placeholder': 'Введите '}))
    #patronymic = forms.CharField(label='', required=False, max_length=254,
                                 #widget=forms.TextInput(attrs={'placeholder': ''}))
    #username = forms.CharField(label='', required=True, max_length=254,
                               #widget=forms.TextInput(attrs={'placeholder': 'Введите желаемый логин'}))
    #email = forms.EmailField(label='', required=True, max_length=254,
                             #widget=forms.TextInput(attrs={'placeholder': 'Введите почту'}))
    #password1 = forms.CharField(label='', required=True, max_length=254, widget=forms.PasswordInput)
    #password2 = forms.CharField(label='', required=True, max_length=254, widget=forms.PasswordInput)
    #rule = forms.BooleanField(label='Нажимая на', required=True)

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))

        if commit:
            user.save()
            return user

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2')



class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['query_text']