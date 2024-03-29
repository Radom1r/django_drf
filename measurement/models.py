from django.db import models


class Sensor(models.Model):
    """Объект на котором проводят измерения."""

    name = models.CharField(max_length=50)
    description = models.TextField()
    
class Measurement(models.Model):
    """Измерение температуры на объекте."""

    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    created_at = models.DateTimeField(
        auto_now_add=True
    )