class Address:
    def __init__(self, value):
        if not value:
            raise ValueError("Address is a required field and cannot be empty.")
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not new_value:
            raise ValueError("Address cannot be empty.")
        self._value = new_value

    def __str__(self):
        return self._value
