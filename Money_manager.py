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

from _constants import * 
# ----------------------


class Money_manager(): 
    """
    Contains methods used to manage and track expenses

    Using the 60:20:20 split, but the ratio can be adjusted
    """

    line = 50 * "_"
    data = ""
    monthly_salary = 0 
    verbose_mode = False 

    def __init__(self):
        colorama.init(autoreset=True)
    # ============================== 

    def check_percentages(self) -> bool:
        '''
        Checks the percentage value of all the expenses/transactions and surplus 
        and ensures that the total percentage is 100%
        '''
        percentage = 0 
        for collection in [categories_needs, categories_investments, categories_personal]: 
            for k in collection:
                if type(collection[k]) == int or type(collection[k]) == float: 
                    percentage += collection[k]

        if (percentage <= 100):
            return True  
        return False 


    def unpack(self, salary:int | float) -> None: 
        print(f"\n {Fore.YELLOW}SPENDINGS\n")

        percentage = 0 
        for collection in [categories_needs, categories_investments, categories_personal]: 
            for k in collection:
                while len(k) < 20:  
                    k += " "

                if type(collection[k.strip()]) == int or type(collection[k.strip()]) == float: 
                    ex1 = salary * (collection[k.strip()] / 100)
                    print(f" {k}| \t{ex1} ({collection[k.strip()]}% of monthly income)\n")
                    percentage += collection[k.strip()]

                    ### saving to variable
                    self.data += f"{k}| \t{ex1} ({collection[k.strip()]}% of monthly income)\n"

        total_spendings = salary * (percentage / 100)
        surplus = round((salary - total_spendings), 2)
        print(f" {self.line}\n")
        print(f" Total spendings: \tR {total_spendings} ({percentage}% of {salary})")
        print(f" Surplus: \t\tR {surplus}")
        print(f" {self.line}\n")

        ### saving to variable
        self.data += f"{self.line}\n"
        self.data += f"\nTotal spendings: \tR {total_spendings} ({percentage}% of {salary})"
        self.data += f"\nSurplus: \t\t\tR {surplus}"


    def unpack_verbose(self, salary:int | float) -> None: 
        self.verbose_mode = True  
        print(f"\n {Fore.YELLOW}SPENDINGS (verbose)\n")

        total_spendings = 0
        percentage = 0 
        count = 1
        for collection in [categories_needs, categories_investments, categories_personal]: 
            for k in collection:
                print(f" #{count}")
                while len(k) < 20:  
                    k += " "
                        
                if type(collection[k.strip()]) == int or type(collection[k.strip()]) == float: 
                    ex1 = salary * (collection[k.strip()] / 100)
                    total_spendings += ex1 
                    print(f" {k}| \t{Fore.YELLOW}{ex1} ({collection[k.strip()]}% of monthly income)")
                    percentage += collection[k.strip()]
                    
                    ### saving to variable
                    self.data += f"{k}| \t{ex1} ({collection[k.strip()]}% of monthly income)\n"

                else:
                    print(f" {k}| \t[Nothing]")
                    
                    ### saving to variable
                    self.data += f"{k}| \t[Nothing]\n"
                print()
                count += 1

        total_spendings = salary * (percentage / 100)
        surplus = round((salary - total_spendings), 2)
        print(f" {self.line}\n\n")
        print(f" Total spendings: \tR {total_spendings} ({percentage}% of {salary})")
        print(f" Surplus: \t\tR {surplus}")
        print(f"\n {self.line}\n")

        ### saving to variable
        self.data += f"{self.line}\n"
        self.data += f"\nTotal spendings: \tR {total_spendings} ({percentage}% of {salary})"
        self.data += f"\nSurplus: \t\t\tR {surplus}"


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

        if verbose: 
            self.unpack_verbose(monthly_salary)
        else: 
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
