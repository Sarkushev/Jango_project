from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок поста',
                'autofocus': True
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите содержимое вашего поста...',
                'rows': 8
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'published_date': forms.DateInput(attrs={  # ИЗМЕНЕНО: DateInput вместо DateTimeInput
                'class': 'form-control',
                'type': 'date'  # ИЗМЕНЕНО: type="date" вместо type="datetime-local"
            }),
        }
        labels = {
            'title': 'Заголовок поста',
            'content': 'Содержимое',
            'category': 'Категория',
            'published_date': 'Дата публикации',
        }