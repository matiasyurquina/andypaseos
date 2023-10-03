from django.db import models
from Usuario.models import Usuario
from Mascota.models import Mascota

class Paseo(models.Model):
    fecha_paseo = models.DateField(default='2022-01-01')
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=False)
    mascota = models.ForeignKey(Mascota, on_delete=models.DO_NOTHING, null=False)
    
    precio = models.PositiveIntegerField(null=False)
    fecha = models.DateField(default='2022-01-01')
    cupos = models.PositiveSmallIntegerField(default=6, null=False)

class Meta:
    ordering = ['fecha_paseo']
    unique_together = ['user', 'mascota', 'fecha_paseo']
    constraints = [
            models.UniqueConstraint(fields=['user', 'mascota', 'fecha_paseo'], name='const_unique_together')
    ]
