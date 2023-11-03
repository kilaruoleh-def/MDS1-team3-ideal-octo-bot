from bot.commands.base_command import BaseCommand


class ShowAllNotesCommand(BaseCommand):
    def execute(self) -> str:
        if not self.objects:
            return "No notes available."
        return "\n".join([note.show() for note in self.objects])
