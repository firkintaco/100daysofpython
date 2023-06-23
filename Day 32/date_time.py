from datetime import datetime
now = datetime.now()
year = now.year
weekday = now.weekday()
month = now.month
print(month)

# New datetime object
date_of_birth = datetime(year=1995,month=10,day=2)
print(date_of_birth) # 1995-10-02 00:00:00