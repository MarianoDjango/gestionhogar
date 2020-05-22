from django.db import models
from django.utils import timezone

# Create your models here.
class Movimiento(models.Model):
    ENTRADA ='E'
    SALIDA='S'
    OPCS_TIPO_MOV=[
        (ENTRADA, 'Entrada Dinero'),
        (SALIDA, 'Salida Dinero')
    ]
    tipo_mov = models.CharField(
        max_length=1,
        choices=OPCS_TIPO_MOV,
        default=SALIDA,)
    fechareg_mov=models.DateTimeField(
            blank=True, null=True)
    fecha_mov=models.DateTimeField(
            blank=True, null=True)
    importe_mov=models.FloatField()
    descri_mov=models.CharField(
        max_length=50)


    def publish(self):
        self.fechareg_mov = timezone.now()
        self.save()

    def __str__(self):
        return self.descri_mov
