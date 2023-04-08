from colorama import init, Fore, Style

# Инициализировать colorama
init()

def colored(text, color):
    # Вернуть результат - цветное сообщение
    if(color == "BLACK" or color == 'black'):
        return f"{Fore.BLACK}{text}{Style.RESET_ALL}"
    elif(color == "RED" or color == 'red'):
        return f"{Fore.RED}{text}{Style.RESET_ALL}"
    elif(color == "GREEN" or color == 'green'):
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"
    elif(color == "YELLOW" or color == 'yellow'):
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"
    elif(color == "BLUE" or color == 'blue'):
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"
    elif(color == "MAGENTA" or color == 'magenta'):
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"
    elif(color == "CYAN" or color == 'cyan'):
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"
    elif(color == "WHITE" or color == 'white'):
        return f"{Fore.WHITE}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTBLACK_EX" or color == 'lightblack_ex'):
        return f"{Fore.LIGHTBLACK_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTRED_EX" or color == 'lightred_ex'):
        return f"{Fore.LIGHTRED_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTGREEN_EX" or color == 'lightgreen_ex'):
        return f"{Fore.LIGHTGREEN_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTYELLOW_EX" or color == 'lightyellow_ex'):
        return f"{Fore.LIGHTYELLOW_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTBLUE_EX" or color == 'lightblue_ex'):
        return f"{Fore.LIGHTBLUE_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTMAGENTA_EX" or color == 'lightmagenta_ex'):
        return f"{Fore.LIGHTMAGENTA_EX}{text}{Style.RESET_ALL}"
    elif(color == "LIGHTCYAN_EX" or color == 'lightcyan_ex'):
        return f"{Fore.LIGHTCYAN_EX}{text}{Style.RESET_ALL}"
    elif(color == "RESET" or color == 'reset'):
        return f"{Style.RESET_ALL}{text}{Style.RESET_ALL}"
    else:
        return f"{text}"