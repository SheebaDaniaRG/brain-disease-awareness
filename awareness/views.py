from django.shortcuts import render
from django.db.models import Q

from .models import Condition


def home(request):

    return render(
        request,
        "awareness/home.html"
    )


def conditions(request):

    diseases = Condition.objects.all()

    return render(

        request,

        "awareness/conditions.html",

        {

            "diseases": diseases

        }

    )


def knowledge_base(request):

    q = request.GET.get("q")

    diseases = Condition.objects.all()

    if q:

        diseases = diseases.filter(

            Q(name__icontains=q)

        )

    return render(

        request,

        "awareness/knowledge.html",

        {

            "diseases": diseases

        }

    )


def get_involved(request):

    return render(

        request,

        "awareness/get_involved.html"

    )