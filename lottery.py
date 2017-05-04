class LotteryTicket:
    """Initializes an empty lottery ticket as a list from 1 to 69"""
    def set_empty_ticket(self):
        self.ticket = list(range(1,70))
        return self.ticket
        
    def remove_number(self, number):
        return self.ticket.remove(number)
        
class Drawing:
    """Initializes a drawing object, which can be used to determine the billion dollar ticket"""
    def __init__(self, tickets):
        self.tickets = tickets
        
    def pick_winner(self):
        self.winner = None

class EmployeeTicket(LotteryTicket):
    """Specific lottery ticket object which takes in first & last name, lottery numbers, and powerball"""
    def __init__(self, first=None, last=None, powerball=None, user_picks=[]):
        self.first = first
        self.last = last
        self.powerball = powerball
        self.user_picks = user_picks
        
    def print_menu(self):
        print("""Greenphire Employee Lottery\n""")
        
    def get_name(self):
        self.first = str(input("Enter your first name: "))
        self.last = str(input("Enter your last name: "))
        
    def get_picks(self):
        while len(self.user_picks) < 5:
            pick = int(input("Select Number {} (1 thru 69): ".format(len(self.user_picks))))
            if pick not in self.ticket:
                print("You cannot pick the same number twice!")
            else:
                self.user_picks.append(pick)
                self.remove_number(pick)
            
        return self.user_picks
        
    def get_powerball(self):
        self.powerball = int(input("Select Powerball Number: "))
        
    def print_ticket_info(self):
        print("{} {}'s ticket, {}".format(self.first, self.last, self.user_picks))