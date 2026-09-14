# Claude Timed Message Automation

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Placeholder-lightgrey.svg)](#license)
[![Status](https://img.shields.io/badge/Status-Experimental-orange.svg)](#)


The script is designed for simple scheduled interactions where the user wants a message such as `Continue` to be sent automatically without manually interacting with the Claude interface at the scheduled time.

The current implementation uses **PyAutoGUI** to control the mouse and keyboard. It waits until the configured target time, clicks the Claude input box at a specified screen position, types the configured message, and presses **Enter** to send it.

> **Note:** The current script assumes that Claude is already open and that the input box is visible at the configured screen coordinates. It does not currently launch the browser or perform authentication automatically.

## Features

* **Timed messaging** — waits until a configured `HH:MM` time before sending the message.
* **Custom message** — configure the message sent to Claude through the `MESSAGE` setting.
* **Mouse and keyboard automation** — uses PyAutoGUI to click the Claude input field, type the message, and press Enter.
* **Lightweight implementation** — requires only a small Python script and its dependencies.
* **Console feedback** — displays status messages while waiting and after the message is sent.

## Prerequisites

Before running the project, ensure you have:

* **Python 3.x** installed.
* A supported desktop operating system.
* **Claude opened in a web browser**.
* An authenticated Claude session.
* The Claude message input box visible on screen.
* **PyAutoGUI** installed.
* A stable screen layout so the configured mouse coordinates point to the Claude input box.

Because this implementation uses screen coordinates rather than browser DOM selectors, changing the browser window position, display resolution, scaling, or Claude's layout may require updating the coordinates in the script.

## Installation

### 1. Clone the repository

Replace the placeholder repository URL with the actual repository URL:

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

Install PyAutoGUI:

```bash
pip install pyautogui
```

Alternatively, if the project contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Configuration

The main configuration is currently defined directly inside the Python script.

Open:

```text
python_automation_Claudeopenchat.py
```

Locate the settings section:

```python
TARGET_TIME = "05:01"
MESSAGE = "Continue"
```

### Configure the scheduled time

Set `TARGET_TIME` using the `HH:MM` 24-hour format:

```python
TARGET_TIME = "18:30"
```

The script checks the current system time every 10 seconds until it matches the configured target time.

### Configure the message

Change the `MESSAGE` value to the text you want to send:

```python
MESSAGE = "Continue with the next step"
```

> The current implementation defines `MESSAGE`, but the actual send operation currently types the hard-coded string `"Continue"`. To make the setting fully configurable, replace:
>
> ```python
> pyautogui.write("Continue", interval=0.1)
> ```
>
> with:
>
> ```python
> pyautogui.write(MESSAGE, interval=0.1)
> ```
>
> The hard-coded `"Continue"` behavior is present in the current script.

### Configure the Claude input coordinates

The script currently clicks:

```python
pyautogui.click(1350, 898)
```

These coordinates represent the location of the Claude input box on the screen.

Adjust them to match your display:

```python
pyautogui.click(X, Y)
```

You should test the coordinates carefully before relying on the automation.

### Authentication

The current script does not contain a login or authentication mechanism.

Before starting the script:

1. Open Claude in your browser.
2. Sign in to your Claude account.
3. Navigate to the conversation where the message should be sent.
4. Make sure the message input box is visible.
5. Keep the browser and Claude window in the expected screen position.

## Usage

Once the configuration is complete, run:

```bash
python python_automation_Claudeopenchat.py
```

The script will display:

```text
Waiting until 18:30...
```

It will continue waiting until the configured time is reached.

When the target time is reached, it will click the configured position, type the message, and press Enter:

```text
Target time reached!
Message sent to Claude.
```

## Disclaimer

This project automates interaction with the Claude web interface through simulated mouse and keyboard input.

Automating a third-party web interface may violate **Anthropic's Terms of Service**, applicable usage policies, or other platform restrictions. Users are responsible for reviewing and complying with the latest applicable terms, policies, and laws.

Use this software **at your own risk**. The author is not responsible for account restrictions, unexpected actions, lost data, unintended messages, or other consequences resulting from the use of this automation.

This project should be used responsibly and only with accounts and systems that you are authorized to automate.
