from bot.commands.base_command import BaseCommand


class SearchNoteCommand(BaseCommand):
    def execute(self) -> str:
        query = input("Enter tag or title to search: ").lower()
        found_notes = [
            note for note in self.objects
            if any(query in tag.lower() for tag in note.tags) or query in note.name.lower()
        ]
        if not found_notes:
            return f"No notes found with tag or title containing '{query}'."
        return "\n".join([note.show() for note in found_notes])

