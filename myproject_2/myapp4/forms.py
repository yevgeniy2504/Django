# Создание формы добавления изображения

from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']
        labels = {'title': 'Название', 'image': 'Изображение'}
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'})}


