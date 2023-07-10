from django import forms


class RegistrationForm(forms.Form):
    # class Meta:
    #     model = Participant
    #     fields = ['email']
    email = forms.EmailField(label='Your email!')