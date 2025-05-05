#!/usr/bin/python
# Copyright 2021 MTM

# Program to calculate sales commissions using a menu-based system
# 

import sys
import re
import os
import shutil

# custom files/modules with functions
import formatting
import calc
import settings

def display_menu():
    """Display the main menu options to the user."""
    print("\n===== SALES COMMISSION CALCULATOR =====")
    print("1. Fixed Rate Commission")
    print("2. Variable Rate Commission")
    print("3. Leveraged Commission")
    print("4. Update Saved Settings")
    print("5. Help / Information")
    print("0. Exit")
    print("=======================================")
    return input("Enter your choice (0-5): ")

def get_float_input(prompt, default_value=None):
    """Get a float input from the user with validation and default value."""
    if default_value is not None:
        prompt = f"{prompt} [{default_value}]: $"
    else:
        prompt = f"{prompt}: $"

    while True:
        user_input = input(prompt)
        
        # Use default value if input is empty and default exists
        if not user_input and default_value is not None:
            return default_value
        
        try:
            return float(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")

def fixed_rate_calculation():
    """Handle fixed rate commission calculation."""
    print("\n----- FIXED RATE COMMISSION -----")
    
    # Load saved settings
    saved_settings = settings.load_settings()
    
    # Get revenue (always ask for this as it's dynamic)
    revenue = get_float_input("Enter revenue amount")
    
    # Use saved values as defaults for the rest
    variable_comp = get_float_input(
        "Enter variable compensation amount (quarterly)", 
        saved_settings.get('variable_comp')
    )
    
    quota = get_float_input(
        "Enter quota amount (quarterly)", 
        saved_settings.get('quota')
    )
    
    attainment = get_float_input(
        "Enter quarterly attainment so far", 
        saved_settings.get('attainment')
    )
    
    args = ["fixedrate", str(revenue), str(variable_comp), str(quota), str(attainment)]
    calc.plantype(args, saved_settings.get('fixed_rate'))
    
    # Update settings with new values AND add current revenue to both quarterly and annual attainment
    saved_settings['variable_comp'] = variable_comp
    saved_settings['quota'] = quota
    saved_settings['attainment'] = attainment + revenue
    
    # Update annual attainment
    if 'annual_attainment' not in saved_settings:
        saved_settings['annual_attainment'] = 0.0
    saved_settings['annual_attainment'] += revenue
    
    print(f"\nAttainment updated!")
    print(f"New quarterly attainment: ${saved_settings['attainment']:.2f}")
    print(f"Annual attainment to date: ${saved_settings['annual_attainment']:.2f}")
    settings.save_settings(saved_settings)

def variable_rate_calculation():
    """Handle variable rate commission calculation."""
    print("\n----- VARIABLE RATE COMMISSION -----")
    
    # Load saved settings
    saved_settings = settings.load_settings()
    
    # Get revenue (always ask for this as it's dynamic)
    revenue = get_float_input("Enter revenue amount")
    
    # Use saved values as defaults for the rest
    variable_comp = get_float_input(
        "Enter variable compensation amount (quarterly)", 
        saved_settings.get('variable_comp')
    )
    
    quota = get_float_input(
        "Enter quota amount (quarterly)", 
        saved_settings.get('quota')
    )
    
    attainment = get_float_input(
        "Enter quarterly attainment so far", 
        saved_settings.get('attainment')
    )
    
    args = ["varrate", str(revenue), str(variable_comp), str(quota), str(attainment)]
    calc.plantype(args)
    
    # Update settings with new values AND add current revenue to both quarterly and annual attainment
    saved_settings['variable_comp'] = variable_comp
    saved_settings['quota'] = quota
    saved_settings['attainment'] = attainment + revenue
    
    # Update annual attainment
    if 'annual_attainment' not in saved_settings:
        saved_settings['annual_attainment'] = 0.0
    saved_settings['annual_attainment'] += revenue
    
    print(f"\nAttainment updated!")
    print(f"New quarterly attainment: ${saved_settings['attainment']:.2f}")
    print(f"Annual attainment to date: ${saved_settings['annual_attainment']:.2f}")
    settings.save_settings(saved_settings)

def leveraged_calculation():
    """Handle leveraged commission calculation."""
    print("\n----- LEVERAGED COMMISSION -----")
    
    # Load saved settings
    saved_settings = settings.load_settings()
    
    # Get revenue (always ask for this as it's dynamic)
    revenue = get_float_input("Enter revenue amount")
    
    # Use saved values as defaults for the rest
    variable_comp = get_float_input(
        "Enter variable compensation amount (quarterly)", 
        saved_settings.get('variable_comp')
    )
    
    quota = get_float_input(
        "Enter quota amount (quarterly)", 
        saved_settings.get('quota')
    )
    
    attainment = get_float_input(
        "Enter quarterly attainment so far", 
        saved_settings.get('attainment')
    )
    
    args = ["leveraged", str(revenue), str(variable_comp), str(quota), str(attainment)]
    calc.plantype(args)
    
    # Update settings with new values AND add current revenue to both quarterly and annual attainment
    saved_settings['variable_comp'] = variable_comp
    saved_settings['quota'] = quota
    saved_settings['attainment'] = attainment + revenue
    
    # Update annual attainment
    if 'annual_attainment' not in saved_settings:
        saved_settings['annual_attainment'] = 0.0
    saved_settings['annual_attainment'] += revenue
    
    print(f"\nAttainment updated!")
    print(f"New quarterly attainment: ${saved_settings['attainment']:.2f}")
    print(f"Annual attainment to date: ${saved_settings['annual_attainment']:.2f}")
    settings.save_settings(saved_settings)

def update_settings_menu():
    """Menu to update saved settings."""
    print("\n----- UPDATE SAVED SETTINGS -----")
    
    # Load current settings
    saved_settings = settings.load_settings()
    
    # Display current settings
    print(settings.get_settings_summary())
    
    # Update settings
    print("\nEnter new values (or press enter to keep current value):")
    variable_comp = get_float_input("Variable compensation (quarterly)", saved_settings.get('variable_comp'))
    quota = get_float_input("Quota (quarterly)", saved_settings.get('quota'))
    attainment = get_float_input("Quarterly attainment to date", saved_settings.get('attainment'))
    annual_attainment = get_float_input("Annual attainment to date", saved_settings.get('annual_attainment', 0.0))
    
    # Get fixed rate percentage (no $ symbol)
    fixed_rate_prompt = f"Fixed rate percentage [{saved_settings.get('fixed_rate')}%]: "
    while True:
        user_input = input(fixed_rate_prompt)
        
        # Use default value if input is empty
        if not user_input:
            fixed_rate = saved_settings.get('fixed_rate')
            break
        
        try:
            fixed_rate = float(user_input)
            if fixed_rate < 0:
                print("Error: Rate must be positive")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number.")
    
    # Update settings
    saved_settings['variable_comp'] = variable_comp
    saved_settings['quota'] = quota
    saved_settings['attainment'] = attainment
    saved_settings['annual_attainment'] = annual_attainment
    saved_settings['fixed_rate'] = fixed_rate
    
    # Save updated settings
    if settings.save_settings(saved_settings):
        print("\nSettings updated successfully!")
    else:
        print("\nFailed to update settings.")

def show_help():
    """Display help information."""
    print("\n===== COMMISSION CALCULATOR HELP =====")
    formatting.Help()
    input("\nPress Enter to return to the main menu...")

def main():
    print("\nWelcome to the Sales Commissions Calculator!")
    
    # Check for saved settings on startup
    if os.path.exists(settings.SETTINGS_FILE):
        print(settings.get_settings_summary())
    else:
        print("\nNo saved settings found. Default values will be used.")
    
    while True:
        choice = display_menu()
        
        if choice == '1':
            fixed_rate_calculation()
        elif choice == '2':
            variable_rate_calculation()
        elif choice == '3':
            leveraged_calculation()
        elif choice == '4':
            update_settings_menu()
        elif choice == '5':
            show_help()
        elif choice == '0':
            print("\nThank you for using the Sales Commissions Calculator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
        
        # Ask if the user wants to make another calculation
        if choice in ['1', '2', '3']:
            continue_choice = input("\nWould you like to make another calculation? (y/n): ").lower()
            if continue_choice != 'y':
                print("\nThank you for using the Sales Commissions Calculator. Goodbye!")
                break

if __name__ == "__main__":
    main()
