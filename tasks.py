import datetime
import pywhatkit
import pygetwindow 
import pyautogui
import webbrowser
import os
import ctypes
import psutil

def play_song(command):
    song = command.replace('play', '').strip()
    pywhatkit.playonyt(song)

def pause_song():
    pyautogui.press('space')

def tell_time():
    return datetime.datetime.now().strftime('%I:%M %p')

def tell_date():
    return datetime.datetime.now().strftime('%A, %B %d, %Y')

def open_gmail():
    webbrowser.open("https://mail.google.com")

def set_reminder(reminder_text):
    with open("reminders.txt", "a") as file:
        file.write(f"{datetime.datetime.now()}: {reminder_text}\\n")

def show_reminders():
    try:
        with open("reminders.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def close_browser():
    browser_processes =     ['chrome', 'firefox', 'edge', 'safari', 'opera' , 'brave']
    for process in psutil.process_iter(['pid', 'name']):
        try:
            if any(browser in process.info['name'].lower() for browser in browser_processes):
                os.kill(process.info['pid'], 9)
        except Exception as e:
            print(f"Error closing process: {e}")


def close_app_window(app_name):
    """Closes a specific application window if found."""
    windows = pygetwindow.getWindowsWithTitle(app_name)
    if windows:
        for window in windows:
            window.close()
        return f"Closed {app_name}."
    
    # If window not found, try force-closing the app
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if app_name.lower() in process.info['name'].lower():
            psutil.Process(process.info['pid']).terminate()
            return f"Force closed {app_name}."
    
    return f"No application named {app_name} found."
def shutdown_pc():
    """Shuts down the PC."""
    os.system("shutdown /s /t 5")  # Shutdown in 5 seconds

def restart_pc():
    """Restarts the PC."""
    os.system("shutdown /r /t 5")  # Restart in 5 seconds

def search_google(query):
    """Opens a Google search for the given query."""
    webbrowser.open(f"https://www.google.com/search?q={query}")

def increase_volume():
    """Increases system volume."""
    for _ in range(5):
        pyautogui.press("volumeup")
    return "Volume increased."

def decrease_volume():
    """Decreases system volume."""
    for _ in range(5):
        pyautogui.press("volumedown")
    return "Volume decreased."

def mute_system():
    """Mutes system volume."""
    pyautogui.press("volumemute")
    return "System muted."

def unmute_system():
    """Unmutes system volume."""
    pyautogui.press("volumemute")
    return "System unmuted."

def lock_pc():
    """Locks the computer."""
    ctypes.windll.user32.LockWorkStation()
    return "PC locked."


def take_screenshot():
    """Takes a screenshot and saves it."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_path = f"screenshot_{timestamp}.png"
    pyautogui.screenshot(screenshot_path)
    return f"Screenshot saved as {screenshot_path}."

def close_window():
    """Closes the currently active window."""
    try:
        active_window = pygetwindow .getActiveWindow()
        if active_window:
            active_window.close()
            return "Closed the active window."
        else:
            return "No active window found."
    except Exception as e:
        return f"Error closing window: {e}"
    