from bot.commands.base_command import BaseCommand


class EditNoteCommand(BaseCommand):
    def execute(self) -> str:
        title = input("Enter note title to edit: ")
        for note in self.objects:
            if note.name == title:
                new_text = input("Enter new text: ")
                note.change_text(new_text)
                return f"Note '{title}' updated successfully!"
        return f"Note with title '{title}' not found."
