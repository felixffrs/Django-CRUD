from django.db import models

# Create your models here.
class BaseModel(models.Model):

    id = models.AutoField(primary_key = True)
    created_at = models.DateField('Created at date', auto_now=False, auto_now_add=True)
    updated_at = models.DateField('Updated at date', auto_now=True, auto_now_add=False)
    deleted_at = models.DateField('Deleted at date', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'