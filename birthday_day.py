import datetime

days_of_week = {0 : 'Monday', 
                1 : 'Tuesday', 
                2 : 'Wednesday', 
                3 : 'Thursday', 
                4 : 'Friday', 
                5 : 'Saturday', 
                6 : 'Sunday'}

birthday_number = 34
birthday_year = 1984 + birthday_number

birthday = datetime.date(birthday_year, 12, 5)
print(days_of_week[birthday.weekday()])
