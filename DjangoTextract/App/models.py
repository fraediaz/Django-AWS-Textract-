from django.db import models

# Create your models here.
class Consulta(models.Model):
    img         = models.ImageField('', upload_to='busquedas')
    txt         = models.TextField('Texto', blank=True, null=True)
    def __str__(self):
        return str(self.img)
