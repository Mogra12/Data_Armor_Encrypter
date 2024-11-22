from os import system, name

def cli_cleaner():
    return system('cls') if name == "nt" else system('clear')