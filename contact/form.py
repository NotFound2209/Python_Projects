from django import forms



class Contact_form(forms.Form):
    
    subject = forms.CharField(label='Subject', max_length=25, required=True)
    email = forms.EmailField(label='Email', required=True)
    message = forms.CharField(label='Message', max_length=800, required=True, widget=forms.Textarea)