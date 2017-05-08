import random
from .menus import *

class Lottery:
    
    """Initializes an empty lottery ticket as a list from 1 to 69"""
    
    ## Creates an empty lottery ticket as a list from 1 to 69
    def set_empty_ticket(self):
        self.ticket = list(range(1,70))
        return self.ticket
        
    ## Removes the specified number parameter from the list of available numbers on the ticket
    def remove_number(self, number):
        return self.ticket.remove(number)
        
class EmployeeTicket(Lottery):
    
    """Specific lottery ticket object which takes in employee's first & last name, lucky numbers, and powerball number"""
    
    def __init__(self, first=None, last=None, powerball=None):
        self.first = first
        self.last = last
        self.powerball = powerball
        self.pick_nums = ["1st","2nd","3rd","4th","5th"]
        
    ## Function that sets employee's first and last name for ticket    
    def get_name(self, first, last):
        self.first = first
        self.last = last
        
        return self.first, self.last
        
    ## Function that contains a loop for collecting 5 picks, while also
    ## specifying the range parameters and ensuring no number is picked twice    
    def get_picks(self):
        self.set_empty_ticket() ## set an empty lottery ticket
        self.user_picks = [] ## holds the users picks
        counter = 0 ## formatting helper
        while len(self.user_picks) < len(self.pick_nums):
            pick = int(input("Select {} Number (1 thru 69), Excluding: {}: ".format(self.pick_nums[counter], self.user_picks)))
            if pick > 69 or pick < 1:
                print("Number out of range!")
            elif pick not in self.ticket:
                print("You cannot pick the same number twice!")
            else:
                self.user_picks.append(pick)
                self.remove_number(pick)
                counter += 1
            
        return self.user_picks
        
    ## Function that loops to collect the powerball as long as it is between 1 and 26    
    def get_powerball(self):
        while self.powerball == None:
            powerball = int(input("Select Powerball Number (1 thru 26): "))
            if powerball > 26 or powerball < 1:
                print("Powerball number out of range!")
            else:
                self.powerball = powerball
        
        return self.powerball
        
    ## Returns formatted ticket info    
    def ticket_info(self):
        print("\nTicket Info:\n{} {}, Numbers: {} Powerball: {}\n".format(self.first, self.last, [pick for pick in self.user_picks], self.powerball))

class Pool:
    
    """Initializes an empty pool from which tickets can be added to."""
    
    def __init__(self):
        self.pool = []
        self.numbers = []
        self.powerball = None
    
    ## Adds Ticket to Drawing Pool
    def add_ticket(self, ticket):
        return self.pool.append(ticket)

        
        
class EmployeePool(Pool):
    
    """Specific employee drawing pool that shows all tickets and selects the winning ticket"""
    
    ## Shows formatted record of all tickets in the drawing pool
    def show_drawing_pool(self):
        for ticket in self.pool:
            print("Name: {} {}, Numbers: {}, Powerball: {}".format(ticket['first'], ticket['last'], ticket['picks'], ticket['powerball']))
    
    ## Picks numbers of the winning ticket        
    def pick_winning_numbers(self):
        for ticket in self.pool:
            for picks in ticket['picks']:
                self.numbers.append(picks)
        
        winning_numbers = set(i for i in self.numbers if self.numbers.count(i) > 1) ## pulls numbers with a count over 1
        #if len(winning_numbers) is not 5:
        #    winning_numbers.add()
            
        #winning_numbers = sorted(winners, key = winners.get, reverse = True)
        return winning_numbers