# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model, models
from django.db import transaction
from django.db.utils import IntegrityError
from politica_publica_social.models import SindsepProfile
from core.models import Course, Class

import unicodecsv
import random

User = get_user_model()


#
# Expected columns in the CSV file: 'RF', 'cpf', 'name', 'occupation', 'email'
# The class to be targeted is expected as a command line parameter
#
class Command(BaseCommand):
    args = 'file'
    help = 'import users to a group and class'

    @transaction.atomic
    def handle(self, *args, **options):

        if not len(args) == 2:
            raise CommandError('Incorrect parameters')

        print('Preparing to import data for "Curso Reflexões - 5"')
        group, _ = models.Group.objects.get_or_create(name="Curso Reflexões - 5")
        students = models.Group.objects.get(name="students")

        course = Course.objects.get(id=4)  # Reflexões sobre desenvolvimento infantil (second version)
        classs, _ = Class.objects.get_or_create(name=args[1], course=course)

        with open(args[0], 'r') as csvfile:
            readf = unicodecsv.DictReader(csvfile)
            count = 0
            for row in readf:
                email = row.get('email')
                cpf = row.get('cpf')
                cpf_length = len(cpf)
                if cpf_length < 11:
                    for i in range(11-cpf_length):
                        cpf = '0' + cpf

                try:
                    with transaction.atomic():
                        user = User.objects.create(username=cpf, email=email)
                    profile = SindsepProfile()
                    user.is_active = False
                    print('created ' + user.username)
                except IntegrityError as e:
                    user = User.objects.get(username=cpf)
                    profile = SindsepProfile.objects.get(user=user)
                    print('found ' + user.username)

                user.first_name, user.last_name = row.get('name').split(' ', 1 )
                user.rg = row.get('RF')
                if user.first_name:
                    user.first_name = user.first_name.title()
                if user.last_name:
                    user.last_name = user.last_name.title()
                if row.has_key('email') and row.get('email'):
                    user.email = row.get('email')
                else:
                    user.email = str(random.randint(1,100000000)) + '@nomail.com'

                if row.has_key('occupation'):
                    user.occupation = row.get('occupation')

                user.save()

                profile.user = user
                profile.cpf = cpf
                profile.rf = row.get('RF')
                profile.save()

                classs.students.add(user)
                group.user_set.add(user)
                students.user_set.add(user)

                count += 1
                if count % 10 == 0:
                    self.stdout.write(str(count))
