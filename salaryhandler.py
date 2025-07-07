from colorama import Fore
import colorama
from expenseshandler import ExpenseHandler
import json

from textfilehandler import save_data

class SalaryHandler:

    ### Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SalaryHandler, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        colorama.init(autoreset=True)

        self.line = "\n" + 50 * "_" + "\n"
        self.data = ""
        self.monthly_salary = 0

        #Gets data from split.json and stores it in split
        file_path = "split.json"
        with open(file_path, "r") as file:
            self.split = json.load(file)

        self.exp = ExpenseHandler()

    def get_salary(self):
        while self.monthly_salary == 0.0:
            print(" Enter your monthly NET salary")
            try:
                self.monthly_salary = float(input(" R "))
            except ValueError:
                print(f" {Fore.RED}Invalid input type")
                print(" Enter a valid number or decimal value")

### prints split
    def load_split(self):
        print(f" {self.line}")
        print(f"\n {Fore.YELLOW}Split")
        print(f" - Needs: \t\tR {self.monthly_salary * self.split["needs"] / 100:.2f}")
        print(f" - Investments: \tR {self.monthly_salary * self.split["investments"] / 100:.2f}")
        print(f" - Personal: \t\tR {self.monthly_salary * self.split["personal"] / 100:.2f}")
        print(f"\n Split ratio = [{self.split["needs"]}:{self.split["investments"]}:{self.split["personal"]}]")
        print(f" {self.line}")

    def unpack(self, verbose) -> None:
        if verbose:
            print(f"\n {Fore.YELLOW}SPENDING (verbose){Fore.RESET}")
        else:
            self.data += f"\n {Fore.YELLOW}SPENDING{Fore.RESET}"

        self.load_data(self.exp.content, verbose)

        total_spending = self.monthly_salary * (self.exp.percentage / 100)
        surplus = round((self.monthly_salary - total_spending), 2)

    ### saving to variable
        self.data += f"{self.line}"
        self.data += f"Total spending: \tR {total_spending:.2f} ({self.exp.percentage:.2f}% of {self.monthly_salary:.2f})\n"
        self.data += f"Surplus: \t\t\tR {surplus}\n"

        print(self.data)

### loads data in the json
    def load_data(self, value, verbose_mode, key=""):
        if type(value) != dict:
            cost = self.monthly_salary * value / 100
            if verbose_mode:
                self.data += f" {key}| \tR{cost:.2f} ({value:.2f}% of monthly income)\n"
            else:
                if value > 0:
                    self.data += f"{key}| \tR{cost:.2f} ({value:.2f}% of your income)\n"
        else:
            self.data += f"\n{key}"
            self.data += self.line
            for key, value in value.items():
                self.load_data(value, verbose_mode, key)

    def main(self, verbose):
        self.get_salary()
        self.load_split()
        self.unpack(verbose)
        save_data(data = self.data, directory= "records", verbose = verbose)
        self.data = ""