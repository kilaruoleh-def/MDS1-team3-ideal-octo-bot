from models.field import Name, Phone, Birthday, Address, Email


class Record:
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.birthday = None
        self.address = None
        self.email = None

    def show_phone(self):
        return self.phone.value

    def change_phone(self, new_phone):
        self.phone = Phone(new_phone)

    def add_birthday(self, date):
        self.birthday = Birthday(date)

    def add_address(self, address):
        self.address = Address(address)

    def add_email(self, email):
        self.email = Email(email)

    def show_birthday(self):
        return self.birthday.value if self.birthday else "No birthday added."

    def show_address(self):
        return self.address.value if self.address else "No address added."

    def show_email(self):
        return self.email.value if self.email else "No email added."

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {self.phone.value}"

    def to_dict(self):
        return {
            "name": self.name.value,
            "phone": self.phone.value,
            "birthday": self.birthday.value if self.birthday else None,
            "address": self.address.value if self.address else None,
            "email": self.email.value if self.email else None,
        }

    @classmethod
    def from_dict(cls, data):
        record = cls(data["name"], data["phone"])
        if data["birthday"]:
            record.birthday = Birthday(data["birthday"])
        if data["address"]:
            record.add_address(data["address"])
        if data["email"]:
            record.add_email(data["email"])
        return record
