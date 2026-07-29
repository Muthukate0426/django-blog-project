from django import forms
from .models import Contact, Profile, Post



class ContactForm(forms.ModelForm):

    class Meta:

        model = Contact

        fields = [
            'name',
            'email',
            'message'
        ]


        widgets = {

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your name'
                }
            ),


            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email'
                }
            ),


            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your message',
                    'rows': 5
                }
            ),

        }





class ProfileForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [
            'image'
        ]


        widgets = {

            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }





class PostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = [
            'title',
            'content',
            'image'
        ]


        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter post title'
                }
            ),


            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your post...',
                    'rows': 6
                }
            ),


            'image': forms.FileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

        }