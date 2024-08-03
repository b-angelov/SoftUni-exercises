import os
import django
from django.db.models import Q, Count, F, When, Case, Value

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import Profile, Order, Product


# Create queries within functions

def get_profiles(search_string=None):
    if search_string is None: return ""
    profiles = Profile.objects.filter(Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(phone_number__icontains=search_string)).annotate(orders_count=Count('order')).order_by('full_name')
    return '\n'.join(f'Profile: {p.full_name}, email: {p.email}, phone number: {p.phone_number}, orders: {p.orders_count}' for p in profiles) if len(profiles) else ""

def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()
    return '\n'.join(f'Profile: {p.full_name}, orders: {p.order_count}' for p in profiles) if len(profiles) else ""

def get_last_sold_products():
    order = Order.objects.prefetch_related('products').last()
    return f"Last sold products: {', '.join(p.name for p in order.products.all().order_by('name'))}" if order else ""


def get_top_products():
    recent_products = Product.objects.annotate(sales_count=Count('order')).filter(sales_count__gt=0).order_by('-sales_count','name')[:5]
    result = "Top products:\n" +"\n".join(f"{p.name}, sold {p.sales_count} times" for p in recent_products)
    return result if Order.objects.count() else ""


def apply_discounts():
    orders_to_discount = Order.objects.annotate(product_count=Count('products')).filter(product_count__gt=2, is_completed=False).update(total_price=F('total_price') * 0.90)
    return f"Discount applied to {orders_to_discount} orders."


def complete_order():
    order = Order.objects.filter(is_completed=False).order_by('creation_date').first()
    if not order:
        return ""
    order.products.update(
        in_stock=F('in_stock') - 1,
        is_available=Case(
            When(in_stock__gt=1, then=Value(True)),
            default=False
        )
    )

    order.is_completed = True
    order.save()
    return "Order has been completed!"




if __name__ == "__main__":
    # print(Profile.objects.get_regular_customers())
    # print(get_profiles('the'))
    # print(get_loyal_profiles())
    # print(get_last_sold_products())
    # print(get_top_products())
    # print(apply_discounts())
    print(complete_order())