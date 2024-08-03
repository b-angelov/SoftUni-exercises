import os
import django
from django.core.exceptions import ValidationError


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Restaurant

# Create queries within functions

if __name__ == '__main__':
    pass
    from main_app.models import Restaurant, RegularRestaurantReview, FoodCriticRestaurantReview
    from django.core.exceptions import ValidationError

    restaurant1 = Restaurant.objects.create(name="Restaurant A", location="123 Main St.",
                                            description="A cozy restaurant", rating=4.88)
    RegularRestaurantReview.objects.create(reviewer_name="Bob", restaurant=restaurant1,
                                           review_content="Good experience overall.", rating=4)
    RegularRestaurantReview.objects.create(reviewer_name="Aleks", restaurant=restaurant1,
                                           review_content="Great food and service!", rating=5)

    duplicate_review = RegularRestaurantReview(reviewer_name="Aleks", restaurant=restaurant1,
                                               review_content="Another great meal!", rating=5)

    try:
        duplicate_review.full_clean()
        duplicate_review.save()
    except ValidationError as e:
        print(f"Validation Error: {e}")

    print("Regular Restaurant Review:")
    print(f"Model Name: {RegularRestaurantReview._meta.verbose_name}")
    print(f"Model Plural Name: {RegularRestaurantReview._meta.verbose_name_plural}")

    print("Food Critic Restaurant Review:")
    print(f"Model Name: {FoodCriticRestaurantReview._meta.verbose_name}")
    print(f"Model Plural Name: {FoodCriticRestaurantReview._meta.verbose_name_plural}")
