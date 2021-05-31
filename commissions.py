#!/usr/bin/python
# Copyright 2021 MTM


# Program to calculate a sales commissions, using dict, input parameters
# 
# 

#import commands

import sys
import re
import os
import shutil

# custom files/modules with functions
import formatting
import calc

"""
Program to calculate amounts

General shell:
- store the arguments passed
- print out the arguments
- perform calculations
- print

"""
  

def main():
  # This basic command line argument parsing code is provided.

  print("\n\nHello Sales Commissions World! (written in Python3)\n")


	#	ensure the sales person's quota, variable comp and revenue they want to be paid on, are entered as arguments, else given an example

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if len(args) < 1:
    formatting.ArgumentHelp()
    formatting.Help()
    sys.exit(1)
  else:
    calc.plantype(args)
  
  
if __name__ == "__main__":
  main()
