from django.db import models


class Table(models.Model):
    number = models.IntegerField(unique=True)
    status = models.CharField(max_length=20, choices=[("free", "Свободно"), ("occupied", "Занято")], default="free")

    def __str__(self):
        return f"Стол №{self.number} - {self.status}"
