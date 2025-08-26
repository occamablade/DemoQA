"""Module with basic configs for the work the framework"""
from dataclasses import dataclass


class Timeouts:
    """
    Class with timeouts
    """
    sec_1 = 1
    sec_5 = 5
    sec_10 = 10


@dataclass
class Person:
    """Class person data"""
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

    first_name: str = None
    last_name: str = None
    age: int = None
    salary: int = None
    department: str = None

    subject: str = None
    phone: str = None


class CodeStatus:
    """A class with response code statuses"""

    codes = {
        'Created': {'code': '201',
                    'text': 'Created'},
        'No Content': {'code': '204',
                       'text': 'No Content'},
        'Moved': {'code': '301',
                  'text': 'Moved Permanently'},
        'Bad Request': {'code': '400',
                        'text': 'Bad Request'},
        'Unauthorized': {'code': '401',
                         'text': 'Unauthorized'},
        'Forbidden': {'code': '403',
                      'text': 'Forbidden'},
        'Not Found': {'code': '404',
                      'text': 'Not Found'},
    }


class Subjects:
    """A class with subject data"""

    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry",
                "Biology", "Computer Science", "Commerce", "Accounting",
                "Economics", "Arts", "Social Studies", "History", "Civics"]


class Genders:
    """A class with gender data"""

    genders = {'1': 'Male',
               '2': 'Female',
               '3': 'Other'}


class Hobbies:
    """A class with hobbies data"""

    hobbies = {'1': 'Sports',
               '2': 'Reading',
               '3': 'Music'}


class Months:
    """A class with month data"""

    months = {'0': 'January',
              '1': 'February',
              '2': 'March',
              '3': 'April',
              '4': 'May',
              '5': 'June',
              '6': 'July',
              '7': 'August',
              '8': 'September',
              '9': 'October',
              '10': 'November',
              '11': 'December'}

class Colors:
    """A class with colors data"""

    colors = ['Aqua', 'Yellow', 'White', 'Red', 'Blue', 'Green',
              'Purple', 'Voilet', 'Magenta', 'Indigo', 'Black']
