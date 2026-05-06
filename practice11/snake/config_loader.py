import json
import os

_DIR = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(_DIR, "settings.json")


def load_settings():
    with open(FILE, "r") as f:
        return json.load(f)


def save_settings(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)