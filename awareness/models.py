from django.db import models


class Condition(models.Model):

    CATEGORY=[

        ("degenerative","Degenerative"),

        ("neurological","Neurological"),

        ("genetic","Genetic")

    ]

    name=models.CharField(
        max_length=200
    )

    description=models.TextField()

    category=models.CharField(
        max_length=50,
        choices=CATEGORY
    )

    def __str__(self):

        return self.name