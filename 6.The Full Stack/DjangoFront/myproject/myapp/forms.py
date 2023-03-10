from django import forms

class UserCommentsForm(forms.Form):
    first_name = forms.CharField(max_length= 200)
    last_name = forms.CharField(max_length= 200)
    comment = forms.CharField(max_length= 1000)