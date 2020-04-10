import sys

from ctrla import *
from model import *

options = ["View All", "Add", "Delete", "Edit", "Search", "Import", "Export", "Exit"]
attribs = ["First Name", "Last Name", "Date of Birth", "Email", "Number"]
ac = Ctrla()


class Mainmenu:
    def __init__(self):
        while True:
            self.list_options(options)
            user_choice = input("What would you like to do? ")

            if options[user_choice] == "View All":
                self.print_people()
            elif options[user_choice] == "Add":
                fname = raw_input("First Name: ")
                lname = raw_input("Last Name: ")
                dob = raw_input("Date of Birth: ")
                email = raw_input("Email: ")
                number = raw_input("Number: ")

                x = Person(None, fname, lname, dob, email, number)
                ac.add_person(x)
            elif options[user_choice] == "Delete":
                which_one = input("Which one? ")
                ac.delete_person(which_one)
            elif options[user_choice] == "Edit":
                which_one = input("Which one? ")
                self.list_options(attribs)
                edit_type = input("Edit Type? ")
                edit = raw_input("Enter change: ")
                ac.edit_person(which_one, edit_type, edit)
            elif options[user_choice] == "Search":
                self.list_options(attribs)
                search_id = input("Search By? ")
                search_term = raw_input("Search term? ")
                search_results = ac.search_person(search_id, search_term)

                print(str(len(search_results)) + " record(s) found.")
                for i in search_results:
                    i.to_string()
            elif options[user_choice] == "Import":
                ac.import_people()
            elif options[user_choice] == "Export":
                ac.export_people()
            elif options[user_choice] == "Exit":
                sys.exit()

    @classmethod
    def list_options(cls, list_x):
        for idx, i in enumerate(list_x):
            print(str(idx) + " - " + i)

    @classmethod
    def print_people(cls):
        for i in ac.view_people():
            i.to_string()
