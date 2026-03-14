import json
import os

DATA_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []

def save_expenses(expenses):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")
