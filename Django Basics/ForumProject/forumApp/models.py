from IPython.core.release import authors
from django.db import models
from django.db.models import Q
from django.utils.text import slugify


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Author(Person):
    pass

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_all_posts(cls, search=None):
        if search:
            return cls.objects.prefetch_related('author').filter(Q(title__icontains=search) | Q(content__icontains=search)).order_by('-created_at','title','content')
        else:
            return cls.objects.prefetch_related('author').all().order_by('-created_at','title','content')

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.prefetch_related('author').filter(id=id).first()

class Articles(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    assigned_to_url = models.ForeignKey('URLs', on_delete=models.CASCADE, related_name='articles', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    @classmethod
    def get_article_for_url(cls, url=''):
        return cls.objects.filter(assigned_to_url__url=url).first()

    def clean(self):
        if not self.assigned_to_url:
            url = slugify(self.title)
            URLs.objects.create(url=url)
            self.url = url
        super().clean()

class URLs(models.Model):
    url = models.TextField(default='', blank=True)

    def clean(self, *args, **kwargs):
        self.url = slugify(self.url)
        super().clean()

    class Meta:
        verbose_name = 'URL'
        verbose_name_plural = 'URLs'

    def __str__(self):
        return self.url

