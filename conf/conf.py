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
