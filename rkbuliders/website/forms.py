from django import forms
from website.models import Query


class QueryForm(forms.ModelForm):
    """
        Model form for Query model
    """
    class Meta:
        model = Query
        fields =('name', 'email', 'message')
        widgets = {'message': forms.Textarea(attrs={'rows': 4})}