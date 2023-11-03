from bot.commands.base_command import BaseCommand


class ChangeUserCommand(BaseCommand):
    def execute(self) -> str:
        name_to_change = input("Enter the name of the user you want to change: ")

        user_to_change = next((user for user in self.objects if user.name.__str__() == name_to_change), None)
        if user_to_change is None:
            return f"User {name_to_change} not found!"

        field_to_change = input("Enter the field you want to change (name, phone, email, address, birthday): ")
        if field_to_change not in ['name', 'phone', 'email', 'address', 'birthday']:
            return f"Invalid field: {field_to_change}!"

        new_value = input(f"Enter the new value for {field_to_change}: ")

        if field_to_change == 'name':
            user_to_change.name.value = new_value
        elif field_to_change == 'phone':
            user_to_change.phone.value = new_value
        elif field_to_change == 'email':
            user_to_change.email.value = new_value
        elif field_to_change == 'address':
            user_to_change.address.value = new_value
        elif field_to_change == 'birthday':
            user_to_change.birthday.value = new_value

        return f"{field_to_change.capitalize()} for user {name_to_change} changed successfully!"
