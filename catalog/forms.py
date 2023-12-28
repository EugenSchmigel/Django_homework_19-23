from django import forms

from catalog.models import Product, Version


class StyleFormMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description', 'price', 'category',)
        # exclude = ('',)

    def not_allowed_words(self):
        not_allow_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        return not_allow_words

    def clean_name(self):
        not_allow_words = self.not_allowed_words()
        cleaned_data = self.cleaned_data['name']
        for word in not_allow_words:
            if word.lower() in cleaned_data:
                raise forms.ValidationError('not valid name. not allow words.')
        return cleaned_data

    def clean_description(self):
        not_allow_words = self.not_allowed_words()
        cleaned_data = self.cleaned_data['description']
        for word in not_allow_words:
            if word.lower() in cleaned_data:
                raise forms.ValidationError('not valid description. not allow words')
        return cleaned_data


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category')


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
