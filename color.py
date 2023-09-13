from colorama import init, Fore,Back,Style
init(autoreset=True)

# Colored text
print(Fore.RED + Back.BLUE +"This is red text.")
print(Fore.GREEN + Style.DIM + "This is green text.")
print(Fore.YELLOW + "This is yellow text.")
print(Fore.BLUE + "This is blue text.")
print(Fore.MAGENTA + "This is magenta text.")
print(Fore.CYAN + "This is cyan text.")

