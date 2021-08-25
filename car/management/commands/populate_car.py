from django.core.management.base import BaseCommand, CommandError
from car.models import Car

import random

import factory  
import factory.django

class CarFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = Car

    name = factory.Faker('name')
    description = factory.Faker('address')
    color = factory.Faker('phone_number')
    type=random.randint(1,2)

class Command(BaseCommand):

    def handle(self, *args, **options):
        # for i in range(2,100):
        #     Car.objects.create(
        #         name=factory.Faker('first_name'),
        #         description=factory.Faker('company'),
        #         color=factory.Faker('job'),
        #         type=random.randint(1,2)
        #     )

        for i in range(2,100):
            CarFactory.create()