from bot.commands.base_command import BaseCommand


class UserHelpCommand(BaseCommand):
    def execute(self) -> str:
        help_text = """
        Available user commands:
        - add: Add a new user.
        - change: Change a field for an existing user.
        - delete: Delete a user by name.
        - find: Find and display a user by any field.
        - all: Display all users.
        - birthdays: Display users who have birthdays within a specified number of days.
        - home: Switch to home mode.
        - help: Display this help message.
        """
        return help_text
