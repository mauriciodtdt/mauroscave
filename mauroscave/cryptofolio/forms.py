from django import forms
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'api_secret': forms.PasswordInput(),
    }