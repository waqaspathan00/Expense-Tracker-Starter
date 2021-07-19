# Expense-Tracker-Starter
This project is a starter file to practice python concepts like: dictionaries, lists, functions, conditionals, loops, and fileIO

# Project Overview
We want to help users manage their expenses. Visualizing data makes it much easier to manage. 

# How do I get this project on my computer?
- Open terminal and change directory to where the project will reside
- For example all my python projects are in a folder called "python" on my desktop. My directory path should look like this $ waqaspathan00/Desktop/python
- Go to the [project landing page](https://github.com/waqaspathan00/Expense-Tracker-Starter) and click on  Code.
- ![image](https://user-images.githubusercontent.com/67988358/126201715-19385d2c-1e95-4d0c-a92e-0908357f5a0c.png)
- While HTTPS tab is selected, copy the link below it
- Enter the following command into terminal
```
git clone {github project link}
# EXAMPLE
git clone https://github.com/waqaspathan00/Expense-Tracker-Starter.git
```
- After this, you should see a folder named Expense-Tracker-Starter in the directory you chose in step 2
- You can now open this folder in your editor and 2 files should appear, main.py and README.md


# Where do I start?
Function stubs have already been made for you and comments that describe what theyre used for. However, you won't be able to use these right off the bat.  
Build out the project piece by piece, don't try and build the final version of the project on your first try.  
Instead, think about how you can break the project into pieces and build out those pieces instead.

For example, the first piece you can start by building is getting data into the expenses dictionary  
For this we will need to take user input for the name of a category, how much budget to allocate for it, and then names of purchases that are relevant to the category

Example of what data might look like inside the expenses dictionary when it is printed
```
print(expenses[“media”])
>>> {“media”: [50, [“Youtube”, “CrunchyRoll”]]
```

# Moving forward
Create a variable called “left_to_allocate”  
The value of it is the monthly income which the user will input  
This variable will represent the amount of available income we have left to allocate

Repeat the process of asking the user to enter categories until:
  - The user enters “done” for the name of a category
  - left_to_allocate equals 0

If the user enters “done” then create a category named “Miscellaneous” with the budget allocated to left_to_allocate

# JSON Usage
Once you are able to produce this, then begin implementing saving and loading into your program.  
Always remember, load first, save later. We always want to load data before starting a program. Inversely, we always want to save our data before closing a program.  Just like a video game.  
Write the save function that writes all the data in the expenses variable into a seperate file.  
THEN write a load function that loads the data from the file you created into the expenses variable (you will need to use global variables for this. Why do we need to do this in the load function but not the save function?)  
TIPS/ HINTS/ LINKS:
- Call the load function before your main logic, call the save function after
- Use JSON file extension, it uses the same formatting as a python dictionary and NoSQL databases
- do testing in a seperate file to really understand how this works

[JSON Documentation](https://docs.python.org/3/library/json.html)

# Additional notes
- Dont be afraid to mess around with the code, figure out how the project works as if it were your own
- Make sure to print out variables to see what their values are during the program (If working in an IDE you can also use Debug mode + Breakpoints)
- If you want to destroy old data just delete the file that it is being stored in. If you did not implement the load function correctly your program will crash. To fix this you need to be sure the data file exists before loading the data

# Requirements
- Implement saving and loading into your program. Each time we run the program we should retain all of the data you created, modified, deleted in previous runs
- Finish function logic for print_categories() to print out the name of all categories that were created
- Finish function logic for print_category() that asks the user to enter what category they want to view, then print out the name of the category and the list of relevant purchases
- Create a function that prints out the average cost of purchases within a category
- The user should be able to change the value of how much monthly income they previously had
- The user should be able to add, edit, and remove items from relevant purchases list within categories 
- The user should be able to add edit and remove categories 

# Ideas
- Can you use color to call attention to text that appears in the console? Maybe print names in one color, numbers in another



