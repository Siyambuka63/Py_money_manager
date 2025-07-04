"""
main.py
=======

Started: 13.06.25
Updated: 24.06.25
=================  
"""
import sys 
from moneymanager import MoneyManager
# --------------------------------------


def command_line_arg_handler(command_line_args:list, obj:MoneyManager):
    if len(command_line_args) > 1:
        ### Verbose mode 
        if command_line_args[1].lower() in ["true", "verbose", "verbose-mode", "verbose mode", "v"]: 
            if len(command_line_args) == 2:
                obj.cli_app(verbose=True)

            elif len(command_line_args) > 2:
                try: 
                    income = float(command_line_args[2])
                    obj.monthly_salary = income
                    if type(income) == float:
                        obj.unpack(verbose=True)

                except ValueError: 
                    print("Invalid input type for monthly-net-income\n")

        ### Default mode 
        ### Only display important details
        else: 
            try: 
                # income = int(command_line_args[1])
                income = float(command_line_args[1])
                obj.monthly_salary = income
                if type(income) == float:
                    obj.unpack(verbose=False)

            except ValueError: 
                print("Invalid input")
                print("Add the appropriate value(s) for *verbose mode*, *monthly-net-income*, or both\n")
        # ========================================

    ### No CL args 
    else: 
        obj.cli_app(verbose=False)

# --------------------------------------
def main(): 
    obj = MoneyManager()
    if obj.check_percentages():
        command_line_arg_handler(command_line_args=sys.argv, obj=obj)
    else:
        print("Invalid percentages. Overall percentage exceeds 100%")
        print("\n  ***Invalid percentages in data-structure(s)***")
        print("  Overall percentage exceeds 100%")
        print("  Check the data in '_constants.py'")
# --------------------------------------

if __name__ == "__main__": 
    main()
# --------------------------------------
