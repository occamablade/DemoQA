"""Module with generator functions"""

import random

from faker import Faker

from conf.conf import Person

faker_ru = Faker('ru_RU')
Faker.seed()
def generated_person():
    """Method that generates a person"""
    yield Person(
        full_name=faker_ru.first_name() + ' ' + faker_ru.last_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 80),
        salary=random.randint(0, 1000000),
        department=faker_ru.job(),
        subject=faker_ru.job(),
    )
