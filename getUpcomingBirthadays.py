from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        currentDate = datetime.now().date()

        congratulationDate = birthday.replace(year=currentDate.year)

        if congratulationDate < currentDate:
            congratulationDate = congratulationDate.replace(year=currentDate.year + 1)

        daysUntilBirthday = (congratulationDate - currentDate).days

        dayOfWeek = congratulationDate.weekday()
        #перевірка чи не на вихідних др
        if (dayOfWeek > 4):
            holidayAfterBirthaday = 7 - dayOfWeek

            congratulationDate = congratulationDate + timedelta(days=holidayAfterBirthaday)

        #в кого др ближчі 7 днів
        if (daysUntilBirthday <= 7):
            result.append({ "name": user["name"], "congratulation_date": congratulationDate.strftime("%A, %d %B %Y")})
        

    return result


users = [
    {"name": "John Doe", "birthday": "1985.07.21"},
    {"name": "Jane Smith", "birthday": "1990.07.16"}
]

print(get_upcoming_birthdays(users))