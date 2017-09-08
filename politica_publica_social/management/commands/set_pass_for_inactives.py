# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model, models
from django.db import transaction
from django.db.utils import IntegrityError

import unicodecsv
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Activate all inactive users and set their passwords to match usernames'

    @transaction.atomic
    def handle(self, *args, **options):

        if len(args) > 0:
            raise CommandError('No parameters must be included here')

        inactives = User.objects.filter(is_active=False)
        for user in inactives:
            user.set_password(user.username)
            user.is_active = True
            user.save()
            print(user.username)
        