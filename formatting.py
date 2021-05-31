# functions related to boilerplate text and formatting data

def ArgumentHelp():
	print("Usage:", "commissions <plan type> <revenue> <variable comp> <quota> <attainment to date> ", "\ne.g., python3 commissions.py fixedrate 25000 100000 500000 0", "\ne.g., python3 commissions.py varrate 25000 100000 500000 0", "\ne.g., python3 commissions.py leveraged 25000 100000 500000 0","\n")

def Help():
	print("There are 3 types of commission plans. Pass the appropriate plan type code as argument to the software program.\n\n")
	print("FIXED RATE ( code: fixedrate  ) apply a specific percentage e.g., 10% to the revenue number to determine the commission amount.\n\n")
	print("VARIABLE RATE ( code: varrate  ) apply a deterministic or variable percentage to the revenue number to determine the commission amount.  The rate is the annual variable compensation amount / annual quota.\n\n")
	print("LEVERAGED ( code: leveraged  ) takes the revenue / quota to determine a rate that is applied to the annual variable compensation amount to determine the commission amount.\n")
