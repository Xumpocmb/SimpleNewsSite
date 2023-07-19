from .models import news_post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class news_postForm(ModelForm):
    class Meta:
        model = news_post
        fields = ['news_title', 'news_anounsment', 'news_escription', 'news_date']
        widgets = {
            'news_title': TextInput(attrs={
                'class': 'form-control me-2',
                'placeholder': 'article\'s name',
            }),
            'news_anounsment': TextInput(attrs={
                'class': 'form-control me-2',
                'placeholder': 'article\'s anounce',
            }),
            'news_escription': Textarea(attrs={
                'class': 'form-control me-2',
                'placeholder': 'article\'s full text',
                'maxlength': 2500,
            }),
            'news_date': DateTimeInput(attrs={
                'class': 'form-control me-2',
                'placeholder': 'article\'s date',
            }),
        }
