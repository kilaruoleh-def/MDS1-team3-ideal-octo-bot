from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle
from commands.core import AssistantBot

def bot_cli() -> None:
    """
    Інтерфейс командного рядка для AssistantBot, який підтримує автозаповнення команд.
    """
    bot = AssistantBot()
    print("Ласкаво просимо до помічника-бота! Наберіть команду.")

    # Визначаємо список команд для автозаповнення.
    command_completer = WordCompleter([
        'hello', 'add', 'change', 'phone', 'all',
        'add-birthday', 'show-birthday', 'birthdays'
    ], ignore_case=True)

    # Створення сесії з використанням prompt_toolkit для підтримки автозаповнення.
    session = PromptSession(completer=command_completer, complete_style=CompleteStyle.READLINE_LIKE)

    while True:
        try:
            # Отримуємо введення від користувача з автозаповненням команд.
            user_input = session.prompt("> ", complete_while_typing=True)
            response = bot.execute_command(user_input)
            print(response)
        except SystemExit as e:
            # Виводимо повідомлення про вихід і завершуємо роботу.
            print(f"Завершення роботи: {e}")
            break
        except Exception as e:
            # Виводимо інформацію про помилку.
            print(f"Виникла помилка: {e}")

# Перевіряємо, що скрипт запущений безпосередньо, і викликаємо bot_cli.
if __name__ == "__main__":
    bot_cli()
