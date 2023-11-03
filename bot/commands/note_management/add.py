from bot.commands.base_command import BaseCommand
from models.note.note import Note


class CreateNoteCommand(BaseCommand):
    def execute(self) -> str:
        title = input("Enter note title: ")
        text = input("Enter note text: ")
        note = Note(title)
        note.change_text(text)
        self.objects.append(note)
        return f"Note '{title}' added successfully!"
