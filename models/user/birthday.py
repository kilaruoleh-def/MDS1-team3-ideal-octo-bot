import re


class Birthday:
    def __init__(self, value):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
        if not re.fullmatch(pattern, value):
            raise ValueError("Invalid birthday format!")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        pattern = r"\d{2}\.\d{2}\.\d{4}"
        if not re.fullmatch(pattern, new_value):
            raise ValueError("Invalid birthday format!")
        self._value = new_value

    def __str__(self):
        return self._value
