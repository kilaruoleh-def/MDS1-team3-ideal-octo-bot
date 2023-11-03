import re
from typing import Optional

from commands.note_commands import Notebook
from errors.error_decorator import input_error
from models.adress_book import AddressBook
from models.field import Birthday, Address, Email, Phone
from models.record import Record
from storage.storage import Storage


class AssistantBot:
    def __init__(self) -> None:
        """Initialize the bot with an empty contacts dictionary."""
        self.book = AddressBook(Storage.load_from_file())
        self.notes = Notebook()

    def execute_command(self, command: str) -> str:
        """Execute a given command and return the bot's response."""
        command_pattern = re.compile(r"(\w+(?:-\w+)?)(?:\s+(.*))?")
        match = command_pattern.match(command)

        if not match:
            return "Invalid command."

        cmd, args = match.groups()
        cmd = cmd.lower()

        command_function = {
            "hello": self.hello,
            "add": self.add_contact,
            "change": self.change_contact,
            "phone": self.show_phone,
            "all": self.show_all,
            "add-birthday": self.add_birthday,
            "show-birthday": self.show_birthday,
            "birthdays": self.birthdays,
            "note-manager": self.notes.execute_command
            "add-address": self.add_address,
            "show-address": self.show_address,
            "add-email": self.add_email,
            "show-email": self.show_email,
            "delete": self.delete_contact,
        }.get(cmd)

        if command_function:
            return command_function(args)

        if cmd in ["close", "exit"]:
            Storage.save_to_file_note(self.notes.notes)
            Storage.save_to_file(self.book.data)
            raise SystemExit("Good bye!")

        return "Invalid command."

    def hello(self, _: Optional[str]) -> str:
        """Handle the 'hello' command."""
        return "How can I help you?"

    @input_error
    def add_contact(self, args: Optional[str]) -> str:
        if not args:
            return "Invalid format for adding contact. Use 'add [name] [phone] [email] [address] [birthday]'."

        args = re.split(r"\s+", args)

        if len(args) < 2:
            return "Invalid format for adding contact. You must provide at least a name and a phone number."

        name = args[0]
        phone = args[1]
        email = args[2] if len(args) > 2 else None
        address = args[3] if len(args) > 3 else None
        birthday = args[4] if len(args) > 4 else None

        try:
            if phone:
                Phone(phone)
            if email:
                Email(email)
            if birthday:
                Birthday(birthday)
        except ValueError as e:
            return str(e)

        self.book.data[name] = Record(name, phone)
        if email:
            self.book.data[name].add_email(email)
        if address:
            self.book.data[name].add_address(Address(address))
        if birthday:
            self.book.data[name].add_birthday(birthday)

        return "Contact added."

    @input_error
    def change_contact(self, args: Optional[str]) -> str:
        if not args:
            return "Invalid format for changing contact. Use 'change [name] [phone] [email] [address] [birthday]'."

        args = re.split(r"\s+", args)

        if len(args) < 2:
            return "Invalid format for changing contact. You must provide at least a name and a phone number."

        name = args[0]
        new_phone = args[1]
        new_email = args[2] if len(args) > 2 else None
        new_address = args[3] if len(args) > 3 else None
        new_birthday = args[4] if len(args) > 4 else None

        try:
            if name not in self.book.data:
                return f"No contact found for name: {name}"

            if new_email:
                Email(new_email)
            if new_phone:
                Phone(new_phone)
            if new_birthday:
                Birthday(new_birthday)
        except ValueError as e:
            return str(e)

        contact = self.book.data[name]
        contact.change_phone(new_phone)
        if new_email:
            contact.add_email(new_email)
        if new_address:
            contact.add_address(Address(new_address))
        if new_birthday:
            contact.add_birthday(new_birthday)

        return "Contact updated."

    @input_error
    def show_phone(self, args: Optional[str]) -> str:
        """Show the phone number for a given contact name."""
        if not args:
            raise ValueError
        name = args.strip()
        record = self.book.find(name)
        if not record:
            raise KeyError
        return record.show_phone()

    @input_error
    def show_all(self, _: Optional[str]) -> str:
        """Show all saved contacts and their phone numbers."""
        if not self.book.data:
            raise IndexError
        return "\n".join(
            [
                f"{name}: {record.show_phone()}"
                for name, record in self.book.data.items()
            ]
        )

    @input_error
    def add_birthday(self, args):
        if not args:
            return "Invalid format for adding birthday. Use 'add-birthday [name] [DD.MM.YYYY]'."
        name, birthday = args.split(None, 1)
        record = self.book.find(name)
        if record:
            record.add_birthday(birthday)
            return f"Birthday added for {name}."
        return f"No contact found for name: {name}."

    @input_error
    def show_birthday(self, args):
        name = args.strip()
        record = self.book.find(name)
        if record and record.birthday:
            return record.birthday.value
        return f"No birthday data found for name: {name}."

    @input_error
    def birthdays(self, _):
        upcoming_birthdays = self.book.get_birthdays_per_week()
        if not upcoming_birthdays:
            return "No birthdays in the upcoming week."
        output = []
        for day, names in upcoming_birthdays.items():
            output.append(f"{day}: {', '.join(names)}")
        return "\n".join(output)

    @input_error
    def add_address(self, args):
        if not args:
            return (
                "Invalid format for adding address. Use 'add-address [name] [address]'."
            )
        name, address = args.split(None, 1)
        record = self.book.find(name)
        if record:
            record.add_address(Address(address))
            return f"Address added for {name}."
        return f"No contact found for name: {name}."

    @input_error
    def show_address(self, args):
        name = args.strip()
        record = self.book.find(name)
        if record and record.address:
            return record.address.value
        return f"No address data found for name: {name}."

    @input_error
    def add_email(self, args):
        if not args:
            return "Invalid format for adding email. Use 'add-email [name] [email]'."
        name, email = args.split()
        record = self.book.find(name)
        if record:
            try:
                record.add_email(email)
                return f"Email added for {name}."
            except ValueError as e:
                return str(e)

        return f"No contact found for name: {name}"

    @input_error
    def show_email(self, args):
        name = args.strip()
        record = self.book.find(name)
        if record and record.email:
            return record.email.value
        return f"No email data found for name: {name}."

    @input_error
    def delete_contact(self, name: str) -> str:
        if name in self.book.data:
            del self.book.data[name]
            return f"Contact '{name}' deleted."
        else:
            return f"No contact found for name: {name}"
