

''' This module reads the data in the json file and returns the data '''

import json
import os

DATA_FILE = 'data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}
    return data

def read_user(user_id):
    data = load_data()
    return data.get(user_id)

def read_all():
    return load_data()
