# Mouse Mover

A simple Python application for macOS that automatically moves the mouse to keep your Mac awake, but only when you're not actively using it.

## Features

- Moves mouse in a small circular pattern to prevent sleep
- Detects when you're actively using the computer and pauses
- Configurable interval between mouse movements
- Configurable idle threshold to determine when to activate
- Minimal, non-intrusive movements
- Uses macOS Quartz framework for accurate idle detection

## Requirements

- macOS
- Python 3.6+
- pip3

## Installation

Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

This will install:
- `pyautogui` - For mouse control
- `pyobjc-framework-Quartz` - For macOS system idle time detection

## Usage

### Basic Usage

Run with default settings (moves mouse every 30 seconds if idle for 20+ seconds):

```bash
python3 mouse_mover.py
```

### Custom Configuration

Specify custom interval and idle threshold:

```bash
# Move mouse every 60 seconds if idle for 30+ seconds
python3 mouse_mover.py -i 60 -t 30
```

### Command Line Options

- `-i, --interval`: Interval in seconds between mouse movements (default: 30)
- `-t, --idle-threshold`: Only move mouse if system has been idle for this many seconds (default: 20)

### Examples

```bash
# Check for activity every 15 seconds, move if idle for 10+ seconds
python3 mouse_mover.py -i 15 -t 10

# Check every minute, move if idle for 45+ seconds
python3 mouse_mover.py -i 60 -t 45
```

## How It Works

1. The app uses macOS Quartz framework to check system idle time every N seconds (configurable with `-i`)
2. If the system has been idle for longer than the threshold (configurable with `-t`), it moves the mouse slightly
3. If you move the mouse or press a key, the app detects this instantly and won't interfere
4. The mouse movement is a small 5-pixel circle that returns to the original position
5. The idle detection tracks both mouse and keyboard activity

## Technical Details

- Uses `Quartz.CGEventSourceSecondsSinceLastEventType()` for precise idle time measurement
- Detects any input event type (mouse movement, clicks, keyboard input)
- Non-blocking operation with configurable sleep intervals
- Graceful shutdown with Ctrl+C

## Stopping the Application

Press `Ctrl+C` to stop the application.

## Making It Executable

To run the script directly without typing `python3`:

```bash
chmod +x mouse_mover.py
./mouse_mover.py
```

## Running in Background

To run in the background:

```bash
nohup python3 mouse_mover.py > /dev/null 2>&1 &
```

To stop it later, find the process ID and kill it:

```bash
ps aux | grep mouse_mover
kill <PID>
```

## Troubleshooting

### Import Errors
If you get errors about missing modules, ensure dependencies are installed:
```bash
pip3 install -r requirements.txt
```

### Permission Issues
On macOS, you may need to grant accessibility permissions:
1. Go to System Preferences > Security & Privacy > Privacy > Accessibility
2. Add Terminal or your terminal application to the list
3. Restart the application

### Script Not Moving Mouse
- Verify you're using `python3` instead of `python`
- Check that the idle threshold is set appropriately
- Ensure PyAutoGUI has permission to control your mouse
