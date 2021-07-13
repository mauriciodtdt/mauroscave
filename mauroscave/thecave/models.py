from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to='images/')
    project_url = models.CharField(max_length=100, null=False, default='/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name
