#!/usr/bin/python
# Settings manager for Sales Commission Calculator

import os
import json

# Path to settings file
SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'commission_settings.json')

# Default settings - updated for quarterly values
DEFAULT_SETTINGS = {
    'variable_comp': 37500.0,  # Quarterly variable comp
    'quota': 187500.0,         # Quarterly quota
    'attainment': 0.0,         # Quarterly attainment
    'annual_attainment': 0.0,  # Annual attainment tracker
    'fixed_rate': 10.0,        # Default fixed rate percentage
    'is_quarterly': True       # Indicates we're using quarterly defaults
}

def load_settings():
    """Load settings from file or return defaults if file doesn't exist."""
    try:
        if os.path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        return DEFAULT_SETTINGS.copy()
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: Could not load settings file: {e}")
        return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    """Save settings to file."""
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f, indent=2)
        return True
    except IOError as e:
        print(f"Warning: Could not save settings file: {e}")
        return False

def update_settings(key, value):
    """Update a single setting."""
    settings = load_settings()
    settings[key] = value
    save_settings(settings)

def get_settings_summary():
    """Return a formatted string summarizing current settings."""
    settings = load_settings()
    summary = "\n=== Saved Settings ===\n"
    
    # Handle each setting with proper type checking to avoid format errors
    var_comp = settings.get('variable_comp')
    if isinstance(var_comp, (int, float)):
        summary += f"Variable compensation (quarterly): ${var_comp:.2f}\n"
    else:
        summary += f"Variable compensation (quarterly): Not set\n"
        
    quota = settings.get('quota')
    if isinstance(quota, (int, float)):
        summary += f"Quota (quarterly): ${quota:.2f}\n"
    else:
        summary += f"Quota (quarterly): Not set\n"
        
    attainment = settings.get('attainment')
    if isinstance(attainment, (int, float)):
        summary += f"Quarterly attainment: ${attainment:.2f}\n"
    else:
        summary += f"Quarterly attainment: Not set\n"
        
    annual_attainment = settings.get('annual_attainment')
    if isinstance(annual_attainment, (int, float)):
        summary += f"Annual attainment to date: ${annual_attainment:.2f}\n"
    else:
        summary += f"Annual attainment to date: Not set\n"
        
    fixed_rate = settings.get('fixed_rate')
    if isinstance(fixed_rate, (int, float)):
        summary += f"Default fixed rate: {fixed_rate}%\n"
    else:
        summary += f"Default fixed rate: Not set\n"
        
    return summary