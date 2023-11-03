from bot.commands.base_command import BaseCommand


class GetAllUserCommand(BaseCommand):
    def execute(self) -> str:
        if not self.objects:
            return "No users found."

        return "\n".join([str(user) for user in self.objects])
