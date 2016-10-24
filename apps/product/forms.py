from django import forms

from core.models import ProductModel
from core.utils.clearable_fileinput import CustomClearableFileInput
from .models import (
    ProductCategory, ProductSubCategory, Product,
    ProductDetail
)


class ProductCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductSubCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_category'].widget.attrs.update(
            {'placeholder': 'Product Category', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = ProductSubCategory
        fields = "__all__"


class ProductForm(forms.ModelForm):
    logo_product = forms.ImageField(widget=CustomClearableFileInput, required=False)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['product_category'].widget.attrs.update(
            {'placeholder': 'Product Category', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['brand'].widget.attrs.update(
            {'placeholder': 'Brand', 'required': True,
             'class': 'form-control'})
        self.fields['unit'].widget.attrs.update(
            {'placeholder': 'Unit', 'required': True,
             'class': 'form-control'})
        self.fields['sale_price'].widget.attrs.update(
            {'placeholder': 'Sale Price', 'required': True,
             'class': 'form-control'})
        self.fields['purchase_price'].widget.attrs.update(
            {'placeholder': 'Purchase Price', 'required': True,
             'class': 'form-control'})
        self.fields['logo_product'].widget.attrs.update(
            {'placeholder': 'Picture', 'class': 'file-styled'})

        category_id = self.data.get("product_category", None)
        brand_id = self.data.get("brand", None)

        if self.instance.id:
            self.fields['product_subcategory'].queryset = ProductSubCategory.objects.filter(
                product_category=self.instance.product_category)
            self.fields['model'].queryset = ProductModel.objects.filter(
                brand=self.instance.brand)
        else:
            self.fields['product_subcategory'] = forms.ChoiceField(choices=(('', '----------'),))
            self.fields['model'] = forms.ChoiceField(choices=(('', '----------'),))
            if category_id:
                self.fields['product_subcategory'] = forms.ModelChoiceField(
                    queryset=ProductSubCategory.objects.filter(product_category=category_id))
            if brand_id:
                self.fields['model'] = forms.ModelChoiceField(
                    queryset=ProductModel.objects.filter(brand=brand_id))

        self.fields['product_subcategory'].widget.attrs.update(
            {'placeholder': 'Product Subcategory', 'required': True,
             'class': 'form-control'})
        self.fields['model'].widget.attrs.update(
            {'placeholder': 'Model', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['series'].widget.attrs.update(
            {'placeholder': 'series', 'class': 'form-control'})
        self.fields['origin'].widget.attrs.update(
            {'placeholder': 'origin', 'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'description', 'class': 'form-control',
             'rows': "5"})

    class Meta:
        model = ProductDetail
        fields = ["series", "origin", "description"]

    def save(self, product=None, commit=True):
        product_detail = super().save(commit=False)
        if product:
            product_detail.product = product
        product_detail.save()
        return product_detail
