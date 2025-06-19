"""
_constants.py
=============

Started: 12.06.25
Updated: 19.06.25
=================   
"""

import os 
import colorama
from colorama import Fore 
# --------------------

needs = 0.6         # yellow 
investments = 0.2   # blue  
personal = 0.2      # yellow

### expressed in percentages of the net monthly budget 
categories_needs = {
    "debts": "",
    "transport": 30.0,  
    "parents": "",
    "groceries": 10,
    "electricity": "",

    "water_and_sewage": "",
    "wifi_and_data": 5,
    "medical_related": "",
    "insurance": "",
    "retirement": "",
    
    "school_fees": "",
    "tax": "",
    "security": "",
    "emergency_funds": 10,
    "bond": "",
    
    "vehicle_payment": "",
    "insurance": "",
    "retirement_fund": "",
}

categories_investments = {
    "stocks": 5,
    "real_estate": "",
    "crypto_currency": 5,
    "charity": 5,
}

categories_personal = {
    "restaurant": "", 
    "fast_food": 5, 
    "quick_cash": 5, 
    "amusement": "", 
    "hobbies": {
        "piano": "",
        "fitness": "",
        "bicycle": "",
    }, 
    "snacks": "", 
    "other": "" 
}

# variable_costs = [categories_personal]
# fixed_costs = [categories_needs, categories_investments]

def banner() -> None: 
    # from https://fsymbols.com/generators/carty/
    # ========================================= # 
    text = """
    
 ╔═╗╔═╗─────────────╔═╗╔═╗
 ║║╚╝║║─────────────║║╚╝║║
 ║╔╗╔╗╠══╦═╗╔══╦╗─╔╗║╔╗╔╗╠══╦═╗╔══╦══╦══╦═╗
 ║║║║║║╔╗║╔╗╣║═╣║─║║║║║║║║╔╗║╔╗╣╔╗║╔╗║║═╣╔╝
 ║║║║║║╚╝║║║║║═╣╚═╝║║║║║║║╔╗║║║║╔╗║╚╝║║═╣║
 ╚╝╚╝╚╩══╩╝╚╩══╩═╗╔╝╚╝╚╝╚╩╝╚╩╝╚╩╝╚╩═╗╠══╩╝
 ──────────────╔═╝║───────────────╔═╝║
 ──────────────╚══╝───────────────╚══╝

    """
    # ========================================= # 
    text1 = """

 ╭━┳━╮╱╱╱╱╱╱╱╱╱╭━┳━╮
 ┃┃┃┃┣━┳━┳┳━┳┳╮┃┃┃┃┣━╮╭━┳┳━╮╭━┳━┳┳╮
 ┃┃┃┃┃╋┃┃┃┃┻┫┃┃┃┃┃┃┃╋╰┫┃┃┃╋╰┫╋┃┻┫╭╯
 ╰┻━┻┻━┻┻━┻━╋╮┃╰┻━┻┻━━┻┻━┻━━╋╮┣━┻╯
 ╱╱╱╱╱╱╱╱╱╱╱╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯

    """
    # ========================================= # 

    os.system("cls")
    colorama.init()
    print(f"{Fore.YELLOW}{text1}{Fore.RESET}")
    print(f" NOTE")
    print(f" Expenses and percentages can be altered in '{Fore.YELLOW}_constants.py{Fore.RESET}'\n")
# ---------------------------------------
