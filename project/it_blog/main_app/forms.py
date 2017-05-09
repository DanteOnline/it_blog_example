from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}))
    subtitle = forms.CharField(label='Подзаголовок',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Подзаголовок'}))
    text = forms.CharField(label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст (поддерживается html)'}))

    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'text', 'is_active')
