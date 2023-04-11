from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
  
class RegisterUserForm(UserCreationForm):  

    email = forms.EmailField(max_length=255)  

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
  
    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        try :
            user = User.objects.get(username = username)  
        except Exception as e:
            return username  
        raise forms.ValidationError(f"User {username} is already in use.")   
  
    def clean_email(self):  
        email = self.cleaned_data['email'].lower()  
        try :
            user = User.objects.get(email = email)  
        except Exception as e:
            return email  
        raise forms.ValidationError(f"{email} is already taken.")  
  
    # def clean_password2(self):  
    #     password1 = self.cleaned_data['password1']  
    #     password2 = self.cleaned_data['password2']  
  
    #     if password1 and password2 and password1 != password2:  
    #         raise ValidationError("Password don't match")  
    #     return password2  
  
    # def save(self, commit = True):  
    #     user = User.objects.create_user(  
    #         self.cleaned_data['username'],  
    #         self.cleaned_data['email'],  
    #         self.cleaned_data['password1']  
    #     )  
    #     return user 