# Shawn Niederriter, Code Assessment
## Employee Lottery System
### Tested Python Versions: 3.5.2+

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

- Option 1 adds a new ticket to the drawing
```terminal
Select an Option: 1

 ______________
|Add New Ticket|
|______________|

Enter your first name: Shawn
Enter your last name: Niederriter
Select 1st Number (1 thru 69), Excluding: []: 23
Select 2nd Number (1 thru 69), Excluding: [23]: 41
Select 3rd Number (1 thru 69), Excluding: [23, 41]: 45
Select 4th Number (1 thru 69), Excluding: [23, 41, 45]: 59
Select 5th Number (1 thru 69), Excluding: [23, 41, 45, 59]: 71
Number out of range!
Select 5th Number (1 thru 69), Excluding: [23, 41, 45, 59]: 0
Number out of range!
Select 5th Number (1 thru 69), Excluding: [23, 41, 45, 59]: 23
You cannot pick the same number twice!
Select 5th Number (1 thru 69), Excluding: [23, 41, 45, 59]: 15
Select Powerball Number (1 thru 26): 23

Ticket Info:
Shawn Niederriter, Numbers: [23, 41, 45, 59, 15] Powerball: 23
```
- Option 2 will show all tickets.
```terminal
Select an Option: 2


 _______
|  All  |
|Tickets| 
|_______|


Name: Shawn Niederriter, Numbers: [23, 41, 45, 59, 15], Powerball: 23
Name: Foo Bar, Numbers: [23, 61, 15, 41, 69], Powerball: 22
```
- Option 3 selects a winner.
```terminal
Select an Option: 3


 _________
| Winning |
| Ticket  |
|_________|

Numbers: [41, 19, 15, 61, 23], Powerball: 17
```
- Option 4 exits the program, however the program can be cleanly terminated at anytime with CTRL+C.
- Tickets will persist in memory until you close the program.

### The Code:
- All logic code can be found inside the "lottery_system" module.
- ____init____.py contains a Menu object that controls user interaction.
- lottery.py contains ticket & ticket pool objects
- menus.py simply contains display functions for the terminal interface