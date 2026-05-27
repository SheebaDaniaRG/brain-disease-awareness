from django.contrib import admin

from .models import Condition


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):

    list_display = (

        "name",

        "category"

    )

    search_fields = (

        "name",

    )