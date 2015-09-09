
from django import forms
from django.db import models
from blog import models as m

class PostModelForm(forms.ModelForm):
    class Meta:
        model = m.Blog
        fields = ['title', 'text', 'author', 'pub_date']