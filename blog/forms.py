from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post, Contact
from django.template.defaultfilters import slugify
   
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'category', 'tags',)
 
    def clean_name(self):
        n = self.cleaned_data['title']
        if n.lower() == "post" or n.lower() == "add" or n.lower() == "update":
            raise ValidationError("Post name can't be '{}'".format(n))
        return n

class ContactForm(forms.ModelForm):
 
    class Meta:
        model = Contact
        fields = '__all__' 