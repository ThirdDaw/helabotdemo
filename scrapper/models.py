from django.db import models


# Create your models here.
class SAPUser(models.Model):
    login = models.CharField("Login", max_length=50)
    password = models.CharField("Password", max_length=50)
    ip = models.CharField("IP", max_length=20)
    instance_number = models.PositiveIntegerField("Instance Number")

    def __str__(self):
        return self.login + " " + str(self.instance_number)

    class Meta:
        verbose_name = "SAPUser"
        verbose_name_plural = "SAPUsers"
