from django import forms
from wiki.models import Page


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Page
        # exclude = ('modified', 'created')
        fields = "__all__"
        