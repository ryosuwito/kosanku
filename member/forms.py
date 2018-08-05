from django.contrib.auth.models import User
from django import forms 
from .models import Member

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm,self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

    class Meta:
        model = User
        fields = ("username","email","password")

class MemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemberForm,self).__init__(*args, **kwargs)
        self.fields['profile_photo'].widget.attrs['onChange'] = 'Handlechange(event)'
        self.fields['profile_photo'].widget.attrs['class'] = 'hidden'
        self.fields['nama_lengkap'].widget.attrs['placeholder'] = 'Nama Lengkap'
        self.fields['alamat_lengkap'].widget = forms.Textarea() 
        self.fields['alamat_lengkap'].widget.attrs['rows'] = '3'
        self.fields['alamat_lengkap'].widget.attrs['placeholder'] = 'Alamat Lengkap\nContoh: Jl. Angkasa 1 Blok AF6 NO 18'
    class Meta:
        model = Member 
        fields = ("profile_photo","nama_lengkap", "alamat_lengkap")
