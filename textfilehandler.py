from datetime import datetime
import webbrowser as wb
from colorama import Fore
import os

line = 50 * "_"

### Save data to text file
def save_data(data, directory, verbose:bool) -> None:
    print(" Save the data to a text file? (y/n)")
    if input(" > ").strip().lower() == "y":
        now = datetime.now()
        time_stamp = now.strftime("%Y-%m-%d-%H-%M")
        time_now = now.strftime("%Y-%m-%d %H:%M:%S")

        if verbose:
            # filename = f"records/verbose_{time_stamp}.txt"
            filename = f"verbose_{time_stamp}.txt"
        else:
            # filename = f"records/{time_stamp}.txt"
            filename = f"{time_stamp}.txt"

        with open(f"{directory}/{filename}", "w") as writer:
            writer.write(f"\nTime stamp: [{time_now}]")
            writer.write(data)
            writer.write(f"{line}")

            print(f" Data recorded: '{Fore.YELLOW}{filename}{Fore.RESET}'")

            open_file(directory, filename)
    elif input(" > ").strip().lower() == "n":
        pass
    else:
        print("Invalid input. Enter y or n")
        save_data(data, directory, verbose=False)

### Open file
def open_file(directory, filename) -> None:
    print("\n Open file? (y/n)")
    if input(" > ").lower() == "y":
        os.chdir(directory)
        # wb.open(f"{time_stamp}.txt")
        wb.open(filename)
        # or
        # os.system(f"start notepad.exe {filename}")
    elif input(" > ").lower() == "n":
        pass
    else:
        print("Invalid input. Enter y or n")
        open_file(directory, filename)