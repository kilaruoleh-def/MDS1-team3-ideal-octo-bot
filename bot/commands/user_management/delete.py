from bot.commands.base_command import BaseCommand


class DeleteUserCommand(BaseCommand):
    def execute(self) -> str:
        name_to_delete = input("Enter the name of the user you want to delete: ")

        user_to_delete = next((user for user in self.objects if user.name.value == name_to_delete), None)

        if user_to_delete is None:
            return f"User {name_to_delete} not found!"

        self.objects.remove(user_to_delete)
        return f"User {name_to_delete} deleted successfully!"
