# Alarm Clock System

This is a Python-based alarm clock system that allows users to set alarms and snooze the alarms.

## Features

- Display the current time.
- Add alarms for specific days of the week.
- Snooze alarms up to three times at five-minute intervals.
- Remove alarms by their unique ID.

**Python 3.9 and above is recommended**

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/alarm-clock.git
```

2. Navigate to the project directory:
```bash
cd alarm-clock
```

3. Create a new python virtual environment:
```bash
python3 -m venv venv
```

4. Once the virtual environment is created, activate it by running the appropriate command based on your operating system:
    - On Windows
    ```bash
    .\venv\Scripts\activate
    ```

    - On Linux and macOS
    ```bash
    source venv/bin/activate
    ```
    You will see the name of the virtual environment appear at the beginning of your command prompt, indicating that the virtual environment is active.
    **To deactivate** the virtual environment and return to the global Python environment, simply run the following command:
    ```bash
    deactivate
    ```
5. Run ```python main.py``` file for the executing of the sample code
```
from alarm.alarm_clock import AlarmClock
import time
from alarm.enums import DayOfWeek

# Instantiate the AlarmClock object
clock1 = AlarmClock()
# Add an alarm
clock1.add_alarm("12:20", "saturday")

while True:
    clock1.display_current_time()
    time.sleep(1)
```
The snooze duration and maximum allowed snoozes can be configured from the ```alarm/constants.py```