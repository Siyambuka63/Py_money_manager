"""
main.py
=======

Started: 13.06.25
Updated: 24.06.25
=================  
"""
import sys 
from Money_manager import Money_manager 
# --------------------------------------


def command_line_arg_handler(command_line_args:list, obj:Money_manager): 
    if len(command_line_args) > 1:
        ### Verbose mode 
        if command_line_args[1].lower() in ["true", "verbose", "verbose-mode", "verbose mode", "v"]: 
            if len(command_line_args) == 2:
                obj.cli_app(verbose=True)

            elif len(command_line_args) > 2:
                try: 
                    income = float(command_line_args[2])
                    if type(income) == float:
                        obj.unpack_verbose(income)

                except ValueError: 
                    print("Invalid input type for monthly-net-income\n")

        ### Default mode 
        ### Only display important details
        else: 
            try: 
                # income = int(command_line_args[1])
                income = float(command_line_args[1])
                if type(income) == float:
                    obj.unpack(income)

            except ValueError: 
                print("Invalid input")
                print("Add the appropriate value(s) for *verbose mode*, *monthly-net-income*, or both\n")
        # ========================================

    ### No CL args 
    else: 
        obj.cli_app(verbose=False)

# --------------------------------------
def main(): 
    obj = Money_manager()
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
