from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('organisation', )

class ECForm(forms.Form):
    ec_name = forms.CharField(label='EC Name', max_length=100)


class GeneForm(ModelForm):

    def clean(self):
        cleaned_data = super(GeneForm, self).clean()
        entity = cleaned_data.get("entity")
        sense = cleaned_data.get("sense")

        if not entity == "Chromosome" and not entity == "Plasmid":
            raise forms.ValidationError("Entity must be 'Chromosome' or 'Plasmid'")
        if not sense == "+" and not sense == "-":
            raise forms.ValidationError("Sense must be '+' or '-'")
        return(cleaned_data)

    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense',
                  'start_codon', 'sequencing', 'ec']
