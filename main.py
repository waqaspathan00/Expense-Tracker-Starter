# uncomment this once you need it
# import json

"""
print the name of all categories in the expenses dictionary
"""
def print_categories(expenses):
  pass

"""
neatly formats and prints the budget and purchases in a category

EXAMPLE:
Allocated Budget: 50
1. Netflix
2. Youtube
3. Hulu
"""
def print_category(category):
  pass

"""
saves all current expenses data into a seperate file using JSON
"""
def save():
  pass

"""
load previous expenses data from a seperate file using JSON

using try catch, return True if you are able to load in previous data, if you cant return False

HINT: you may have to use global variable to do this, why in load() but not in save()?
"""
def load():
  pass

"""
expenses is a dictionary where the key is the name of a budget category and the value is a list.
  the first index of that list is the budget allocated to the category
  the second index of the list is a list of all relevant purchases in that category
"""
expenses = {}

# main logic starts here