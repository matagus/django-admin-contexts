from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from django_admin_contexts.models import AdminContext


@admin.register(AdminContext)
class AdminContextAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "description", "created_at", "updated_at"]
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        verbose_name = _("Admin Context")
        verbose_name_plural = _("Admin Contexts")
