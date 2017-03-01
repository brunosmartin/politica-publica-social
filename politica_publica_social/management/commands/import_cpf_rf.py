# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model, models
from django.db import transaction
from politica_publica_social.models import SindsepProfile
import unicodecsv
import random

User = get_user_model()

collumns = [
    'RF',
    'name',
    'job',
    'cell',
    'email',
]


class Command(BaseCommand):
    args = 'file'
    help = 'import users'

    @transaction.atomic
    def handle(self, *files, **options):

        if not len(files) == 1:
            raise CommandError('No file to import')

        group, _ = models.Group.objects.get_or_create(name="Associados")

        with open(files[0], 'r') as csvfile:
            readf = unicodecsv.DictReader(csvfile)
            count = 0
            for row in readf:
                cpf = row.get('cpf')
                try:
                    user = User.objects.get(username=cpf)
                    profile = SindsepProfile()
                    profile.user = user
                    profile.cpf = cpf
                    profile.rf = row.get('RF')
                    profile.save()
                except:
                    pass
                count += 1
                if count % 100 == 0:
                    self.stdout.write(str(count))
