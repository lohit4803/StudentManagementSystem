from django import forms
from admissions.models import Student

class studentmodelform(forms.ModelForm):
    class Meta:
        model = Student
        fields  = '__all__'

class vendorform(forms.Form):
    name = forms.CharField(max_length=10)
    address = forms.CharField()
    contact = forms.CharField()
    item = forms.CharField()
