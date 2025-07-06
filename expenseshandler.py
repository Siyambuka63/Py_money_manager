import json

#ToDo Add singleton
class ExpenseHandler:
    line = 50 * "_"

    file_path = "expenses.json"
    with open(file_path, "r") as file:
        content = json.load(file)

    percentage = 0

    def __init__(self):
        self.get_percent(self.content)

    def edit_expense(self):
        expense = input("\n Enter expense: ")

        flag = False
        for value in self.content.values():
            for v in value.keys():
                if v == expense:
                    flag = True
                    break

        if flag:
            print(f" Your total is {self.percentage:.2f}%")
            percentage = int(input(" Enter the new percentage: "))
            for key, value in self.content.items():
                for k in value.keys():
                    if k == expense:
                        if self.is_valid_percentage(percentage, self.content[key][k]):
                            print(f" Changed {k} from {self.content[key][k]:.2f}% to {percentage:.2f}%\n")
                            self.content[key][k] = round(percentage, 2)
                            with open(self.file_path, "w") as file:
                                json.dump(self.content, file, indent=4)
                        else:
                            print(f" Changing {k} from {self.content[key][k]:.2f}% to {percentage:.2f}% will make the percent total exceed 100%\n")
                            self.edit_expense()
                        break

    def load_expenses(self, value, key=""):
        if type(value) != dict:
            print(f" {key}| \t ({value:.2f}% of monthly income)")
        else:
            print(f"\n{key}")
            print(self.line)
            for key, value in value.items():
                self.load_expenses(value, key)

    def get_percent(self, content):
        if type(content) == dict:
           for key, value in content.items():
               self.get_percent(value)
        elif content > 0:
            self.percentage += content

    def is_valid_percentage(self, new_percentage, old_percentage):
        if 100 >= self.percentage - old_percentage + new_percentage:
            self.percentage = self.percentage - old_percentage + new_percentage
            return True
        else:
            return False

    def main(self):
        self.load_expenses(self.content)
        self.edit_expense()