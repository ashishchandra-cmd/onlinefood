from myadmin.models import AdminLoginModel,StateModel,CityModel,CuisineModel
from django import forms
class AdminloginForm(forms.ModelForm):
    class Meta:
        model=AdminLoginModel
        fields=['username','password']


class StateForm(forms.ModelForm):
    class Meta:
        model=StateModel
        fields=['name','photo']  

class CityForm(forms.ModelForm):
    class Meta:
        model=CityModel
        fields=['name','photo','city_state']

class CuisineForm(forms.ModelForm):
    class Meta:
        model=CuisineModel
        fields=['type','photo']        
