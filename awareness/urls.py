from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "knowledge/",
        views.knowledge_base,
        name="knowledge"
    ),

    path(
        "conditions/",
        views.conditions,
        name="conditions"
    ),

    path(
        "get-involved/",
        views.get_involved,
        name="get_involved"
    ),

]