#!/usr/bin/python3
"""
A class that defines a student
"""


class Student:
    """
    a public instance attribute containing first_name, last_name and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """
    a public instance attribute that retrieves
    a dictionary representation of a Student instance
    """
    def to_json(self, attrs=None):
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
        """
        Public method def reload_from_json(self, json):
        that replaces all attributes of the Student instance
        """
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values from the JSON dictionary.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
