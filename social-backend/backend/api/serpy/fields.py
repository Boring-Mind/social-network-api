from datetime import datetime, date

from django.utils.dateparse import parse_datetime
from serpy import Field


class DateTimeField(Field):
    """Serpy field that supports date and time."""

    datetime_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    date_format = "%Y-%m-%d"

    def to_value(self, value):
        if isinstance(value, str):
            return parse_datetime(value)
        if isinstance(value, datetime):
            return value.strftime(self.datetime_format)
        if isinstance(value, date):
            return value.strftime(self.date_format)
