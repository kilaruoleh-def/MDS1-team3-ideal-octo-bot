from bot.commands.base_command import BaseCommand


class RemoveTagCommand(BaseCommand):
    def execute(self) -> str:
        title = input("Enter note title to remove a tag: ")
        for note in self.objects:
            if note.name == title:
                tag = input("Enter tag to remove: ")
                try:
                    note.remove_tag(tag)
                    return f"Tag '{tag}' removed from note '{title}'."
                except KeyError:
                    return f"Tag '{tag}' not found in note '{title}'."
        return f"Note with title '{title}' not found."
