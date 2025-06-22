from datetime import UTC, datetime, timedelta


def convert_to_24_hour(time: str) -> str:
    time = time.replace("a.m.", "AM").replace("p.m.", "PM")
    dt = datetime.strptime(time, "%I:%M %p").astimezone(UTC)
    return dt.strftime("%H:%M")


def time_difference_forward(time1: str, time2: str) -> tuple[int, int]:
    dt1 = datetime.strptime(convert_to_24_hour(time1), "%H:%M").astimezone(UTC)
    dt2 = datetime.strptime(convert_to_24_hour(time2), "%H:%M").astimezone(UTC)

    # If time2 is later in the day, calculate same-day difference
    if dt2 >= dt1:
        diff = dt2 - dt1
    else:
        # If time2 is earlier, assume it's the next day
        dt2_next_day = dt2 + timedelta(days=1)
        diff = dt2_next_day - dt1

    # Extract hours and minutes
    total_seconds = int(diff.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60

    return [hours, minutes]


def time_to_eat(time: str) -> list[int]:
    breakfast_diff = time_difference_forward(time, "7:00 a.m.")
    lunch_diff = time_difference_forward(time, "12:00 p.m.")
    dinner_diff = time_difference_forward(time, "7:00 p.m.")
    return sorted([breakfast_diff, lunch_diff, dinner_diff])[0]
