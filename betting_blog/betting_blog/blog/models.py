from django.db import models

#ads associated  with this article
class affiliate(models.Model):
    name = models.CharField('Product Name', max_length=120)
    description = models.TextField(blank=True)
    url = models.URLField()

    def __str__(self):
        return self.name

class articles(models.Model):
    name = models.CharField('Article Name', max_length=120)
    url = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class promotions(models.Model):
    name = models.CharField('promotion', max_length=120)
    description = models.CharField('promotion description', max_length=250)
    url = models.CharField(max_length=120)
