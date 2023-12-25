from django.shortcuts import render, redirect, HttpResponseRedirect
from django.template.response import TemplateResponse
from store.models import Products, Category, Locations, City, Village, SubCategory
from django.views import View
from django.views.generic import ListView, DetailView


# Create your views here.
class Index(View):
	template='index.html'

	def get(self, request):
		context = {
		'host': request.get_host(),
		'locations': Locations.objects.all()
		}
		template = self.template
		return TemplateResponse(request, template, context)

class LocationDetailVIew(DetailView):
	model = Locations
	template_name = 'location/detail.html'
	slug_url_kwarg = 'slug'
	query_pk_and_slug = True
	host = None
	slug = None

	def dispatch(self, request, *args, **kwargs):
		self.host = request.get_host()
		self.slug = kwargs["slug"]
		return super(LocationDetailVIew, self).dispatch(request, *args, **kwargs)
	
	def func_chunk(self, lst, n):
		for x in range(0, len(lst), n):
			e_c = lst[x : n + x]
			if len(e_c)<n:
				e_c = e_c + [None for y in range(n-len(e_c))]
			yield e_c
	
	def get_context_data(self, **kwargs):
		context = super(LocationDetailVIew,self).get_context_data(**kwargs)
		context["name"] = kwargs['object'].name 
		context['host'] = self.host
		context['slug'] = self.slug
		context['location'] = self.get_queryset()
		context['cities'] = City.objects.filter(location__slug=self.slug)
		context["categories"] = list(self.func_chunk(Category.objects.all(), 3))
		return context


class CityDetailView(DetailView):
	model = City
	template_name = 'location/detail.html'
	slug_url_kwarg = 'slug_city'
	query_pk_and_slug = True
	slug_city = None
	slug = None

	def dispatch(self, request, *args, **kwargs):
		print(kwargs)
		self.slug = kwargs["slug"]
		self.slug_city = kwargs["slug_city"]
		return super(CityDetailView, self).dispatch(request, *args, **kwargs)
	
	def func_chunk(self, lst, n):
		for x in range(0, len(lst), n):
			e_c = lst[x : n + x]
			if len(e_c)<n:
				e_c = e_c + [None for y in range(n-len(e_c))]
			yield e_c
	
	def get_context_data(self, **kwargs):
		context = super(CityDetailView,self).get_context_data(**kwargs)
		context["name"] = kwargs['object'].name
		context['slug'] = self.slug
		context['slug_city'] = self.slug_city
		context['location'] = self.get_queryset()
		context['cities'] = Village.objects.filter(city__slug=self.slug_city)
		context["categories"] = list(self.func_chunk(Category.objects.all(), 3))
		return context
	


def store(request):
	products = None
	categories = Category.get_all_categories()
	categoryID = request.GET.get('category')
	if categoryID:
		products = Products.get_all_products_by_categoryid(categoryID)
	else:
		products = Products.get_all_products()

	data = {}
	data['products'] = products
	data['categories'] = categories
	return render(request, 'index.html', data)


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'location/detail_product.html'
	slug_url_kwarg = 'slug_category'
	query_pk_and_slug = True
	slug_category = None
	slug_city = None
	slug = None

	def dispatch(self, request, *args, **kwargs):
		print(kwargs)
		try:
			self.slug_city = kwargs['slug_city']
		except KeyError:
			self.slug_city = None
		try:
			self.slug = kwargs["slug"]
		except KeyError:
			self.slug = None
		self.slug_category = kwargs["slug_category"]
		return super(CategoryDetailView, self).dispatch(request, *args, **kwargs)

	
	def get_context_data(self, **kwargs):
		context = super(CategoryDetailView,self).get_context_data(**kwargs)
		if self.slug is not None:
			context['slug'] = self.slug
		if self.slug_city is not None:
			context['slug_city'] = self.slug_city
		context['slug_category'] = self.slug_category
		context['category'] = self.get_queryset()
		print(context)
		return context


class LocationAllPrice(DetailView):
	model = Locations
	template_name = 'location/detail_price.html'
	slug_url_kwarg = 'slug'
	query_pk_and_slug = True
	slug = None

	def dispatch(self, request, *args, **kwargs):
		self.slug = kwargs["slug"]
		return super(LocationAllPrice, self).dispatch(request, *args, **kwargs)

	
	def get_context_data(self, **kwargs):
		context = super(LocationAllPrice, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.filter()
		context['slug'] = self.slug
		return context
	