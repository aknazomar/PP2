# 1 Subtract five days from the current date
from datetime import datetime, timedelta

current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Current Date:", current_date)
print("Date after subtracting 5 days:", new_date)

# 2 Print yesterday, today, and tomorrow
from datetime import datetime, timedelta

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3 Drop microseconds from datetime
from datetime import datetime

current_datetime = datetime.now()
without_microseconds = current_datetime.replace(microsecond=0)

print("With microseconds:", current_datetime)
print("Without microseconds:", without_microseconds)


# 4 Calculate difference between two dates in seconds
from datetime import datetime

date1 = datetime(2026, 2, 27, 12, 0, 0)  # Example date
date2 = datetime(2026, 2, 28, 12, 0, 0)  # Example date

difference = (date2 - date1).total_seconds()
print("Difference in seconds:", difference)
