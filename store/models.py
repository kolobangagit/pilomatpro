from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html



class Locations(models.Model):
	class Meta:
		verbose_name = 'Областной центер'
		verbose_name_plural = 'Областной центер'


	name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Областной центер')
	slug = models.SlugField(max_length=255, null=False, unique=True)
	region = models.CharField(max_length=50, blank=True, null=True)


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Locations, self).save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse("location_detail", kwargs={"slug": self.slug})

	def __str__(self):
		return self.name

class City(models.Model):
	class Meta:
		verbose_name = 'Районные центры'
		verbose_name_plural = 'Районные центры'

	name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Районные центры')
	slug = models.SlugField(max_length=255, null=False, unique=True)
	region = models.CharField(max_length=50, blank=True, null=True)
	location = models.ForeignKey('Locations', on_delete=models.CASCADE, 
	null=True, blank=True)

	def __str__(self):
		return self.name


class Village(models.Model):
	class Meta:
		verbose_name = 'Населенный пункт'
		verbose_name_plural = 'Населенный пункт'

	name = models.CharField(max_length=50, blank=True, null=True, 
	verbose_name='Населенный пункт')
	city = models.ForeignKey('City', on_delete=models.CASCADE, 
	null=True, blank=True)

def __str__(self):
		return self.name

	

class Category(models.Model):

	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='category',blank=True, null=True)
	description = models.CharField(
        max_length=250, default='', blank=True, null=True)
	slug = models.SlugField(max_length=255, null=False, unique=True)

	@staticmethod
	def get_all_categories():
		return Category.objects.all()

	def preview_url(self, width='80'):
		return get_thumbnail(self.image.url.lstrip('/media'), width, crop='center', quality=99)
	
	def preview(self, width='80'):
		url = self.preview_url(width)
		return format_html('<img src="/media/%s" alt="%s" >' % (url, self.image.url,))
	
	preview.allow_tags = True
        

	def __str__(self):
		return self.name

class SubCategory(models.Model):
	name = models.CharField(max_length=60, blank=True, null=True)
	slug = models.SlugField(max_length=255, null=False, unique=True, default='')
	description = models.TextField(blank=True, null=True, verbose_name="Описание подкатегории")
	description_appointment = models.TextField(blank=True, null=True, verbose_name="Назначение подкатегории")
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,
	    null=True)
	unit_of_measurement = models.CharField(max_length=60, blank=True, null=True, verbose_name="Единицы измерения")
	
	def __str__(self):
		return self.name


class Products(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    slug = models.SlugField(max_length=255, null=False, unique=True, default='')
    price = models.FloatField(default=0)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, 
	    blank=True, null=True)
    hickness = models.PositiveSmallIntegerField(default=0, verbose_name="ТОЛЩИНА, ММ")
    height = models.PositiveSmallIntegerField(default=0, verbose_name="ДЛИНА , ММ")
    whidth = models.PositiveSmallIntegerField(default=0, verbose_name="ШИРИНА, М")


    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(sub_category_id):
        if sub_category_id:
            return Products.objects.filter(sub_category=sub_category_id)
        else:
            return Products.get_all_products()


class YandexMetrica(models.Model):
	counter_id = models.PositiveIntegerField(blank=True, null=True, verbose_name='Яндекс Метрика')

	def __str__(self):
		return self.name
