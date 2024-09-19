from dataclasses import fields
from django import forms
from .models import Category, Stock, StockHistory

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=('category', 'item_name', 'quantity')
        
   
    
    def clean_item_name(self):
        item_name=self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('this field is required')
        for instance in Stock.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError( str(item_name) + ' is already exist')
        return item_name