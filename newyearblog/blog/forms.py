from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            })
        }