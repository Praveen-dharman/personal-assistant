import re
from transformers import pipeline

nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

intents_map = {
    r"\bplay\b": "PLAY_SONG",
    r"\bpause\b": "PAUSE",
    r"\btime\b": "TIME",
    r"\bdate\b": "DATE",
    r"\bopen gmail\b": "OPEN_GMAIL",
    r"\bset reminder\b": "SET_REMINDER",
    r"\bshow reminders\b": "SHOW_REMINDERS",
    r"\bclose browser\b": "CLOSE_BROWSER",
    r"\b(exit|quit|close app)\b": "EXIT",
    r"\bshutdown\b": "SHUTDOWN_PC",
    r"\brestart\b": "RESTART_PC",
    r"\bsearch\b": "SEARCH_GOOGLE",
    r"\bincrease volume\b": "INCREASE_VOLUME",
    r"\bdecrease volume\b": "DECREASE_VOLUME",
    r"\bmute\b": "MUTE_SYSTEM",
    r"\bunmute\b": "UNMUTE_SYSTEM",
    r"\block pc\b": "LOCK_PC",
    r"\btake screenshot\b": "TAKE_SCREENSHOT",
    r"\bclose window\b": "CLOSE_WINDOW",
    r"\bclose app\b": "CLOSE_APP_WINDOW"
}

def classify_command(command):
    """Classifies user input into predefined intents or falls back to NLP-based classification."""
    command = command.lower()
    
    for pattern, intent in intents_map.items():
        if re.search(pattern, command):
            return intent

    try:
        labels = list(intents_map.values())  # Convert to list of possible intents
        results = nlp(command, candidate_labels=labels)
        return results["labels"][0]  # Return the highest confidence label
    except Exception as e:
        return "UNKNOWN"
