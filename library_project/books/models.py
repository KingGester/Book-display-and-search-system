from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='نام ژانر')
    description = models.TextField(blank=True, verbose_name='توضیحات')

    class Meta:
        verbose_name = 'ژانر'
        verbose_name_plural = 'ژانرها'
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان کتاب')
    author = models.CharField(max_length=100, verbose_name='نویسنده')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, verbose_name='ژانر')
    description = models.TextField(verbose_name='توضیحات')
    published_date = models.DateField(verbose_name='تاریخ چاپ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب‌ها'
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['author']),
            models.Index(fields=['genre']),
            models.Index(fields=['published_date']),
        ]

    def __str__(self):
        return self.title
