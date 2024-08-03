import os
import django
from django.db.models import Count, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review


# Create queries within functions

def get_authors(search_name=None, search_email=None):

    if not search_name and not search_email :
        return ""
    elif search_name and not search_email:
        result = Author.objects.filter(full_name__icontains=search_name).order_by('-full_name')
    elif search_email and not search_name:
        result = Author.objects.filter(email__icontains=search_email).order_by('-full_name')
    else:
        result = Author.objects.filter(email__icontains=search_email, full_name__icontains=search_name).order_by('-full_name')

    return '\n'.join(f'Author: {r.full_name}, email: {r.email}, status: {"Banned" if r.is_banned else "Not Banned"}' for r in result)


def get_top_publisher():
    if not len(Article.objects.all()):
        return ""
    author = Author.objects.get_authors_by_article_count().first()
    return f"Top Author: {author.full_name} with {author.articles_count} published articles."

def get_top_reviewer():
    if not len(Review.objects.all()):
        return ""
    best_reviewer = Author.objects.prefetch_related('review_set').annotate(review_count=Count('review')).order_by('-review_count','email').first()
    return f"Top Reviewer: {best_reviewer.full_name} with {best_reviewer.review_count} published reviews."


def get_latest_article():
    article = Article.objects.prefetch_related('review_set').annotate(count_reviews=Count('review'), average_rating=Avg('review__rating',default=0)).order_by('published_on').last()
    return f"The latest article is: {article.title}. Authors: {', '.join(author.full_name for author in article.authors.all().order_by('full_name'))}. Reviewed: {article.count_reviews} times. Average Rating: {article.average_rating:.2f}." if article else ""

def get_top_rated_article():
    article = Article.objects.prefetch_related('review_set').annotate(average_rating=Avg('review__rating',default=0), num_reviews=Count('review')).order_by('-average_rating', 'title').first()
    return f"The top-rated article is: {article.title}, with an average rating of {article.average_rating:.2f}, reviewed {article.num_reviews} times." if article and len(article.review_set.all()) else ""

def ban_author(email=None):
    author = Author.objects.filter(email=email).annotate(num_reviews=Count('review')).first()
    if not author:
        return "No authors banned."
    author.is_banned = True
    author.review_set.all().delete()
    author.save()
    return f"Author: {author.full_name} is banned! {author.num_reviews} reviews deleted."




if __name__ == "__main__":

    # print(Author.objects.get_authors_by_article_count())
    # print(get_authors('a',))
    # print()
    # print(get_top_publisher())
    # print()
    # print(get_top_reviewer())
    print()
    print(get_latest_article())
    print()
    print(get_top_rated_article())
    print()
    print(ban_author('denetor@white-tree.gond'))