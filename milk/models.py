from django.db import models
from auth_user.models import CustomUser
import calendar

obj = calendar.Calendar()
days_Jan = dict()
days_Feb = dict()
days_Mar = dict()
days_Apr = dict()
days_May = dict()
days_Jun = dict()
days_Jul = dict()
days_Aug = dict()
days_Sep = dict()
days_Oct = dict()
days_Nov = dict()
days_Dec = dict()


class year2022(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    for day in obj.itermonthdays(2022, 1):
        if day != 0:
            days_Jan[day] = "NULL"

    def call_Jan():
        return days_Jan
    Jan = models.JSONField(default=call_Jan)
    days = dict()
    for day in obj.itermonthdays(2022, 2):
        if day != 0:
            days_Feb[day] = "NULL"

    def call_Feb():
        return days_Feb
    Feb = models.JSONField(default=call_Feb)
    days = dict()
    for day in obj.itermonthdays(2022, 3):
        if day != 0:
            days_Mar[day] = "NULL"

    def call_Mar():
        return days_Mar
    Mar = models.JSONField(default=call_Mar)
    days = dict()
    for day in obj.itermonthdays(2022, 4):
        if day != 0:
            days_Apr[day] = "NULL"

    def call_Apr():
        return days_Apr
    Apr = models.JSONField(default=call_Apr)
    days = dict()
    for day in obj.itermonthdays(2022, 5):
        if day != 0:
            days_May[day] = "NULL"

    def call_May():
        return days_May
    May = models.JSONField(default=call_May)
    days = dict()
    for day in obj.itermonthdays(2022, 6):
        if day != 0:
            days_Jun[day] = "NULL"

    def call_Jun():
        return days_Jun
    Jun = models.JSONField(default=call_Jun)
    days = dict()
    for day in obj.itermonthdays(2022, 7):
        if day != 0:
            days_Jul[day] = "NULL"

    def call_Jul():
        return days_Jul
    Jul = models.JSONField(default=call_Jul)
    days = dict()
    for day in obj.itermonthdays(2022, 8):
        if day != 0:
            days_Aug[day] = "NULL"

    def call_Aug():
        return days_Aug
    Aug = models.JSONField(default=call_Aug)
    days = dict()
    for day in obj.itermonthdays(2022, 9):
        if day != 0:
            days_Sep[day] = "NULL"

    def call_Sep():
        return days_Sep
    Sep = models.JSONField(default=call_Sep)
    days = dict()
    for day in obj.itermonthdays(2022, 10):
        if day != 0:
            days_Oct[day] = "NULL"

    def call_Oct():
        return days_Oct
    Oct = models.JSONField(default=call_Oct)
    days = dict()
    for day in obj.itermonthdays(2022, 11):
        if day != 0:
            days_Nov[day] = "NULL"

    def call_Nov():
        return days_Nov
    Nov = models.JSONField(default=call_Nov)
    days = dict()
    for day in obj.itermonthdays(2022, 12):
        if day != 0:
            days_Dec[day] = "NULL"

    def call_Dec():
        return days_Dec
    Dec = models.JSONField(default=call_Dec)
