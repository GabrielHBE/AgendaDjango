from . import models
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept':'/*',}))

    class Meta: 
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category','picture')


    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name==last_name:
            self.add_error('first_name',ValidationError('Os nomes não podem ser iguais',code='invalid1'))
            self.add_error('last_name',ValidationError('Os nomes não podem ser iguais',code='invalid2')) 

        return super().clean()
    
    #def clean_first_name(self):
    #    first_name = self.cleaned_data.get('first_name')
    #
    #    if first_name == 'abc':
    #        raise ValidationError('nao digite abc',code='invalid')


    #    return first_name



class RegisterForm(UserCreationForm):
    pass