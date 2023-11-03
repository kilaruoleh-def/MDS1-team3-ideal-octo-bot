from bot.commands.base_command import BaseCommand


class AddTagCommand(BaseCommand):
    def execute(self) -> str:
        title = input("Enter note title to add a tag: ")
        for note in self.objects:
            if note.name == title:
                tag = input("Enter tag: ")
                note.add_tag(tag)
                return f"Tag '{tag}' added to note '{title}'."
        return f"Note with title '{title}' not found."
