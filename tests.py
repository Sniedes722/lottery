from greenphire import EmployeeTicket

if __name__ == '__main__':
    max_test = EmployeeTicket(first="Max", last="Test", powerball=26, user_picks=[1,32,45,55,69])
    min_test = EmployeeTicket(first="Min", last="Test", powerball=1, user_picks=[1,39,42,51,69])
    high_test = EmployeeTicket(first="High", last="Range", powerball=27, user_picks=[1,39,42,51,70]) ## should return error
    low_test = EmployeeTicket(first="Low", last="Range", powerball=0, user_picks=[0,39,42,51,69]) ## should return error
    
    max_test.set_empty_ticket()
    min_test.set_empty_ticket()
    high_test.set_empty_ticket()
    low_test.set_empty_ticket()
    
    print(max_test.ticket_info())
    print(min_test.ticket_info())
    print(high_test.ticket_info())
    print(low_test.ticket_info())