# MDS1-team3-ideal-octo-bot

## Overview
Assistant Bot is a command-line interface (CLI) application designed to assist users in managing contacts and notes efficiently. The bot supports various operations such as adding, editing, deleting, and searching for users and notes.

## Features
### User Management
- Add a User: Add a new user by providing details such as name, phone, email, address, and birthday.
- Edit User Details: Edit any field of an existing user.
- Delete a User: Delete a user by specifying their name.
- Search for a User: Search for users by any field.
- Display All Users: List all users in the address book.
- Upcoming Birthdays: Display users who have birthdays within a specified number of days.
### Note Management
- Add a Note: Add a new note with a title and text.
- Edit a Note: Edit the text of a note by specifying its title.
- Delete a Note: Delete a note by specifying its title.
- Search for a Note: Search for notes by tag or title.
- Display All Notes: List all notes.
- Add/Remove Tags: Add or remove tags from a note.

## Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/kilaruoleh-def/MDS1-team3-ideal-octo-bot.git
    ```
2. Navigate to the project directory:
    ```shell
    cd assistant-bot
    ```
3. Install the required dependencies.
    ```shell
    pip install -r requirements.txt
    ```

## Usage
To start the Assistant Bot, run the following command:

    ```shell
    python main.py
    ```

Upon starting, the bot will provide a prompt where you can enter commands. To switch between user management and note management modes, type `user_management` or `note_management` respectively. To return to the main menu, type `home`. To exit the application, type `exit`.

For a list of available commands in any mode, type `help`.