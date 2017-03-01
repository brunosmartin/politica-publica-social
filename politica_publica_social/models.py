# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class SindsepProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=11, blank=True, null=True, unique=True)
    rf = models.CharField('Registro Funcional', max_length=32, blank=True, null=True, unique=True)
