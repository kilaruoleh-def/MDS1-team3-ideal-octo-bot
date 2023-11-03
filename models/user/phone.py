class Phone:
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Invalid phone number format!")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not (len(new_value) == 10 and new_value.isdigit()):
            raise ValueError("Invalid phone number format!")
        self._value = new_value

    def __str__(self):
        return self._value
