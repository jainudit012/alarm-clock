from datetime import datetime
import threading
import time
from uuid import uuid4

from alarm.enums import DayOfWeek
from alarm.alarm import Alarm


class AlarmClock:
    """Represents an alarm clock with various functionality.

    Attributes:
        alarms (dict): Dictionary mapping alarm IDs to Alarm objects representing the alarms set in the clock.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls) -> 'AlarmClock':
        # Checking if there is already an instance created
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """Initializes the AlarmClock object."""
        if not hasattr(self, '_initialized'):
            self.alarms: dict[str, Alarm] = {}
            self._alarm_thread = None
            self._initialized: bool = True

    def _check_alarms(self) -> None:
        """Checks the alarms periodically and triggers them if it's time."""
        while True:
            now = datetime.now()
            for alarm in self.alarms.values():
                if alarm.day_of_week == DayOfWeek[now.strftime("%A").upper()] and \
                    alarm.alarm_time == now.strftime("%H:%M"):
                    alarm.trigger()
            time.sleep(60 - int(now.strftime("%S")))  # Check every start of the minute

    def _validate_time_format(self, time_str: str) -> bool:
        """Validates the format of the time string (HH:MM).

        Args:
            time_str (str): The time string to be validated.

        Raises ValueError if the time string is not valid
        """
        try:
            datetime.strptime(time_str, "%H:%M")
        except ValueError as e:
            raise ValueError("Invalid time string format. Expected format 'HH:MM'")
        
    def _validate_and_get_day_of_week(self, day_str: str) -> DayOfWeek:
        """Validates the day of the week string.

        Args:
            day_str (str): The day of the week string to be validated.

        Raises ValueError if the day string is not valid
        """
        if day_str.upper() not in DayOfWeek.__members__:
            raise ValueError(f"Invalid day of the week string. Use {', '.join(DayOfWeek.__members__)}.")
        return DayOfWeek[day_str.upper()]
    
    def _check_duplicate_alarm(self, alarm_time: str, day_of_week: DayOfWeek) -> bool:
        """Checks if there is a duplicate alarm based on alarm_time and day_of_week.

        Args:
            alarm_time (str): The time at which the alarm is set to go off (in HH:MM format).
            day_of_week (DayOfWeek): The day of the week for the alarm from the enum DayOfWeek.

        Returns:
            bool: True if a duplicate alarm is found, False otherwise.
        """
        for alarm in self.alarms.values():
            if alarm.alarm_time == alarm_time and alarm.day_of_week == day_of_week:
                return True
        return False
    
    @property
    def pending_alarms(self) -> bool:
        """Checks if there are pending alarms which have yet to receive human input.
        """
        pending_alarm_alerts = False
        for alarm in self.alarms.values():
            pending_alarm_alerts |= alarm.ringing
        return pending_alarm_alerts

    @staticmethod
    def display_current_time(format="%H:%M:%S") -> None:
        """Displays the current time in the specified format.

        Args:
            format (str, optional): The format string to display the time. 
            Defaults to "%H:%M:%S" (hour:minute:second).
        """
        now = datetime.now()
        print(f"Current Time: {now.strftime(format)}")

    def add_alarm(self, alarm_time: str, day_of_week: str) -> str:
        """Adds a new alarm to the alarm clock.

        Args:
            alarm_time (str): The time at which the alarm is set to go off (in HH:MM format).
            day_of_week (str): The day of the week for the alarm.
        Returns:
            alarm_id (str): The ID of the newly added alarm if created else None.
        """
        self._validate_time_format(alarm_time)
        day_of_week_enum = self._validate_and_get_day_of_week(day_of_week)

        if self._check_duplicate_alarm(alarm_time, day_of_week_enum):
            print(f"Alarm already exists for {day_of_week_enum.name.capitalize()} at {alarm_time}")
            return
        
        if not self.alarms:
            self._alarm_thread = threading.Thread(target=self._check_alarms, daemon=True)
            self._alarm_thread.start()
        
        alarm = Alarm(alarm_time, day_of_week_enum)
        alarm_id = uuid4()
        self.alarms[alarm_id] = alarm
        print(f"Alarm added for {day_of_week_enum.name.capitalize()} at {alarm_time}")
        return alarm_id

    def delete_alarm(self, alarm_id: str) -> None:
        """Removes an alarm from the alarm clock.

        Args:
            alarm (Alarm): The alarm object to be removed.
        """
        if alarm_id in self.alarms:
            del self.alarms[alarm_id]
            print("Alarm removed.")
        else:
            print("Alarm not found.")
