from django.forms import ModelForm
from django import forms
from .models import deliveries
from django.utils.translation import gettext_lazy as _

class deliveryForm(ModelForm):
    class Meta:
        model= deliveries
        fields = ['title','size','area','delType','description']
        labels = {
            'delType': _('Type'),
        }
        
