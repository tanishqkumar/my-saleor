from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256, null=True)
    email = models.EmailField(unique=True, null=True)
    type = models.CharField(max_length=256, null=True)
    bio = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
