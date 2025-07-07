"""
main.py
=======

Started: 13.06.25
Updated: 24.06.25
=================  
"""
import sys 
from moneymanager import MoneyManager
from salaryhandler import SalaryHandler
# --------------------------------------


def command_line_arg_handler(command_line_args:list):
    money_manager = MoneyManager()
    salary_handler = SalaryHandler()
    
    if len(command_line_args) > 1:
        ### Verbose mode 
        if command_line_args[1].lower() in ["true", "verbose", "verbose-mode", "verbose mode", "v"]: 
            if len(command_line_args) == 2:
                salary_handler.main(verbose=True)

            elif len(command_line_args) > 2:
                try: 
                    income = float(command_line_args[2])
                    salary_handler.monthly_salary = income
                    if type(income) == float:
                        salary_handler.unpack(verbose=True)

                except ValueError: 
                    print("Invalid input type for monthly-net-income\n")

        ### Default mode 
        ### Only display important details
        else: 
            try: 
                # income = int(command_line_args[1])
                income = float(command_line_args[1])
                salary_handler.monthly_salary = income
                if type(income) == float:
                    salary_handler.unpack(verbose=False)

            except ValueError: 
                print("Invalid input")
                print("Add the appropriate value(s) for *verbose mode*, *monthly-net-income*, or both\n")
        # ========================================

    ### No CL args 
    else: 
        money_manager.cli_app()

# --------------------------------------
def main(): 
    command_line_arg_handler(command_line_args=sys.argv)

if __name__ == "__main__": 
    main()
# --------------------------------------
