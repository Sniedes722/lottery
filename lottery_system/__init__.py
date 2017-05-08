import sys
import os
import signal

from .lottery import EmployeeTicket, EmployeePool
from .menus import *


class Menu:
    
    """Menu Interface Object for Employee Lottery System"""
    
    def __init__(self):
        signal.signal(signal.SIGINT, signal_handler)
        self.ticket = None
        self.pool = EmployeePool()
    
    ## Menu Loop       
    def option_handler(self):
        while True:
            main_menu()
            self.option = int(input("Select an Option: "))
            if self.option == 1:
                self.ticket = EmployeeTicket()
                add_ticket_menu()
                first = str(input("Enter your first name: "))
                last = str(input("Enter your last name: "))
                self.ticket.get_name(first, last)
                self.ticket.get_picks()
                self.ticket.get_powerball()
                self.pool.add_ticket({"first": self.ticket.first, "last": self.ticket.last, "picks": self.ticket.user_picks, "powerball": self.ticket.powerball})
                self.ticket.ticket_info()
            elif self.option == 2:
                view_tickets_menu()
                self.pool.show_drawing_pool()
            elif self.option == 3:
                winner_menu()
                print(self.pool.pick_winning_numbers())
            elif self.option == 4:
                print("Exiting Lottery System")
                sys.exit(0)
                return False
            else:
                print("Not a Valid Option!")

## Signal handler to kill the lottery program on CTRL+C            
def signal_handler(signal, frame):
    print('Exiting Lottery System')
    return sys.exit(0)
    