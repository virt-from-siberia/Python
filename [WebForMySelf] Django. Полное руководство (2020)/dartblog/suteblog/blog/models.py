from django.db import models

# Create your models here.
'''
    Category
    ========
    title, slug
    
    Tag
    ========
    title, slug
    
    Post
    ========
    title, slug, author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Тег')
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Пост')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Автор')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Фото')
    views = models.IntegerField(default=0, verbose_name='Количесство просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    ordering = ['-created_at']
