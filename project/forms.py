from django import forms

class registerform(forms.Form):
    name = forms.CharField(
        label="نام شما",
        widget=forms.TextInput(attrs={"name":"name",
                                      "class": "contact-name form-control",
                                      "id": "name",
                                      "type":"text",
                                      "placeholder":"نام شما"})
    )
    email = forms.CharField(
        label="ایمیل شما",
        widget=forms.EmailInput(attrs={"name":"name",
                                       "class":"contact-subject form-control",
                                       "id":"email",
                                       "type":"email",
                                       "placeholder":"ایمیل شما"})
    )
    message = forms.CharField(
        label="پیام شما",
        widget=forms.TextInput(attrs={"class":"contact-message",
                                     "id":"message",
                                     "rows":"6",
                                     "placeholder":"نامه شما"})
    )