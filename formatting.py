# functions related to boilerplate text and formatting data

def ArgumentHelp():
    print("\nSALES COMMISSION CALCULATOR")
    print("\nThis program calculates sales commissions based on different commission models.")
    print("Select an option from the menu to get started.")

def Help():
    print("There are 3 types of commission plans:\n")
    print("1. FIXED RATE")
    print("   Apply a specific percentage (e.g., 10%) to the revenue number")
    print("   to determine the commission amount.\n")
    print("2. VARIABLE RATE")
    print("   Apply a deterministic or variable percentage to the revenue number")
    print("   to determine the commission amount. The rate is calculated as:")
    print("   quarterly variable compensation amount / quarterly quota.\n")
    print("3. LEVERAGED")
    print("   Takes the revenue / quota to determine a rate that is applied to")
    print("   the quarterly variable compensation amount to determine the commission amount.\n")
    print("NOTE: The calculator uses quarterly defaults for sales compensation plans")
    print("      and tracks both quarterly and annual attainment.")
