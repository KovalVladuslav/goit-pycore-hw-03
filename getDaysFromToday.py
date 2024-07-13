from datetime import datetime

def get_days_from_today(date):
    try:
        current_datetime = datetime.today()

        datetime_object_dif = datetime.strptime(date, "%Y-%m-%d")

        res = current_datetime.toordinal() - datetime_object_dif.toordinal()

        return round(res)
    
    except ValueError:
        print(f"{date} is not date format")


print(get_days_from_today('2020-10-09'))