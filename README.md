# Shawn Niederriter, Code Assessment
## Employee Lottery System
### Tested Python Version: 3.5.2

### To Run:
After cloning the repo:
```terminal
python3.5 run.py
```

Select an option from the menu screen:
```terminal
 __________________________________
|   Employee Lottery System        |
|__________________________________|
|- 1.Add New Ticket                |
|- 2.View Tickets                  |
|- 3.Draw Winner                   |
|- 4.Exit                          |
|__________________________________|

Select an Option: 
```

- Option 1 adds a new ticket to the drawing.
- Option 2 will show all tickets.
- Option 3 selects a winner.
- Option 4 exits the program, however the program can be cleanly terminated at anytime with CTRL+C.
- Tickets will persist in memory until you close the program.

### The Code:
- All logic code can be found inside the "lottery_system" module.
- ____init____.py contains a Menu object that controls user interaction.
- lottery.py contains ticket & ticket pool objects
- menus.py simply contains display functions for the terminal interface