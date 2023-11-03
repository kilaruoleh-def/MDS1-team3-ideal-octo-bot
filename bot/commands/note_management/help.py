from bot.commands.base_command import BaseCommand


class NoteHelpCommand(BaseCommand):
    def execute(self) -> str:
        help_text = """
        Available note commands:
        - add: Add a new note (title and text).
        - change: Change the text of a note.
        - delete: Delete a note by title.
        - add_tag: Add a tag to a note.
        - delete_tag: Remove a tag from a note.
        - find: Search and display a note by tag or title.
        - all: Display all notes.
        - home: Switch to home mode.
        - help: Display this help message.
        """
        return help_text
