from django import forms
from .models import Beasiswa, Mahasiswa, User

class BeasiswaForm(forms.ModelForm):
    class Meta:
        model = Beasiswa
        fields = '__all__'

class MahasiswaForm(forms.ModelForm):
    class Meta:
        model = Mahasiswa
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'border border-black p-1'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border border-black p-1'})
    )
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'border border-black p-1'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'border border-black p-1'}),
            'email': forms.EmailInput(attrs={'class': 'border border-black p-1'}),
        }
