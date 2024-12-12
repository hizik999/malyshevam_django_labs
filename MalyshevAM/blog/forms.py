from django import forms
from .models import Category


class PostsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название ", widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length=150, label="Url", widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label="Текст", required=False, widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(), label="Категория", 
                                      widget=forms.Select(attrs={'class': 'form-control'}))