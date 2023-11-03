from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle

from bot.commands.note_management.add import CreateNoteCommand
from bot.commands.note_management.add_tag import AddTagCommand
from bot.commands.note_management.change import EditNoteCommand
from bot.commands.note_management.delete import DeleteNoteCommand
from bot.commands.note_management.find import SearchNoteCommand
from bot.commands.note_management.get_all import ShowAllNotesCommand
from bot.commands.note_management.help import NoteHelpCommand
from bot.commands.note_management.remove_tag import RemoveTagCommand
from bot.commands.user_management.add import AddUserCommand
from bot.commands.user_management.change import ChangeUserCommand
from bot.commands.user_management.delete import DeleteUserCommand
from bot.commands.user_management.find import FindUserCommand
from bot.commands.user_management.get_all import GetAllUserCommand
from bot.commands.user_management.get_birthday import BirthdayWithinDaysCommand
from bot.commands.user_management.help import UserHelpCommand
from errors.error_decorator import input_error
from storage.storage import Storage


class AssistantBot:
    def __init__(self):
        self.mode = None
        self.users = Storage.load_from_file()
        self.notes = Storage.load_from_file_note()

        self.user_commands = {
            'add': AddUserCommand(self.users),
            'change': ChangeUserCommand(self.users),
            'delete': DeleteUserCommand(self.users),
            'find': FindUserCommand(self.users),
            'all': GetAllUserCommand(self.users),
            'birthdays': BirthdayWithinDaysCommand(self.users),
            'help': UserHelpCommand(self.users)
        }
        self.note_commands = {
            'add': CreateNoteCommand(self.notes),
            'change': EditNoteCommand(self.notes),
            'delete': DeleteNoteCommand(self.notes),
            'add_tag': AddTagCommand(self.notes),
            'delete_tag': RemoveTagCommand(self.notes),
            'find': SearchNoteCommand(self.notes),
            'all': ShowAllNotesCommand(self.notes),
            'help': NoteHelpCommand(self.notes),
        }

    def run(self):
        print(
            "Welcome to the assistant bot! Please type 'user_management' to work with Users or 'note_management' to "
            "work with Notes.")

        home_completer = WordCompleter(['user_management', 'note_management', 'exit'], ignore_case=True)
        user_completer = WordCompleter(list(self.user_commands.keys()) + ['home'], ignore_case=True)
        note_completer = WordCompleter(list(self.note_commands.keys()) + ['home'], ignore_case=True)

        while True:
            try:
                if self.mode == 'user_management':
                    session = PromptSession(completer=user_completer, complete_style=CompleteStyle.READLINE_LIKE)
                elif self.mode == 'note_management':
                    session = PromptSession(completer=note_completer, complete_style=CompleteStyle.READLINE_LIKE)
                else:
                    session = PromptSession(completer=home_completer, complete_style=CompleteStyle.READLINE_LIKE)

                user_input = session.prompt("> ", complete_while_typing=True)

                response = self.execute_command(user_input)
                print(response)
            except SystemExit as e:
                print(e)
                break

    @input_error
    def execute_command(self, user_input: str) -> str:
        if user_input == 'home':
            self.mode = None
            return 'Switched to home mode. Available commands: user_management, note_management'

        if user_input == 'exit':
            Storage.save_to_file_note(self.notes)
            Storage.save_to_file(self.users)
            raise SystemExit('Exiting the program...')

        if self.mode == 'user_management':
            return self.execute_user_command(user_input)
        elif self.mode == 'note_management':
            return self.execute_note_command(user_input)
        elif user_input == 'user_management':
            self.mode = 'user_management'
            return 'Switched to user management mode. Please run help to get list of all commands'
        elif user_input == 'note_management':
            self.mode = 'note_management'
            return 'Switched to note management mode. Please run help to get list of all commands'
        else:
            return 'Unknown command. Please run help to get list of all commands'

    def execute_user_command(self, user_input):
        command = self.user_commands.get(user_input)
        if command:
            return command.execute()
        return 'Unknown user command.'

    def execute_note_command(self, user_input):
        command = self.note_commands.get(user_input)
        if command:
            return command.execute()
        return 'Unknown note command.'
