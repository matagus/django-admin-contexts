from django import forms

from django_admin_contexts.models import AdminContext


class AdminContextForm(forms.Form):
    context = forms.ModelChoiceField(
        queryset=AdminContext.objects.all(),
        required=False,
        empty_label="Any",
        widget=forms.Select(attrs={"onchange": "this.form.submit()"}),
    )
