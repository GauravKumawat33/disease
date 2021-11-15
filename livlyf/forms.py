from django.forms import ModelForm
from django import forms
from . models import Appoin, Personal_Detail,Feedbk

class Registration(forms.ModelForm):
    class Meta:
        model= Personal_Detail
        fields=['First_name','Last_name','Birth_date','Sex','City','Locality','Phone']
        
        # widgets={
        #     'Birth_date':forms.DateField(attrs={'class':'form-control'}),            
        #     'Sex':forms.TextInput(attrs={'class':'form-control'}),
        #     'City':forms.TextInput(attrs={'class':'form-control'}),
        #     'Locality':forms.TextInput(attrs={'class':'form-control'}),
        #     'Phone':forms.TextInput(attrs={'class':'form-control'}),
        # }
class Feedback(forms.ModelForm):
    class Meta:
        model= Feedbk
        fields=('Name','Email','Phone','Feedback')

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),            
            'Email':forms.TextInput(attrs={'class':'form-control'}),
            'Phone':forms.TextInput(attrs={'class':'form-control'}),
            'Feedback':forms.Textarea(attrs={'class':'form-control'}),
        }
