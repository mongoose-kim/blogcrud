from django import forms
from .models import Blog

class NewBlog(forms.ModelForm):
    # email = forms.EmailField()
    # files = forms.FileField()
    # url = forms.URLField()
    # words = forms.CharField(max_length=200)
    # max_number = forms.ChoiceField(choices=[('1', 'one'), ('2', 'two')]) #one을 1로 간주 
    
    class Meta:
        model = Blog
        fields = ['title', 'body']