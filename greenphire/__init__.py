import sys
import os
from .lottery import EmployeeTicket

def menu():
    while True:
        print("""Greenphire Employee Lottery System\n""")
        print("- 1.Add New Ticket\n- 2.View Tickets\n- 3.Draw Winner\n- 4.Exit\n")
        option = int(input("Select an Option: "))
        if option == 1:
            ticket = EmployeeTicket()
            ticket.set_empty_ticket()
            ticket.get_name()
            ticket.get_picks()
            ticket.get_powerball()
            print(ticket.ticket_info())
        elif option == 4:
            sys.exit()
            return False
        else:
            print("Not a Valid Option!")