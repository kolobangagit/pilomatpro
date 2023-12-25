from django import template
from store.models import Locations, Category, SubCategory, Products, City

register = template.Library()

@register.filter
def get_name_location(value):
    try:
        return Locations.objects.get(slug=value)
    except Locations.DoesNotExist:
        return value

@register.filter
def get_name_category(value):
    try:
        return Category.objects.get(slug=value)
    except Category.DoesNotExist:
        return value

@register.filter
def get_city_name(value):
    if value:
        return City.objects.get(slug=value).location.name
    else:
        return ''

@register.filter
def get_location_with_city(value):
    return City.objects.get(slug=value).location.slug

@register.inclusion_tag('location/tags/_product.html', takes_context=True)
def sub_category(context):
    if 'slug' in context:
        slug = context['slug']
    else:
        slug = City.objects.get(slug=context['slug_city']).location.slug
    print(slug)
    return {
        'slug': slug,
        'sub_categories': SubCategory.objects.filter(category__slug=context['slug_category']),
        'slug_category': context['slug_category']
    
    }

@register.inclusion_tag('location/tags/_price.html', takes_context=True)
def price(context, unit_of_measurement, slug_category, item_slug):
    return {
        'unit_of_measurement': unit_of_measurement,
        'name_sub_category': slug_category,
        'products': Products.objects.filter(sub_category__slug=item_slug)
        
    }

@register.inclusion_tag('location/tags/_product_price_short.html', takes_context=True)
def sub_price(context, slug):
    request = context.get('request')
    
    return {
        'request': request,
        'sub_categories': SubCategory.objects.filter(category__slug=slug),
        'slug_category': slug
        
    }
