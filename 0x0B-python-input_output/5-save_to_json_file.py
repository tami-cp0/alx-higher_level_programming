#!/usr/bin/python3
"""
    5-save_to_json_file: save_to_json_file()
"""


import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w') as json_f:
        json.dump(my_obj, json_f)
