class Lottery:
    
    """Initializes an empty lottery ticket as a list from 1 to 69"""
    
    def set_empty_ticket(self):
        '''Creates an empty lottery ticket as a list from 1 to 69'''
        self.ticket = list(range(1,70))
        return self.ticket
        
    def remove_number(self, number):
        '''Removes the specified number parameter from the list of available numbers on the ticket'''
        return self.ticket.remove(number)
        
class EmployeeTicket(Lottery):
    
    """Specific lottery ticket object which takes in employee's first & last name, lucky numbers, and powerball number"""
    
    def __init__(self, first=None, last=None, powerball=None, user_picks=[], user_tickets=[]):
        self.first = first
        self.last = last
        self.powerball = powerball
        self.user_picks = user_picks
        self.user_tickets = user_tickets
        self.pick_nums = ["1st","2nd","3rd","4th","5th"]
        
    def get_name(self, first, last):
        '''Function that sets employee's first and last name for ticket'''
        self.first = first
        self.last = last
        
    def get_picks(self):
        '''Function that contains a loop for collecting 5 picks, while also
           specifying the range parameters and ensuring no number is picked twice'''
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
        
    def get_powerball(self):
        '''Function that loops to collect the powerball as long as it is between 1 and 26'''
        while self.powerball == None:
            powerball = int(input("Select Powerball Number (1 thru 26): "))
            if powerball > 26 or powerball < 1:
                print("Powerball number out of range!")
            else:
                self.powerball = powerball
        
        return self.powerball
        
    def ticket_info(self):
        '''Prints the ticket info'''
        return ("\nTicket Info:\n{} {}, Numbers: {} Powerball: {}\n".format(self.first, self.last, [pick for pick in self.user_picks], self.powerball))

class Pool:
    
    """Initializes an empty pool from which tickets can be added to."""
    
    def __init__(self):
        self.pool = []
        self.numbers = []
        self.powerball = None
    
    def add_ticket(self, ticket):
        '''Adds Ticket'''
        self.pool.append(ticket)

        
        
class EmployeePool(Pool):
    
    """Specific lottery ticket object that takes a pool of tickets and selects the winning ticket"""
    
    def show_drawing_pool(self):
        '''Prints all tickets'''
        print("\n _______")
        print("|Tickets| ")
        print(" _______")
        for ticket in self.pool:
            print("Name: {} {}, Numbers: {}, Powerball: {}".format(ticket['first'], ticket['last'], ticket['picks'], ticket['powerball']))
            
    def pick_winner(self):
        for ticket in self.pool:
            self.numbers.append(pick for picks in ticket['picks'])
        
        return self.numbers