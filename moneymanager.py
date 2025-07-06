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
    """
    Contains methods used to manage and track expenses

    Using the 60:20:20 split, but the ratio can be adjusted
    """

    exp = ExpenseHandler()
    sal = SalaryHandler()

    def menu(self) -> None:
        option = ""
        while option not in ["1","2","3"]:
            print("What would you like to do?")
            print("1. Edit expenses")
            print("2. Enter monthly salary")
            print("3. Close")
            option = input("\nEnter option number: ")

        match option:
            case "1":
                self.exp.main()
                self.menu()
            case "2":
                verbose = ""
                while verbose == "":
                    verbose_input = input("Do you want verbose output? (y/n): ")
                    verbose = True if verbose_input == "y" else False if verbose_input == "n" else ""
                    if verbose == "":
                        print("Please enter a valid verbose option.")
                self.sal.main(verbose)
                self.menu()
            case "3":
                print("Thank you for using MoneyManager")

    def cli_app(self) -> None:
        ### Main app 
        banner()
        self.menu()

# ----------------------------------------------
