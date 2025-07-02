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


class Money_manager:
    """
    Contains methods used to manage and track expenses

    Using the 60:20:20 split, but the ratio can be adjusted
    """

    line = "\n" + 50 * "_" + "\n"
    data = ""
    monthly_salary = 0 
    verbose_mode = False
    percentage = 0

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


    def unpack(self, salary:int | float) -> None:
        self.data +=f"\n {Fore.YELLOW}SPENDINGS"

        self.get_percent(self.content)

        self.load_data(salary, self.content)

        total_spending = salary * (self.percentage / 100)
        surplus = round((salary - total_spending), 2)

        ### saving to variable
        self.data += f"{self.line}"
        self.data += f"Total spendings: \tR {total_spending:.2f} ({self.percentage:.2f}% of {salary:.2f})\n"
        self.data += f"Surplus: \t\t\tR {surplus}\n"

        print(self.data)

    def load_data(self, salary, value, key = ""):
        if type(value) != dict:
            if value > 0:
                cost = salary * value / 100
                if self.verbose_mode:
                    self.data += f" {key} \t| \tR{Fore.YELLOW}{cost:.2f} ({value:.2f}% of monthly income)\n"
                else:
                    self.data += f"{key} \t| \tR{cost:.2f} ({value:.2f}% of your income)\n"
        else:
            self.data += f"\n{key}"
            self.data += self.line
            for key, value in value.items():
                self.load_data(salary, value, key)


    def get_salary(self) -> int | float:
        salary_f = 0.0
        while salary_f == 0.0: 
            print("\n Enter your monthly NET salary")
            salary = input(" R ")

            try: 
                salary_f = float(salary)
                return salary_f 

            except ValueError: 
                print(f" {Fore.RED}Invalid input type")
                print(" Enter a valid number or decimal value")


    def cli_app(self, verbose:bool) -> None: 
        ### Main app 
        banner()
        monthly_salary = self.get_salary()
        
        print(f" {self.line}\n")
        print(f"\n {Fore.YELLOW}Split")
        print(f" - Needs: \t\tR {monthly_salary * needs}")
        print(f" - Investments: \tR {monthly_salary * investments}")
        print(f" - Personal: \t\tR {monthly_salary * personal}")
        print("\n Split ratio = [60:20:20]")
        print(f" {self.line}\n")

        self.unpack(monthly_salary)

        ### Save data to text file 
        print("\n Save the data to a text file? (y/n)")
        save_data = input(" > ")
        if save_data.strip().lower() == "y":
            self.save_data()
        # else:
        print("\n Closing...")
            
   
    def save_data(self) -> None: 
        '''
        Saves the data to a text file
        '''
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d-%H-%M")
        time_now = now.strftime("%Y-%m-%d %H:%M:%S") 

        # filename = f"records/{time_stamp}.txt"
        filename = f"{time_stamp}.txt"

        if self.verbose_mode: 
            # filename = f"records/verbose_{time_stamp}.txt"
            filename = f"verbose_{time_stamp}.txt"

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
