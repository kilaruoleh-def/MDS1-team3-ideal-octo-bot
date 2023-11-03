from bot.commands.base_command import BaseCommand


class DeleteNoteCommand(BaseCommand):
    def execute(self) -> str:
        title = input("Enter note title to delete: ")
        for note in self.objects:
            if note.name == title:
                self.objects.remove(note)
                return f"Note '{title}' deleted successfully!"
        return f"Note with title '{title}' not found."
