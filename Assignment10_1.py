#Luca Schram
#Assignment 10.1: Your Own Class
#Implementation  of a class that models the functionality of a real world object.

class Planner:
    #a class meant to imitate the usage of a planner notebook, works by adding events to a dictionary of lists and using a method to display those days and eventts. Also includes a way to
    #mark tasks as completed with strikethroughs and generate a list of 
    __empty_planner = {"Monday" : [None] , "Tuesday" : [None] , "Wednesday" : [None] , "Thursday" : [None] , "Friday" : [None] , "Saturday" : [None] , "Sunday" : [None]}
    #class attribute that creates a template for each instance to copy for the planner structure.
    def __init__(self):
        self.__current_planner = self.__empty_planner.copy()
        #copies the original class attribute in order to not alter it and makes a current planner data attribute for the object.
    def set_event(self , day , event_desc):
        #creates an event in the planner
        if None in self.__current_planner[day]:
            self.__current_planner[day].remove(None)
            #checks if the default None value is in the day and removes it if it is
        self.__current_planner[day].append(event_desc)
        #appends the event to the specified day
    def get_planner(self):
        #a method to return a formatted display of your planner
        for day in self.__current_planner:
            print(f"Day: {day}")
            #loops through each day key in the dictionary and prints the formatted day
            for count, event in enumerate(self.__current_planner[day] , start = 1):
                print(f"\t{count}) {event}")
                #uses the built-in enumerate function to simultaneously iterate through the event list of the current day while keeping a counter that starts at 1 in order
                #to give a counting formatted list of 1) xxxx 2)xxxx 3)xxxx and so forth. I saw the enumerate function in a video as a better alternative to a counting var
                #so im attempting to implement it here
        return(self.__current_planner)
    def mark_done(self , day , event_num):
        strk_text = ""
        #initializes a string for the strikethrough'd version of the event
        for letter in self.__current_planner[day][(event_num - 1)]:
            strk_text += "\u0336" + letter
            #goes through every letter in the specified event given in the method parameters and adds it on to a new string in addition to a unicode character that 
            #essentially looks like the letter is being struck through. Kind of scuffed, but the best implementation I could think of.
        self.__current_planner[day].pop(event_num - 1)
        self.__current_planner[day].insert(event_num - 1 , strk_text)
        #pops the specified event and replaces it with the insert function with the strikethrough version of the text.
    def todo_list(self):
        self.__to_do_list = []
        #initializes a data attribute to store the to do list of all events in the planner currently
        for event in self.__current_planner.values():
            if None not in event:
                self.__to_do_list += event
            #goes through all the list values in the planner dictionary and, after checking that they are not the default None, adds them to the to-do list.
        print(f"List:\n\t{self.__to_do_list}")
        #prints a slightly formatted version of the to-do list.
        return(self.__to_do_list)
        #returns if needed later in the future.


def main():
    #test coode
    plan = Planner()
    plan.set_event("Tuesday" , "CTLE-01: Final Review Paper Due")
    plan.set_event("Tuesday" , "Eat Pasta")
    plan.set_event("Thursday" , "Take out trash")
    plan.set_event("Friday" , "CSE20: Assignment 10.1 Due")
    plan.mark_done("Tuesday" , 2)
    plan.mark_done("Friday" , 1)
    plan.get_planner()
    plan.todo_list() 

if __name__ == "__main__":
    main()