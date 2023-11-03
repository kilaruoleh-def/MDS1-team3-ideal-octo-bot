from bot.commands.base_command import BaseCommand
from models.user.user import User


class AddUserCommand(BaseCommand):
    def execute(self) -> str:
        # Logic to add a user
        name = input('Enter name: ')
        phone = input('Enter phone. It should be 10 digits: ')
        email = input('Enter email: ')
        address = input('Enter address: ')
        birthday = input('Enter birthday date. It should be in format DD.MM.YYYY: ')
        user = User(name, phone, email, address, birthday)
        # Here you would add the user to your address book
        self.objects.append(user)
        return f"User {name} added successfully!"
