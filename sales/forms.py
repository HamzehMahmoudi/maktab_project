from django import forms
from . import models


class QuoteitemForm(forms.ModelForm):
    class Meta:
        model = models.QuoteItem
        exclude = ['quote', 'created_on']
        fields = ['product', 'qty', 'discount']


class FollowUpForm(forms.ModelForm):
    class Meta:
        model = models.FollowUp
        exclude = ['organization', 'creator']
