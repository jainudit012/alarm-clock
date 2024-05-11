from alarm.alarm_clock import AlarmClock
import time
from alarm.enums import DayOfWeek


# Example usage
clock1 = AlarmClock()
clock2 = AlarmClock()

print("Are clock1 and clock2 the same instance?", clock1 is clock2)

# Add an alarm
clock1.add_alarm("12:20", "saturday")

while True:
    clock1.display_current_time()
    time.sleep(1)
