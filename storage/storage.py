import json

from models.note.note import Note
from models.user.user import User


class Storage:

    @staticmethod
    def save_to_file(data, filename="address_book.json"):
        serializable_data = {str(i): user.to_dict() for i, user in enumerate(data)}
        with open(filename, 'w') as file:
            json.dump(serializable_data, file)

    @staticmethod
    def load_from_file(filename="address_book.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [User.from_dict(record_data) for record_data in data.values()]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_to_file_note(data, filename="notes.json"):
        serializable_data = {str(i): note.to_dict() for i, note in enumerate(data)}
        with open(filename, 'w') as file:
            json.dump(serializable_data, file)

    @staticmethod
    def load_from_file_note(filename="notes.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Note.from_dict(record_data) for record_data in data.values()]
        except FileNotFoundError:
            return []
