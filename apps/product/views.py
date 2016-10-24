from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from core.mixins import AuthListView, AuthUpdateView, AuthDeleteView, AuthCreateView
from .forms import (
    ProductCategoryForm, ProductSubCategoryForm, ProductForm, ProductDetailForm
)
from .models import (ProductCategory, ProductSubCategory, Product, ProductDetail)

"""
    ProductCategory
"""


class ProductCategoryList(AuthListView):
    template_name = 'dashboard/pages/product/productcategory/productcategory_list.html'
    model = ProductCategory
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Product Category")
        return context


class ProductCategoryCreation(AuthCreateView):
    template_name = 'dashboard/pages/product/productcategory/productcategory_form.html'
    model = ProductCategory
    success_url = reverse_lazy('Category:list')
    form_class = ProductCategoryForm


class ProductCategoryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/product/productcategory/productcategory_form.html'
    model = ProductCategory
    success_url = reverse_lazy('Category:list')
    form_class = ProductCategoryForm


class ProductCategoryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/product/productcategory/productcategory_confirm_delete.html'
    model = ProductCategory
    success_url = reverse_lazy('Category:list')


"""
    ProductSubCategory
"""


class ProductSubCategoryList(AuthListView):
    template_name = 'dashboard/pages/product/productsubcategory/productsubcategory_list.html'
    model = ProductSubCategory
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Product Subcategory")
        return context


class ProductSubCategoryCreation(AuthCreateView):
    template_name = 'dashboard/pages/product/productsubcategory/productsubcategory_form.html'
    model = ProductSubCategory
    success_url = reverse_lazy('Subcategory:list')
    form_class = ProductSubCategoryForm


class ProductSubCategoryUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/product/productsubcategory/productsubcategory_form.html'
    model = ProductSubCategory
    success_url = reverse_lazy('Subcategory:list')
    form_class = ProductSubCategoryForm


class ProductSubCategoryDelete(AuthDeleteView):
    template_name = 'dashboard/pages/product/productcategory/productcategory_confirm_delete.html'
    model = ProductSubCategory
    success_url = reverse_lazy('Subcategory:list')


"""
    Product
"""


class ProductList(AuthListView):
    template_name = 'dashboard/pages/product/product/product_list.html'
    model = Product
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["text_central"] = _("list Product")
        return context


class ProductCreation(AuthCreateView):
    template_name = 'dashboard/pages/product/product/product_form.html'
    model = Product
    success_url = reverse_lazy('Product:list')
    form_class = ProductForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        self.product_detail_form = ProductDetailForm()
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        product_detail_form = ProductDetailForm(request.POST, request.FILES)
        if form.is_valid() and product_detail_form.is_valid():
            return self.form_valid(form, product_detail_form)
        else:
            return self.form_invalid(form, product_detail_form)

    def form_valid(self, form, product_detail_form):
        self.object = form.save()
        product_detail_form.save(product=self.object, commit=False)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, product_detail_form):
        self.form = form
        self.product_detail_form = ProductDetailForm
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_detail"] = self.product_detail_form
        return context


class ProductUpdate(AuthUpdateView):
    template_name = 'dashboard/pages/product/product/product_form.html'
    model = Product
    success_url = reverse_lazy('Product:list')
    form_class = ProductForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)
        product_detail = ProductDetail.objects.get(product=self.object)
        self.product_detail_form = ProductDetailForm(instance=product_detail)
        return super().render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        product_detail = ProductDetail.objects.get(product=self.object)
        product_detail_form = ProductDetailForm(request.POST, instance=product_detail)
        if form.is_valid() and product_detail_form.is_valid():
            return self.form_valid(form, product_detail_form)
        else:
            return self.form_invalid(form, product_detail_form)

    def form_valid(self, form, product_detail_form):
        self.object = form.save()
        product_detail_form.save(product=self.object, commit=False)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, product_detail_form):
        self.form = form
        self.product_detail_form = ProductDetailForm
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form
        context["form_detail"] = self.product_detail_form
        return context


class ProductDelete(AuthDeleteView):
    template_name = 'dashboard/pages/product/product/product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('Product:list')
