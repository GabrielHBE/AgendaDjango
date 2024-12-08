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
        #cleaned_data = self.cleaned_data

        self.add_error('first_name',ValidationError('Error message',code='invalid1'))
        self.add_error('first_name',ValidationError('Error message',code='invalid2'))
    

        return super().clean()
