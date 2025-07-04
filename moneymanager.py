"""
Money_manager.py
================

Started: 12.06.25
Updated: 20.06.25
=================   
"""
import colorama
from colorama import Fore 
from datetime import datetime
import webbrowser as wb 
import os
import json

from _constants import * 
# ----------------------


class MoneyManager:
    """
    Contains methods used to manage and track expenses

    Using the 60:20:20 split, but the ratio can be adjusted
    """

    line = "\n" + 50 * "_" + "\n"
    data = ""
    monthly_salary = 0
    percentage = 0
    option = ""

    file_path = "expenses.json"

    with open(file_path, "r") as file:
        content = json.load(file)

    def __init__(self):
        colorama.init(autoreset=True)
    # ============================== 

    def check_percentages(self) -> bool:
        '''
        Checks the percentage value of all the expenses/transactions and surplus 
        and ensures that the total percentage is 100%
        '''

        if self.percentage == 0:
            self.get_percent(self.content)

        return self.percentage <= 100


    def get_percent(self, content):
        if type(content) == dict:
           for key, value in content.items():
               self.get_percent(value)
        elif content > 0:
            self.percentage += content

    def unpack(self, verbose) -> None:
        if verbose:
            print(f"\n {Fore.YELLOW}SPENDINGS (verbose){Fore.RESET}")
        else:
            self.data +=f"\n {Fore.YELLOW}SPENDINGS{Fore.RESET}"

        self.load_data(self.content, verbose)

        total_spending = self.monthly_salary * (self.percentage / 100)
        surplus = round((self.monthly_salary - total_spending), 2)

        ### saving to variable
        self.data += f"{self.line}"
        self.data += f"Total spendings: \tR {total_spending:.2f} ({self.percentage:.2f}% of {self.monthly_salary:.2f})\n"
        self.data += f"Surplus: \t\t\tR {surplus}\n"

        print(self.data)

    def load_data(self, value, verbose_mode, key = ""):
        if type(value) != dict:
            cost = self.monthly_salary * value / 100
            if verbose_mode:
                self.data += f" {key}| \t{Fore.YELLOW}R{cost:.2f} ({value:.2f}% of monthly income){Fore.RESET}\n"
            else:
                if value > 0:
                    self.data += f"{key}| \t{Fore.YELLOW}R{cost:.2f} ({value:.2f}% of your income){Fore.RESET}\n"
        else:
            self.data += f"\n{key}"
            self.data += self.line
            for key, value in value.items():
                self.load_data(value, verbose_mode, key)

    def load_expenses(self, value, key = ""):
        if type(value) != dict:
            print(f" {key}| \t ({value:.2f}% of monthly income)")
        else:
            print(f"\n{key}")
            print(self.line)
            for key, value in value.items():
                self.load_expenses(value, key)

    def menu(self, verbose) -> None:
        while self.option not in ["1","2","3"]:
            print("What would you like to do?")
            print("1. Edit expenses")
            print("2. Enter monthly salary")
            print("3. Close")
            self.option = input("\nEnter option number: ")

        match self.option:
            case "1":
                self.edit_expenses(verbose)
            case "2":
                self.salary_menu(verbose)
            case "3":
                print("Thank you for using MoneyManager")

    def salary_menu(self, verbose):
        self.get_salary()

        print(f" {self.line}")
        print(f"\n {Fore.YELLOW}Split")
        print(f" - Needs: \t\tR {self.monthly_salary * needs}")
        print(f" - Investments: \tR {self.monthly_salary * investments}")
        print(f" - Personal: \t\tR {self.monthly_salary * personal}")
        print("\n Split ratio = [60:20:20]")
        print(f" {self.line}")

        self.unpack(verbose)

        ### Save data to text file
        print(" Save the data to a text file? (y/n)")
        save_data = input(" > ")
        if save_data.strip().lower() == "y":
            self.save_data(verbose)
        # else:
        self.option = ""
        self.menu(verbose)

    def edit_expenses(self, verbose) -> None:
        self.load_expenses(self.content, verbose)

        expense = input("Enter expense: ")
        flag = False
        for value in self.content.values():
            for v in value.keys():
                if v == expense:
                    flag = True
                    break

        if flag:
            percentage = int(input("Enter the new percentage: "))
            for key, value in self.content.items():
                for k in value.keys():
                    if k == expense:
                        print(f"Changed {k} from {self.content[key][k]:.2f}% to {percentage:.2f}%\n")
                        self.content[key][k] = round(percentage, 2)
                        with open(self.file_path, "w") as file:
                            json.dump(self.content, file, indent = 4)
                        break
            self.option = ""
            self.menu(verbose)
        else:
            print("You entered an invalid option")
            self.edit_expenses(verbose)

    def get_salary(self):
        while self.monthly_salary == 0.0:
            print(" Enter your monthly NET salary")
            try:
                self.monthly_salary = float(input(" R "))
            except ValueError:
                print(f" {Fore.RED}Invalid input type")
                print(" Enter a valid number or decimal value")


    def cli_app(self, verbose:bool) -> None:
        ### Main app 
        banner()
        self.menu(verbose)

    def save_data(self, verbose) -> None:
        '''
        Saves the data to a text file
        '''
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d-%H-%M")
        time_now = now.strftime("%Y-%m-%d %H:%M:%S")

        if verbose:
            # filename = f"records/verbose_{time_stamp}.txt"
            filename = f"verbose_{time_stamp}.txt"
        else:
            # filename = f"records/{time_stamp}.txt"
            filename = f"{time_stamp}.txt"

        with open(f"records/{filename}", "w") as writer: 
            writer.write(f"\nTime stamp: [{time_now}]\n\n")
            writer.write(self.data)
            writer.write(f"\n{self.line}")

        print(f" Data recorded: '{Fore.YELLOW}{filename}{Fore.RESET}'")

        ### Open file 
        print("\n Open file? (y/n)")
        open_file = input(" > ")
        if open_file.lower() == "y":
            os.chdir("records")
            # wb.open(f"{time_stamp}.txt") 
            wb.open(filename) 

            # or 
            # os.system(f"start notepad.exe {filename}")

# ----------------------------------------------
