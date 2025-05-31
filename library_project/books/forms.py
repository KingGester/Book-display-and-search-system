from django import forms
from .models import Book, Genre

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'title': 'عنوان کتاب',
            'author': 'نویسنده',
            'genre': 'ژانر',
            'description': 'توضیحات',
            'published_date': 'تاریخ چاپ',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان کتاب را وارد کنید'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام نویسنده را وارد کنید'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات کتاب را وارد کنید', 'rows': 4}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        error_messages = {
            'title': {
                'required': 'لطفا عنوان کتاب را وارد کنید',
                'max_length': 'عنوان کتاب نمی‌تواند بیشتر از ۲۰۰ کاراکتر باشد',
            },
            'author': {
                'required': 'لطفا نام نویسنده را وارد کنید',
                'max_length': 'نام نویسنده نمی‌تواند بیشتر از ۱۰۰ کاراکتر باشد',
            },
            'genre': {
                'required': 'لطفا ژانر کتاب را وارد کنید',
                'max_length': 'ژانر کتاب نمی‌تواند بیشتر از ۱۰۰ کاراکتر باشد',
            },
            'description': {
                'required': 'لطفا توضیحات کتاب را وارد کنید',
            },
            'published_date': {
                'required': 'لطفا تاریخ چاپ را وارد کنید',
            },
        }
