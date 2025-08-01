"""
Utility functions for the AI Soul Core system.
"""

import json
from typing import Dict, List, Any

def load_json_file(filepath: str) -> Any:
    """
    Safely load a JSON file with error handling.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Loaded JSON content or empty dict/list based on context
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_json_file(filepath: str, data: Any) -> None:
    """
    Safely save data to a JSON file.
    
    Args:
        filepath: Path to save the JSON file
        data: Data to save
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def calculate_emotional_intensity(emotions: Dict[str, float]) -> float:
    """
    Calculate the overall emotional intensity from an emotion state.
    
    Args:
        emotions: Dictionary of emotion values
        
    Returns:
        Average emotional intensity
    """
    if not emotions:
        return 0.0
    return sum(emotions.values()) / len(emotions)

def format_time_delta(seconds: float) -> str:
    """
    Format a time delta in seconds into a human-readable string.
    
    Args:
        seconds: Number of seconds
        
    Returns:
        Formatted string like "2 days, 3 hours, 45 minutes"
    """
    days = int(seconds // (24 * 3600))
    seconds = seconds % (24 * 3600)
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        
    return ", ".join(parts) if parts else "less than a minute"
