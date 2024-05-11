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
    """

    def __init__(self, alarm_time: str, day_of_week: DayOfWeek):
        self.alarm_time: str = alarm_time
        self.day_of_week: DayOfWeek = day_of_week
        self.alert_time: str = alarm_time
        self._snooze_count: int = 0
        self._wait_for_user_input = False
        self._lock = threading.Lock()  # Initialize a threading Lock

    @property
    def ringing(self) -> bool:
        """Returns True if waiting for user to Dismiss or Snooze the alarm."""
        return self._wait_for_user_input
    
    def trigger(self) -> None:
        with self._lock:
            print(f"Alarm alert for {self.day_of_week.name.capitalize()} at {self.alarm_time}")
            self._wait_for_user_input = True
            dismiss_alarm = input('Dismiss the alarm ? Y / N :\n')
            self._handle_dismiss_alarm(dismiss_alarm)


    def _handle_dismiss_alarm(self, user_input) -> None:
        """Handle Dismissal or Snoozing of the Alarm."""
        self._wait_for_user_input = False
        if user_input.lower() in ('n', 'no'):
            if self._snooze_count < SNOOZE_COUNT_THRESHOLD:
                self.snooze()
                return
        print(f"Alarm for {self.day_of_week.name.capitalize()} at {self.alarm_time} dismissed.")

    def snooze(self) -> None:
        """Snoozes the alarm."""
        self._snooze_count += 1
        # print(f"Snooze count: {self.snooze_count}")
        threading.Timer(SNOOZE_DURATION_SECONDS, self.trigger).start()
        print(f"Alarm snoozed for {SNOOZE_DURATION_MINUTES} mins.")
