from django.db import models
from .base import BaseModel

class Author(BaseModel):
    name = models.TextField(blank=False, null = False)
    birth_date = models.DateField(blank=False, null = False)
    biography = models.TextField(blank=False, null = False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'authors'
        verbose_name = "Author"
        verbose_name_plural = "Authors"

