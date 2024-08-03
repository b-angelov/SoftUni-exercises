from django.db import models
from django.db.models import Count


class AuthorManager(models.Manager):

    def get_authors_by_article_count(self):
        return self.prefetch_related('article_set__authors').annotate(articles_count=Count('article')).all().order_by('-articles_count', 'email')