from django.shortcuts import render
from django.db.models import Q, F
from django.contrib.contenttypes.models import ContentType
from store.models import Collection, OrderItem, Product, Order
from tags.models import TaggedItem
from django.db import transaction


def say_hello(request):
    # ordered_items_unique = OrderItem.objects.values('product_id').distinct()
    # products = Product.objects.filter(id__in=ordered_items_unique).order_by('title')
    # orders = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
    # tags = TaggedItem.objects.get_tags_for(Product, 1)
    # with transaction.atomic():
    #     collection = Collection.objects.get(pk=11)
    #     collection.featured_product = None
    #     collection.save()
    queryset = Product.objects.all()
    return render(request, "hello.html", {"name": "Mosh", "tags": list(queryset)})
