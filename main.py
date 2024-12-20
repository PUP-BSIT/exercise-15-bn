from bnpackage import citron, delima, quiambao, relente, ynion
import os

try:
    from colorama import Back, Style, Fore
except ModuleNotFoundError as e:
    print("Please install the packages first inside the requirements.txt")
    print("Use 'python -m pip install -r requirements.txt'.")
    print(f"Error: {e}")

def clear_screen(): # Function for cleaning the terminal
    os.system('cls')

def main_menu():
    choice = 0

    while choice != 6:
        print(Fore.YELLOW + "\n---------- BN GROUP ------------")
        print(Fore.CYAN + Style.BRIGHT + "[1] Justine Delima")
        print("[2] Kathleen Citron")
        print("[3] Ma. Patricia Anne Quiambao")
        print("[4] Patricia Joy Relente")
        print("[5] Ma. Bea Mae Ynion")
        print("[6] Exit")
        print(Fore.YELLOW + "--------------------------------")
        
        try:
            choice = int(input(Style.RESET_ALL 
                               + Fore.YELLOW 
                               + "Enter your choice: "))
        except ValueError:
            print(Fore.RED + "\nYou need to input numbers only..")

        print(Fore.RESET) # Resets the color to white.

        clear_screen()
        match choice:
            case 1:
                print(Fore.CYAN)
                delima.justine_delima()
            case 2:
                print(Fore.GREEN)
                citron.citron_kathleen()
            case 3:
                print(Fore.MAGENTA)
                quiambao.quiambao_mapatricia()
            case 4:
                print(Fore.LIGHTMAGENTA_EX)
                relente.relente_patricia()
            case 5:
                print(Fore.LIGHTCYAN_EX)
                ynion.ynion_mabeamae()
            case 6:
                break
            case _:
                print(Fore.RED + "Invalid choice. Choose only from 1-6")
                input("Please press enter to return.")
                print(Fore.RESET)
        clear_screen()

try :
    main_menu() 
except NameError:
    print("Please install there required packages.")