from cryptography.fernet import Fernet
from colorama import Fore

def text_encrypter(text):
    try:
        text_byte = bytes(text, 'utf-8')
        
        key = Fernet.generate_key()
        key_decoded = key.decode('utf-8')
        f = Fernet(key)
        
        token = f.encrypt(text_byte)
        decoded_token = token.decode('utf-8')
        
        print(f"{Fore.CYAN}\nText Token: {Fore.WHITE}{decoded_token}\n{Fore.CYAN}Key: {Fore.WHITE}{key_decoded}\n")
    except KeyboardInterrupt:
        print("Program Interrupted.")
    except ValueError:
        print("Invalid Value")