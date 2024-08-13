from django import forms

from store.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-control'}),
        }
        
        # help_texts = {
        #     'title': 'Enter Valid Title'
        # }
        
    def clean(self):
        super (TaskForm, self).clean()
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        
        if len(title) < 5:
            self._errors['title'] = self.error_class([
                'Title ma 5 ota vanda dherai character huna paryo.'
            ])
            
        if len(description) < 10:
            self._errors['description'] = self.error_class([
                'Description ma 5 ota vanda dherai character huna paryo.'
            ])
            
        return self.cleaned_data

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class':'form-control'})
    )
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control'})
    )
    