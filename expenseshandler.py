import json

from textfilehandler import save_data


class ExpenseHandler:
    ### Singleton
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ExpenseHandler, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.line = 50 * "_"
        self.data = ""

        self.file_path = "expenses.json"
        with open(self.file_path, "r") as file:
            self.content = json.load(file)

        self.percentage = 0
        self.get_percent(self.content)

    def get_percent(self, content):
        if type(content) == dict:
           for key, value in content.items():
               self.get_percent(value)
        elif content > 0:
            self.percentage += content

    def load_expenses(self, value, key=""):
        if type(value) != dict:
            print(f" {key}| \t ({value:.2f}% of monthly income)")
        else:
            print(f"\n {key}")
            print(self.line)
            for key, value in value.items():
                self.load_expenses(value, key)

    def edit_expense(self):
        expense = input("\n Enter expense: ")

        if self.is_valid_expense(expense):
            print(f" Your total is {self.percentage:.2f}%")
            percentage = int(input(" Enter the new percentage: "))
            for key, value in self.content.items():
                    if expense in value.keys():
                        # Checks if the entered value won't make the total percentage exceed 100
                        if self.is_valid_percentage(percentage, self.content[key][expense]):
                            print(f" Changed {expense} from {self.content[key][expense]:.2f}% to {percentage:.2f}%\n")
                            self.content[key][expense] = round(percentage, 2)
                            with open(self.file_path, "w") as file:
                                json.dump(self.content, file, indent=4)
                        else:
                            print(f" Changing {expense} from {self.content[key][expense]:.2f}% to {percentage:.2f}% will make the percent total exceed 100%\n")
                            self.edit_expense()
                        break

    def is_valid_expense(self, expense):
        flag = False

        for value in self.content.values():
            if expense in value.keys():
                flag = True
                break

        return flag

    def is_valid_percentage(self, new_percentage, old_percentage):
        if 100 >= self.percentage - old_percentage + new_percentage:
            self.percentage = self.percentage - old_percentage + new_percentage
            return True
        else:
            return False

    def save_expenses(self, value, key = ""):
        if type(value) != dict:
            self.data += f" {key}| \t ({value:.2f}% of monthly income)\n"
        else:
            self.data += f" \n{key}\n"
            self.data += self.line + "\n"
            for key, value in value.items():
                self.save_expenses(value, key)

    def main(self):
        self.load_expenses(self.content)
        self.edit_expense()
        self.data = ""
        self.save_expenses(self.content)
        save_data(data=self.data, directory="expenses", verbose=False)