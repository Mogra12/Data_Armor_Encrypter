from cryptography.fernet import Fernet
from .file_encrypter import FileEncrypter
from colorama import Fore

def decrypter_by_keyfile(filepath):
    try:
        file_encrypter = FileEncrypter()
        key = file_encrypter.load_key()
        
        f = Fernet(key)
        
        encryped_text = bytes(file_encrypter.encrypted_text(filepath), 'utf-8')
        
        decrypted_text = f.decrypt(encryped_text)
        decrypted_text_decoded = decrypted_text.decode('utf-8')
        
        with open(filepath,"w") as file:
            pass
        
        with open(filepath,"a") as file:
            file.write(decrypted_text_decoded)
        print(f"\n{Fore.LIGHTGREEN_EX}File decrypted sucessfully!{Fore.RESET}\n")    
    except TypeError:
        return "Invalid Type!"
    except ValueError:
        return "Invalid Value!"
    except AttributeError:
        return "Atribute Error!"
    except Exception:
        return "An Error occurred!"

def decrypter_by_keycli(filepath,key_cli):
    try:
        file_encrypter = FileEncrypter()
        
        f = Fernet(key_cli)
        
        encryped_text1 = bytes(file_encrypter.encrypted_text(filepath), 'utf-8')
        
        decrypted_text1 = f.decrypt(encryped_text1)
        decrypted_text_decoded1 = decrypted_text1.decode('utf-8')
        
        with open(filepath,"w") as file:
            pass
        
        with open(filepath,"a") as file:
            file.write(decrypted_text_decoded1)
            
    except TypeError:
        return "Invalid Type!"
    except ValueError:
        return "Invalid Value!"
    except AttributeError:
        return "Atribute Error!"