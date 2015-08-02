from django import forms
from django.core.exceptions import ObjectDoesNotExist
from task.form_validators import FormValidators
from task.models import CustomUser


class SignUpForm(forms.ModelForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
                                validators=[FormValidators.CHAR_VALIDATOR])

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email',)

    def save(self, *args, **kwargs):
        user = super(SignUpForm, self).save(*args, **kwargs)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.username = self.cleaned_data['email']
        user.save()

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True