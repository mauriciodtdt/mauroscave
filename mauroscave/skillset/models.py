from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='files/')
    summary = models.CharField(max_length=300)

    def __str__(self):
        return self.name
