import os
from colorama import Fore
import colorama
from expenseshandler import ExpenseHandler
import json
from datetime import datetime
import webbrowser as wb

#ToDo Add singleton
class SalaryHandler:
    line = "\n" + 50 * "_" + "\n"
    data = ""
    monthly_salary = 0

    file_path = "split.json"
    with open(file_path, "r") as file:
        split = json.load(file)

    exp = ExpenseHandler()

    def __init__(self):
        colorama.init(autoreset=True)

# ==============================

    def unpack(self, verbose) -> None:
        if verbose:
            print(f"\n {Fore.YELLOW}SPENDINGS (verbose){Fore.RESET}")
        else:
            self.data += f"\n {Fore.YELLOW}SPENDINGS{Fore.RESET}"

        self.load_data(self.exp.content, verbose)

        total_spending = self.monthly_salary * (self.exp.percentage / 100)
        surplus = round((self.monthly_salary - total_spending), 2)

    ### saving to variable
        self.data += f"{self.line}"
        self.data += f"Total spendings: \tR {total_spending:.2f} ({self.exp.percentage:.2f}% of {self.monthly_salary:.2f})\n"
        self.data += f"Surplus: \t\t\tR {surplus}\n"

        print(self.data)


    def load_data(self, value, verbose_mode, key=""):
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

    def main(self, verbose):
        self.get_salary()

        print(f" {self.line}")
        print(f"\n {Fore.YELLOW}Split")
        print(f" - Needs: \t\tR {self.monthly_salary * self.split["needs"] / 100:.2f}")
        print(f" - Investments: \tR {self.monthly_salary * self.split["investments"] / 100:.2f}")
        print(f" - Personal: \t\tR {self.monthly_salary * self.split["personal"] / 100:.2f}")
        print(f"\n Split ratio = [{self.split["needs"]}:{self.split["investments"]}:{self.split["personal"]}]")
        print(f" {self.line}")

        self.unpack(verbose)

        ### Save data to text file
        print(" Save the data to a text file? (y/n)")
        save_data = input(" > ")
        if save_data.strip().lower() == "y":
            self.save_data(verbose)

    def get_salary(self):
        while self.monthly_salary == 0.0:
            print(" Enter your monthly NET salary")
            try:
                self.monthly_salary = float(input(" R "))
            except ValueError:
                print(f" {Fore.RED}Invalid input type")
                print(" Enter a valid number or decimal value")

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