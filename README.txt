Luca Schram , Assignment 10.1 README File

Class Documentation

1) Overall Description
    a) This class is meant to mimic the functionality of a planner in real life, with the ability
    to add events to a running planner dictionary that can then be retrieved to print out a formatted
    version of the planner. There is also a method to mark events/tasks as completed by using a
    strikethrough unicode symbol to mimic the appearance of something being struck through to be marked
    as done. Furthermore, it includes a method that simply prints a list of all current tasks as a todo
    list.

2) Class and Data Variables
    a) Class Variables
        1) __empty_planner - This class attribute is used to keep in store a planner template that is
        used in every object to construct the new planner. Keeps None variables inside each dictionary 
        to display a lack of events if there are no events on a specific day.
    b) Data Variables
        1) self.__current_planner - This data attribute is used to store a running version of the planner
        that is then accessed throughout all the other methods to alter the planner. It also can be accessed
        through the get_planner method later on.
        2)self.__to_do_list - This data attribute is used to store a list of all the current events present
        in the __current_planner variable. It is used in the todo_list method.

3) Methods
    1) __init__
        a) Simply initializes the __current_planner variable with the default __empty_planner for later
        alteration.
    2) set_event(self , day , event_desc)
        a) Sets an event in the planner. Done by passing through the intended day for the event "day" and a
        description for the event "event_desc". This is then passed into the proper list in the dictionary and
        Doesn't return anything, simply alters the data variable __current_planner.
    3) get_planner
        a) Get method that gets the __current_planner variable and prints out an ordered, formatted version
        of the information it contains using a nested for loop. It doesn't require any arguments to execute,
        but it does return the __current_planner variable for usage later if necessary.
    4) mark_done(self , day , event_num)
        a) Method that takes in the arguments of a specified day "day" and an event number from the
        get_planner display "event_num". This method then uses a unicode symbol to mimic the appearance of a
        strikethrough on the event, marking it as done. It does not return anything.
    5) todo_list
        a) Method that takes all of the events in all of the days within the dictionary and prints the list
        of all the events in sequence of the days. This will include the marked done events as well. It
        also returns the variable __to_do_list for later usage if necessary.

4) Demo Program
    1) Description
        a) This demo program simply initializes an object "plan" of the Planner class and then sets four
        events in that planner object. Two are on Tuesday, one is on Thursday, and one is on Friday.
        The second Tuesday assignment "Eat Pasta" and the first and only Friday assignment "CSE20:
        Assignment 10.1 Due" are then marked as completed by the mark_done method. The planner is
        then printed and returned using the get_planner method, and a to-do list is created of all the 
        current tasks with the todo_list method.
    2) Instructions
        a) The demo program can be run simply by entering "python3 Assignment10_1.py" in command line
        or terminal and pressing enter. The program will be run and the demo program's results will be
        displayed on the cmd line display. It can also be run in an IDE such as PyCharm or VSCode by
        simply pressing the run button. It can be altered by altering the parameters of the functions
        in the main function.
