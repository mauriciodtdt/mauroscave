from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    image = models.ImageField(upload_to='images/')
    project_url = models.CharField(max_length=100, null=False, default='/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    file = models.FileField(upload_to='files/')
    external_link = models.URLField(null=True, blank=True)
    summary = models.CharField(max_length=300)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_location(self):
        if not self.external_link:
            return self.file.url
        return self.external_link