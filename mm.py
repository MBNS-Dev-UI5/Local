import json
import os
from datetime import datetime

# File paths
TASKS_FILE = "tasks.json"
DELETED_TASKS_FILE = "deleted_tasks and main.json"

def get_current_time():
    """Return the current time as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_tasks():
    """Load tasks from the JSON file, or return an empty list if file doesn't exist."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []