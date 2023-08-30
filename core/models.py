from django.db import models

class Management(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    description = models.TextField()
    photo = models.ImageField( null=True, blank=True)

    def __str__(self):
        return self.name