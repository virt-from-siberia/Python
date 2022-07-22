from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    # auto_now_add = True Записывается только один раз
    created_at = models.DateTimeField(auto_now_add=True)
    # auto_now = True обновления поля при каждой записи в бд
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
