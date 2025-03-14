import speech_recognition as sr
import os
import webbrowser
import threading
from speech import take_command, talk
from intent import classify_command
from tasks import (
    play_song, pause_song, tell_time, tell_date, open_gmail, 
    set_reminder, show_reminders, close_browser,lock_pc
)
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define commandsw
CLOSE_WORD = "exit jarvis"
MUTE_WORD = "mute"
UNMUTE_WORD = "unmute"

# Global flags
assistant_active = True
muted = False

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    else:
        talk("Server shutdown not supported.")
        raise RuntimeError('Not running with the Werkzeug Server')


# Home page to take input from the web interface
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    command = request.form.get('command', '').lower()
    if not command:
        return jsonify({'response': 'No command received'}), 400
    
    if command == CLOSE_WORD:
        assistant_active = False
        talk("Shutting down. Goodbye!")
        os._exit(0)  # Forcefully exits the Flask app
        return jsonify({'response': 'Shutting down.'})


    intent = classify_command(command)
    response = execute_command(intent, command)
    return jsonify({'response': response})


def execute_command(intent, command):
    if intent == "PLAY_SONG":
        talk("Playing the song.")
        play_song(command)
        return "Playing ."
    elif intent == "PAUSE":
        pause_song()
        return "Song paused."
    elif intent == "TIME":
        return f"The current time is {tell_time()}."
    elif intent == "DATE":
        return f"Today's date is {tell_date()}."
    elif intent == "OPEN_GMAIL":
        open_gmail()
        return "Gmail opened."
    elif intent == "SET_REMINDER":
        reminder_text = command.replace('set reminder', '').strip()
        set_reminder(reminder_text)
        return "Reminder set."
    elif intent == "SHOW_REMINDERS":
        reminders = show_reminders()
        return "\n".join(reminders) if reminders else "No reminders."
    elif intent == "CLOSE_BROWSER":
        close_browser()
        return "Browser closed."
    elif intent == "LOCK_PC":
        return lock_pc()
    else:
        return "Unknown command."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
