from django import


#//////////////////////////////////


class Authenticator(forms):
    
    
    name_tag = forms.CharField(min_length=6, max_length=15, required=True)
    email = forms.EmailField(required=True)
    password = forms.pass