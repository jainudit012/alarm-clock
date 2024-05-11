from datetime import datetime
import time
from alarm.alarm_clock import AlarmClock

# Inialize the clock
clock = AlarmClock()
# clock2 = AlarmClock()

# print("Are clock and clock2 the same instance?", clock is clock2)

# now = datetime.now()
# print(now)
# Add an alarm
clock_alarm_id = clock.add_alarm("17:14", "saturday")
# clock.delete_alarm(clock_alarm_id) # Remove the alarm

while True:
    # if there are pending alarms then we need to 
    # wait for user to dismiss or snooze the alarm
    if not clock.pending_alarms:
        clock.display_current_time()
    time.sleep(1)
