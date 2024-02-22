from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    title = forms.CharField(min_length=10)

    class Meta:
        model = Post
        fields = '__all__'
        # fields = [
        #     'author'
        #     'date_create'
        #     'post_category',
        #     'title',
        #     'text',
        #     'rating',
        # ]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError("Описание не должно быть идентично названию.")

        return cleaned_data

    def clean_name(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError("Название должно начинаться с заглавной буквы")

        return title
