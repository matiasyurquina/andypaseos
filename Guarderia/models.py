from django.db import models
from Usuario.models import Usuario
from Mascota.models import Mascota

class Guarderia(models.Model):
    fecha_guarderia = models.DateField(null=False)
    user = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=False)
    mascota = models.ForeignKey(Mascota, on_delete=models.DO_NOTHING, null=False)

    precio = models.PositiveIntegerField(null=False)
    fecha = models.DateField(auto_now=True)
    cupos = models.PositiveSmallIntegerField(default=6)
    
class Meta:
    ordering = ['fecha_guarderia']
    unique_together = ['user', 'mascota', 'fecha_guarderia']
    constraints = [
            models.UniqueConstraint(fields=['user', 'mascota', 'fecha_guarderia'], name='const_guarderia_together')
    ]

