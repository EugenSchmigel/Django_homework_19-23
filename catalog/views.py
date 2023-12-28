from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView, UpdateView, CreateView, DetailView

from catalog.forms import ProductForm, VersionForm, MProductForm
from catalog.models import Product, Category, Version


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'Shop'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:3]

        return context_data


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Product - category'}


class CategoryCatalogListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk
        context_data['title'] = f'Category {category_item.name}'

        return context_data


class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Products'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductDetailView(DetailView):
    model = Product

    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['version'] = Version.objects.filter(product=self.kwargs['pk'])
        return context


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    permission_required = ['catalog.set_is_published', 'catalog.set_description', 'catalog.set_category']
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        if form.is_valid:
            new_product = form.save()
            new_product.user = self.request.user
            new_product.save()

        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (self.request.user != self.object.user and not self.request.user.is_staff
                and not self.request.user.is_superuser and self.request.user.has_perm('catalog.product_published')):
            raise Http404
        return self.object

    def get_form_class(self):
        if self.request.user.has_perm('catalog.product_published'):
            return MProductForm
        return ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class VersionListView(ListView):
    model = Version

