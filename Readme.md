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

# Instantiate the AlarmClock object
clock1 = AlarmClock()
# Add an alarm
clock1.add_alarm("12:20", "saturday")

while True:
    if not clock.pending_alarms:
        clock.display_current_time()
    time.sleep(1)
```
The snooze duration and maximum allowed snoozes can be configured from the ```alarm/constants.py```

## Usage
1. Import the AlarmClock class from the alarm_clock module.
```
from alarm_clock import AlarmClock
```
2. Create an instance of the AlarmClock class.
```
clock = AlarmClock()
```
3. Add alarms using the add_alarm method.
```
alarm_id = clock.add_alarm("07:00", "MONDAY")
```
4. Run the alarm system by calling the ```check_alarms``` method.
```
clock.check_alarms()
```
5. Remove the alarm by calling ```delete_alarm``` method with ```alarm_id``` argument.
```
clock.delete_alarm(alarm_id)
```
5. Show the current time.
```
clock.display_current_time()
# Or
AlarmClock.display_current_time()
```
The system will continuously check for alarms and trigger them accordingly.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

