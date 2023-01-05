from .models import ContactForm
from django import forms


class ContactUs(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['yourName','email','Phonenumber','Subject','Message']
        labels = {
            "yourName":"Full Name",
            "email":"Email",
            "Phonenumber":"Mobile Number",
            "Subject":"Subject",
            "Message":"Message"
        }
        widgets = {
            "yourName": forms.TextInput(attrs={"Placeholder":"Enter Your Full Name","class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter a Valid Email"}),
            "Phonenumber":forms.TextInput(attrs={"placeholder":"Enter Your Phone Number","class":"form-control"}),
            "Message" : forms.Textarea(attrs={"placeholder":"Tell Us About Your Projects","class":"form-control"})
        }
