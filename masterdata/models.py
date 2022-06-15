from operator import mod
from django.db import models

# Create your models here.
class BaseContent(models.Model):

    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    modified        = models.DateTimeField(auto_now=True)
    listing_order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract    = True


class Category(BaseContent):
    title = models.CharField(max_length=150)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        unique_together = ('parent', 'title')
