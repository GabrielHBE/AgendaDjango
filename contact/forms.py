from . import models
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'classe-a','placeholder':'wrhite here'}),
                                 #label='teste'
                                 help_text='help text'
                                 )

    #def __init__(self, *args, **kwargs):
        #super.__init__(**args, **kwargs)

        #self.fields['first_name'].widget.attrs.update({
        #    'class':'classe-a','placeholder':'wrhite here'
        #})

    class Meta: 
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)

        #widgets = {
        #    #'first_name': forms.PasswordInput() A escrita fica escondida
        #    'first_name': forms.TextInput(attrs={'class':'classe-a','placeholder':'wrhite here'}) #Faz alterações no input
        #}

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
