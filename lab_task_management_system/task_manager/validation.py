# Starter Code:

""""

"from datetime import datetime

def validate_task_title(title):
    None
    
def validate_task_description(description):
    None    
    
def validate_due_date(due_date):
    None
    
"""

# Solution 1 - Functions for Validation

from datetime import datetime

def validate_task_title(title):
    if not title or not isinstance(title, str):
        raise ValueError("Title must be a non-empty string")
    if len(title.strip()) < 3:
        raise ValueError("Title must be at least 3 characters long")
    return title.strip()

def validate_task_description(description):
    if not description or not isinstance(description, str):
        raise ValueError("Description must be a non-empty string")
    if len(description.strip()) < 5:
        raise ValueError("Description must be at least 5 characters long")
    return description.strip()

def validate_due_date(due_date):
    try:
        # Try to parse the date in YYYY-MM-DD format
        parsed_date = datetime.strptime(due_date, "%Y-%m-%d")
        # Check if date is not in the past
        if parsed_date < datetime.now():
            raise ValueError("Due date cannot be in the past")
        return due_date
    except ValueError as e:
        if "Due date cannot be in the past" in str(e):
            raise
        raise ValueError("Due date must be in YYYY-MM-DD format")
