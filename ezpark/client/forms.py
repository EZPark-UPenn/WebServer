from django import forms

class CarRegistrationForm(forms.Form):
    license_plate = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': '123ABC', 'class':'form-control'}))
    state = forms.CharField(max_length=2, required=True, widget=forms.TextInput(attrs={'placeholder': 'PA', 'class':'form-control'}))
    make = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Toyota', 'class':'form-control'}))
    model = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Camry', 'class':'form-control'}))
    color = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'placeholder': 'Green', 'class':'form-control'}))
