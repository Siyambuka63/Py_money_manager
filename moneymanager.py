"""
Money_manager.py
================

Started: 12.06.25
Updated: 20.06.25
=================   
"""
from expenseshandler import ExpenseHandler
from salaryhandler import SalaryHandler

from _constants import * 
# ----------------------

class MoneyManager:
    def __init__(self):
        self.expense_handler = ExpenseHandler()
        self.salary_handler = SalaryHandler()

    def menu(self) -> None:
        option = ""
        while option not in ["1","2","3"]:
            print(" What would you like to do?")
            print("     1. Edit expenses")
            print("     2. Enter monthly salary")
            print("     3. Close")
            option = input("\n Enter option number: ")

        match option:
            case "1":
                self.expense_handler.main()
                self.menu()
            case "2":
                verbose = ""
                while verbose == "":
                    verbose_input = input(" Do you want verbose output? (y/n): ")
                    verbose = True if verbose_input == "y" else False if verbose_input == "n" else ""
                    if verbose == "":
                        print(" Please enter a valid verbose option.")
                self.salary_handler.main(verbose)
                self.menu()
            case "3":
                print(" Thank you for using MoneyManager")

    def cli_app(self) -> None:
    ### Main app
        banner()
        self.menu()

# ----------------------------------------------