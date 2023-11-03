from bot.commands.base_command import BaseCommand


class FindUserCommand(BaseCommand):
    def execute(self) -> str:
        search_field = input("Enter the field to search (name, phone, email, address, birthday): ")
        search_value = input("Enter the value to search: ").lower()

        if search_field not in ['name', 'phone', 'email', 'address', 'birthday']:
            return f"Invalid field: {search_field}!"

        found_users = [user for user in self.objects if getattr(user, search_field, '').__str__().lower().find(search_value) != -1]

        if not found_users:
            return f"No users found with {search_field} like {search_value}."

        return "\n".join([str(user) for user in found_users])
