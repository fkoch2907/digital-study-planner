"""
This file stores the definition of the calendar class and its methodes.

We want to create a calendar-like object (final product) in this project.

This calendar should contain the following methodes (functionalities):

- It automatically shows up the current date/time and the events on the day
- It can create a new, empty calendar
- It can add new events with an event name, start/end time, repeat period, and its event type
- It can view events that occur in a month/week/day
- It includes a to-do list. A list of tasks with/without any specific time settings, and can be viewed and edited at
any time
    - (for the end) with overlay decoration
    - Can also automatically include events that occur within a time range (user can set it), such as including events
    within 3 days
- task reminder/notification system for hand-in, deadlines
    - with a day counter

first version: interactive via the terminal window
"""

import os

import pandas as pd
import pickle

class DigitalCalendar:
    """Start a new calendar or access an already existing calendar."""

    def __init__(self, filename: str):
        """Initialize the calendar."""
        self._calendar_filename = f"{filename}.pkl"
        self.calendar = self.check_exists()

    def check_exists(self):
        if os.path.exists(self._calendar_filename):
            print(f"You are checking out your calendar: {self._calendar_filename}")
            return self.load_events_file()
        else:
            print(f"You are creating a new calendar: {self._calendar_filename}")
            return self.make_new_events_file()

    def load_events_file(self):
        with open(self._calendar_filename, "rb") as f:
            return pickle.load(f)

    def make_new_events_file(self):
        """Automatically create a file upon creating a new calendar to store events created for/in this calendar."""
        new_events = pd.DataFrame({})
        with open(f"events_{self._calendar_filename}", "wb") as f:
            pickle.dump(new_events, f)
        return


class Event:
    """Base structure for an event that can be input into the calendar."""

    def __init__(
            self, name: str,
            start_year: int, start_month: int, start_day: int, start_hour: int, start_minute: int,
            end_year: int, end_month: int, end_day: int, end_hour: int, end_minute: int,
            repeat_period_num: int, repeat_period_type: str, event_type: str):
        """Initialize the event."""
        self.name = name
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.start_hour = start_hour
        self.start_minute = start_minute
        self.end_year = end_year
        self.end_month = end_month
        self.end_day = end_day
        self.end_hour = end_hour
        self.end_minute = end_minute
        self.repeat_period = repeat_period_num
        self.repeat_period_type = repeat_period_type
        self.event_type = event_type