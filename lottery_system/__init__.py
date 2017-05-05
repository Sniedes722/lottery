import sys
import os
from .lottery import EmployeeTicket, EmployeePool


class Menu:
    
    """Menu Interface Object for Employee Lottery System"""
    
    def __init__(self, ticket = None):
        self.ticket = ticket
        self.pool = EmployeePool()
        while True:
            print(""" __________________________________""")
            print("""|Greenphire Employee Lottery System|""")
            print("""|__________________________________|""")
            print("- 1.Add New Ticket\n- 2.View Tickets\n- 3.Draw Winner\n- 4.Exit\n")
            self. option = int(input("Select an Option: "))
            self.option_handler()
                
    def option_handler(self):
        if self.option == 1:
            self.ticket = EmployeeTicket()
            print("\nAdd New Ticket")
            print("______________")
            first = str(input("Enter your first name: "))
            last = str(input("Enter your last name: "))
            self.ticket.get_name(first, last)
            self.ticket.get_picks()
            self.ticket.get_powerball()
            self.pool.add_ticket({"first": self.ticket.first, "last": self.ticket.last, "picks": self.ticket.user_picks, "powerball": self.ticket.powerball})
            print(self.ticket.ticket_info())
        elif self.option == 2:
            self.pool.show_drawing_pool()
        elif self.option == 3:
            print("Holder")
            #winner = EmployeePool(ticket.pool).winning_numbers()
        elif self.option == 4:
            sys.exit()
            return False
        else:
            print("Not a Valid Option!")
    