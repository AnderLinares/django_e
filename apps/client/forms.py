from django import forms

from .models import Person


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name', 'required': True,
             'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update(
            {'placeholder': 'Email', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update(
            {'placeholder': 'Address', 'class': 'form-control'})
        self.fields['home_phone'].widget.attrs.update(
            {'placeholder': 'Home Phone', 'class': 'form-control'})
        self.fields['mobile_phone'].widget.attrs.update(
            {'placeholder': 'Mobile Phone', 'class': 'form-control'})
        self.fields['document_type'].widget.attrs.update(
            {'placeholder': 'Document Type', 'class': 'form-control'})
        self.fields['document_number'].widget.attrs.update(
            {'placeholder': 'Document Number', 'class': 'form-control'})
        self.fields['person_type'].widget.attrs.update(
            {'placeholder': 'Person Type', 'class': 'form-control'})

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'address',
                  'home_phone', 'mobile_phone', 'document_type',
                  'document_number', 'person_type']
