import threading

from alarm.enums import DayOfWeek
from alarm.constants import (
    SNOOZE_DURATION_MINUTES, 
    SNOOZE_DURATION_SECONDS, 
    SNOOZE_COUNT_THRESHOLD
)


class Alarm:
    """Represents an alarm with specific attributes.

    Attributes:
        alarm_time (str): The time at which the alarm is set to go off (in HH:MM format).
        day_of_week (DayOfWeek): The day of the week for the alarm.
        alert_time (str): The time at which the alarm should alert the user (in HH:MM format).
    """

    def __init__(self, alarm_time: str, day_of_week: DayOfWeek):
        self.alarm_time: str = alarm_time
        self.day_of_week: DayOfWeek = day_of_week
        self.alert_time: str = alarm_time
        self.snooze_count: int = 0

    def trigger(self) -> None:
        """Triggers the alarm."""
        print(f"Alarm alert for {self.day_of_week.name.capitalize()} at {self.alarm_time}")
        dismiss_alarm = input('Dismiss the alarm ? Y / N : ')
        if dismiss_alarm.lower() in ('n', 'no'):
            if self.snooze_count < SNOOZE_COUNT_THRESHOLD:
                self.snooze()
                return
        print(f"Alarm for {self.day_of_week.name.capitalize()} at {self.alarm_time} dismissed.")

    def snooze(self) -> None:
        """Snoozes the alarm."""
        self.snooze_count += 1
        # print(f"Snooze count: {self.snooze_count}")
        threading.Timer(SNOOZE_DURATION_SECONDS, self.trigger).start()
        print(f"Alarm snoozed for {SNOOZE_DURATION_MINUTES} mins.")
