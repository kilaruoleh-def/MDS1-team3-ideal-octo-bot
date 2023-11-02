import re
from typing import Optional

from errors.error_decorator import input_error
from models.note import Note
from storage.storage import Storage


class NoteBot:
    def __init__(self) -> None:
        self.notes = Storage.load_from_file_note()

    def execute_command(self, ignore) -> str:
        while True:
            try:
                user_input = input("> ")
                command_pattern = re.compile(r'(\w+(?:-\w+)?)(?:\s+(.*))?')
                match = command_pattern.match(user_input)

                if not match:
                    return "Invalid command."

                cmd, args = match.groups()
                cmd = cmd.lower()
                if "to-main" == cmd:
                    return 'You are in main menu'
                command_function = {
                    "hello": self.hello,
                    "show-note": self.show_note,
                    "add-note": self.add_note,
                    "change-note": self.change_note,
                    "delete-note": self.delete_note,
                    "all": self.show_all_titles,
                    "add-tag": self.add_tag,
                    "delete-tag": self.remove_tag,
                    "find-tag": self.find_by_tag,
                    "find-title": self.find_by_title
                }.get(cmd)
                result = command_function(args) if command_function else "Invalid command."
                print(result)
            except SystemExit as e:
                print(e)

    def hello(self, _: Optional[str]) -> str:
        return "How can I help you?"

    @input_error
    def add_note(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 1:
            return "Please enter the note title"
        name = args
        self.notes[name] = Note(name)
        return "Note added."

    @input_error
    def change_note(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 2:
            return "Please enter the note title and new text"
        name, new_text = map(str.strip, args.split())
        if name not in self.notes:
            return "Invalid title"
        self.notes[name].change_text(new_text)
        return "Text updated."

    @input_error
    def show_note(self, args: Optional[str]) -> str:
        if args not in self.notes:
            return "Invalid title"
        return self.notes[args].show()

    @input_error
    def delete_note(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 1:
            return "Please enter the name of tag"
        if args not in self.notes:
            return "Invalid title"
        self.notes.remove(args)
        return "Note deleted."

    @input_error
    def show_all_titles(self, _: Optional[str]) -> str:
        if not self.notes:
            return "There are no notes"
        return '\n'.join([note.name for name, note in self.notes.items()])

    @input_error
    def add_tag(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 2:
            return "Please enter the note title and tag"
        name, tag = map(str.strip, args.split())
        if name not in self.notes:
            return "Invalid title"
        self.notes[name].add_tag(tag)
        return "Teg added."

    @input_error
    def add_tag(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 2:
            return "Please enter the note title and tag"
        name, tag = map(str.strip, args.split())
        if name not in self.notes:
            return "Invalid title"
        self.notes[name].add_tag(tag)
        return "Teg added."

    @input_error
    def remove_tag(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 2:
            return "Please enter the note title and tag"
        name, tag = map(str.strip, args.split())
        if name not in self.notes:
            return "Invalid title"
        self.notes[name].remove_tag(tag)
        return "Teg added."

    @input_error
    def find_by_tag(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 1:
            return "Please enter the tag"
        return '\n'.join([f"{name}: {note.tags}" for name, note in self.notes.items() if note.has_tag(args)])

    @input_error
    def find_by_title(self, args: Optional[str]) -> str:
        if not args or len(args.split()) != 1:
            return "Please enter the tag"
        return '\n'.join([f"{name}: {note.tags}" for name, note in self.notes.items() if args in note.name])
