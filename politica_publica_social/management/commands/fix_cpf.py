# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model, models
from django.db import transaction
from politica_publica_social.models import SindsepProfile
import unicodecsv
import random

User = get_user_model()


class Command(BaseCommand):
    args = 'file'
    help = 'import users'

    @transaction.atomic
    def handle(self, *files, **options):
        count = 0
        all_users = User.objects.all()
        for user in all_users:
            try:
                int(user.username)
                cpf_length = len(user.username)
                if cpf_length < 11:
                    for i in range(11-cpf_length):
                        user.username = '0' + user.username
                    user.save()
            except ValueError:
                self.stdout.write(user.username)

                count += 1
                if count % 100 == 0:
                    self.stdout.write(str(count))
