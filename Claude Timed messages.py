import time
import pyautogui
from datetime import datetime

# ==========================
# SETTINGS
# ==========================

TARGET_TIME = "05:01"   # ⏰ Change this to HH:MM format
MESSAGE = "Continue"

# ⚠️ Replace with the coordinates of Claude's input box on your screen
CLAUDE_INPUT_X = 1350
CLAUDE_INPUT_Y = 898

# ==========================
# WAIT UNTIL TARGET TIME
# ==========================

print(f"Waiting until {TARGET_TIME}...")

while datetime.now().strftime("%H:%M") < TARGET_TIME:
    time.sleep(10)

print("Target time reached!")

# ==========================
# SEND MESSAGE TO CLAUDE
# ==========================

pyautogui.click(CLAUDE_INPUT_X, CLAUDE_INPUT_Y)
time.sleep(1)

pyautogui.write(MESSAGE, interval=0.1)
pyautogui.press("enter")

print("Message sent to Claude.")
