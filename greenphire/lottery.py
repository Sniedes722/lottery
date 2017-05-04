class LotteryTicket:
    
    """Initializes an empty lottery ticket as a list from 1 to 69"""
    
    def set_empty_ticket(self):
        self.ticket = list(range(1,70))
        return self.ticket
        
    def remove_number(self, number):
        return self.ticket.remove(number)
        
class EmployeeTicket(LotteryTicket):
    
    """Specific lottery ticket object which takes in employee's first & last name, lucky numbers, and powerball number"""
    
    def __init__(self, first=None, last=None, powerball=None, user_picks=[]):
        self.first = first
        self.last = last
        self.powerball = powerball
        self.user_picks = user_picks
        self.pick_nums = ["1st","2nd","3rd","4th","5th"]
        
    def get_name(self):
        self.first = str(input("Enter your first name: "))
        self.last = str(input("Enter your last name: "))
        
    def get_picks(self):
        counter = 0
        while len(self.user_picks) < len(self.pick_nums):
            pick = int(input("Select {} Number (1 thru 69): ".format(self.pick_nums[counter])))
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
        self.powerball = int(input("Select Powerball Number (1 thru 26): "))
        
    def ticket_info(self):
        return ("{} {}, Numbers: {} Powerball: {}\n".format(self.first, self.last, [pick for pick in self.user_picks], self.powerball))