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
        self.events = {}

    def check_exists(self):
        if os.path.exists(self._calendar_filename):
            print(f"You are checking out your calendar: {self._calendar_filename}")
            return self.load_calendar()

        else:
            print(f"You are creating a new calendar: {self._calendar_filename}")
            return self.create_calendar()

    def load_calendar(self):
        with open(self._calendar_filename, "rb") as f:\
            return pickle.load(f)

    def create_calendar(self):
        new_calendar = pd.DataFrame({
            self._calendar_filename: [],
        })
        with open(self._calendar_filename, "wb") as f:
            pickle.dump(new_calendar, f)
        return new_calendar