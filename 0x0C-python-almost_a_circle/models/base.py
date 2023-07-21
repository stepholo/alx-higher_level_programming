#!/usr/bin/python3
"""Module to define class Base
"""


import json
import csv
import os


class Base:
    """Parent class to manage id attribute in all classes"""

    __nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns json string representation
        of list_dictionaries
        Parameter:
             list_dictionaries: list of dictionary
        Return:
            json string representation
        """
        new_list = "[]"
        if list_dictionaries is None:
            return new_list
        elif list_dictionaries == []:
            return new_list
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """method that returns list of the json string repr
        Parameter:
             json_string: json string
        Return:
            list of json repr
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    def __init__(self, id=None):
        """Class constructor
        Parameter:
            id: class attribute that returns object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method the saves json string into a file"""
        filename = cls.__name__ + '.json'
        if list_objs is None:
            json_str = '[]'
        else:
            new_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(new_list)
        with open(filename, 'w') as f:
            f.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attibutes
        already set
        """
        dummy = cls(1, 2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """method that returns a list of instances"""
        obj_list = []
        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                char = f.read()
            if char:
                instance = cls.from_json_string(char)
                for obj in instance:
                    obj_list.append(cls.create(**obj))
                    return obj_list
        else:
            return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that saves the attributes of an instance in csv"""
        filename = cls.__name__ + '.csv'
        if list_objs is None:
            csv_dicti = []
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_dicti)
        else:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """class method that loads from a csv file"""
        obj_list = []
        filename = cls.__name__+'.csv'
        if os.path.exists(filename):
            with open(filename, 'r') as csv_file:
                char = csv.reader(csv_file)
                for obj in char:
                    obj_list.append(cls.create_from_csv_row(obj))
                return obj_list
        else:
            return obj_list
