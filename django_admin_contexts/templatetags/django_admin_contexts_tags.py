from collections import defaultdict

from django import template
from django.urls import reverse

from django_admin_contexts.forms import AdminContextForm


register = template.Library()


@register.simple_tag(takes_context=True)
def get_contexts_form(context):
    request = context["request"]

    # Only show the form on the admin index page
    if request.path == reverse("admin:index"):
        return AdminContextForm(request.GET)

    return None


@register.simple_tag(takes_context=True)
def filter_by_context(context, app_list):
    context_app_dict = defaultdict(list)
    request = context["request"]
    form = AdminContextForm(request.GET)
    if form.is_valid():
        context = form.cleaned_data.get("context")

        if context is None:
            return app_list

        for context_type in context.models.all():
            context_app_dict[context_type.app_label].append(context_type.model)

    filtered_app_list = []

    for app in app_list:
        if app["app_label"] in context_app_dict:
            app_with_filterred_models = {
                "app_label": app["app_label"],
                "app_url": app["app_url"],
                "name": app["name"],
                "has_module_perms": app["has_module_perms"],
                "models": [
                    model
                    for model in app["models"]
                    if model["object_name"].lower() in context_app_dict[app["app_label"]]
                ],
            }
            filtered_app_list.append(app_with_filterred_models)

    return filtered_app_list
