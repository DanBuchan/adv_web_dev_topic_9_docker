from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=256, unique=True, db_index=True)
    image = models.FileField(blank=False)
    thumbnail = models.FileField(null=True)

    def __str__(self):
        return self.name
