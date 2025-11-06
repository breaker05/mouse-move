#!/usr/bin/env python3
"""
Mouse Mover - Keep your Mac awake by moving the mouse when idle
"""
import time
import argparse
from datetime import datetime
import pyautogui
import Quartz

# Disable PyAutoGUI's fail-safe
pyautogui.FAILSAFE = False


def get_idle_time():
    """Get the time in seconds since the last user input event (mouse or keyboard)."""
    # Use proper constants for event types
    return Quartz.CGEventSourceSecondsSinceLastEventType(
        Quartz.kCGEventSourceStateHIDSystemState,
        Quartz.kCGAnyInputEventType
    )


def move_mouse_slightly():
    """Move the mouse in a small circle pattern."""
    current_x, current_y = pyautogui.position()

    # Move in a small 5-pixel circle and return to original position
    pyautogui.move(5, 0, duration=0.1)
    pyautogui.move(0, 5, duration=0.1)
    pyautogui.move(-5, 0, duration=0.1)
    pyautogui.move(0, -5, duration=0.1)


def main():
    parser = argparse.ArgumentParser(
        description="Keep your Mac awake by moving the mouse when idle"
    )
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=30,
        help="Interval in seconds to move mouse (default: 30)"
    )
    parser.add_argument(
        "-t", "--idle-threshold",
        type=int,
        default=20,
        help="Only move mouse if system has been idle for this many seconds (default: 20)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Mouse Mover - Keep Your Mac Awake")
    print("=" * 60)
    print(f"Interval: {args.interval} seconds")
    print(f"Idle threshold: {args.idle_threshold} seconds")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    print()

    try:
        while True:
            idle_time = get_idle_time()

            # Only move mouse if system has been idle for longer than threshold
            if idle_time >= args.idle_threshold:
                move_mouse_slightly()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Mouse moved (idle for {idle_time:.1f}s)")
            else:
                # User is active, don't move mouse
                pass

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\n\nStopping mouse mover!")


if __name__ == "__main__":
    main()
