"""Module with generator functions"""
import logging
import random
from pathlib import Path

import allure
from faker import Faker

from conf.conf import Person, Subjects, Colors

RANDOM_FILE = Path(__file__).parent
faker_ru = Faker('ru_RU')
Faker.seed()

logger = logging.getLogger(__name__)


@allure.step('Generate person')
def generate_person():
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

@allure.step('Generate file')
def generate_file():
    """
    Method that generates a file
    :return: filename and path
    """
    path = rf'{RANDOM_FILE}\File{random.randint(0, 1000)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World {random.randint(0, 1000)}')
    file.close()
    file_name = file.name.split('\\')
    file_name = file_name[-1]
    logger.info(f'File generated: {file_name}')
    return file_name, path

@allure.step('Generate subjects')
def generate_subject():
    """
    Method that generates a subject
    :return: list of subjects
    """
    data = []
    count = random.randint(1, len(Subjects.subjects))
    for i in range(count):
        data.append(Subjects.subjects[i])
    return data

@allure.step('Generate random color')
def generate_color(count: int) -> set[str]:
    """
    Method that generates a random color
    :return: random color
    """
    return set(random.choices(Colors.colors, k=count))