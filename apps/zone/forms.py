from django import forms

from .models import Zone, Country, State


class ZoneForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = Zone
        fields = "__all__"


class CountryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zone'].widget.attrs.update(
            {'placeholder': 'zone', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})
        self.fields['code'].widget.attrs.update(
            {'placeholder': 'code', 'class': 'form-control'})
        self.fields['state'].widget.attrs.update(
            {'placeholder': 'state', 'class': 'form-control'})
        self.fields['iso_code'].widget.attrs.update(
            {'placeholder': 'iso_code', 'class': 'form-control'})

    class Meta:
        model = Country
        fields = "__all__"


class StateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zone'].widget.attrs.update(
            {'placeholder': 'zone', 'required': True,
             'class': 'form-control'})
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Name', 'required': True,
             'class': 'form-control'})

        zone_id = self.data.get("zone", None)

        if self.instance.id:
            self.fields['country'].queryset = Country.objects.filter(zone=self.instance.zone)
        else:
            self.fields['country'] = forms.ChoiceField(choices=(('', '----------'),))
            if zone_id:
                self.fields['country'] = forms.ModelChoiceField(
                    queryset=Country.objects.filter(zone=zone_id))

        self.fields['country'].widget.attrs.update(
            {'placeholder': 'country', 'required': True,
             'class': 'form-control'})

    class Meta:
        model = State
        fields = "__all__"
