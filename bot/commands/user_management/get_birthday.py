from datetime import datetime, timedelta

from bot.commands.base_command import BaseCommand


class BirthdayWithinDaysCommand(BaseCommand):
    def execute(self) -> str:
        try:
            days = int(input("Enter the number of days to search for upcoming birthdays: "))
        except ValueError:
            return "Invalid input. Please enter a valid number of days."

        if days < 0:
            return "Number of days cannot be negative."

        today = datetime.today().date()
        end_date = today + timedelta(days=days)

        found_users = []

        for user in self.objects:
            if user.birthday:
                b_day, b_month = map(int, user.birthday.value.split('.')[:2])

                # Handle leap year case
                if b_month == 2 and b_day == 29 and not today.year % 4 == 0:
                    b_day = 28

                birthday_this_year = datetime(today.year, b_month, b_day).date()

                if today <= birthday_this_year <= end_date:
                    found_users.append(user)

        if not found_users:
            return f"No users found with birthdays within the next {days} days."

        return "\n".join([f"{user.name.value} - {user.birthday.value}" for user in found_users])
