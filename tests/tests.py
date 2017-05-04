from lottery import EmployeeTicket

if __name__ == '__main__':
    #test1 = EmployeeTicket(first="Shawn", last="Niederriter")
    #test2 = EmployeeTicket(first="Mike", last="McColgan")
    #test1 = EmployeeTicket()
    test2 = EmployeeTicket()
    
    #test1.set_empty_ticket()
    test2.set_empty_ticket()
    
    test2.print_menu()
    
    #test1
    test2.get_name()
    
    #test1.remove_number(5)
    #test2.remove_number(23)
    test2.get_picks()
    
    test2.get_powerball()
    
    #test1.print_ticket_info()
    test2.print_ticket_info()