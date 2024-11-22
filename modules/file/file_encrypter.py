from cryptography.fernet import Fernet
from os.path import exists, basename
from colorama import Fore

class FileEncrypter:
    def generate_key(self) -> bytes:
        key: bytes = Fernet.generate_key()
        key_decoded: str = key.decode('utf-8')
        with open("key.key", "a") as file:
                file.write(key_decoded)
                
        return key_decoded
            
    def load_key(self):
        self.generate_key()
        with open("key.key","rb") as file:
                return file.read()
    
    def file_encrypter(self, file_path):
        try:
            f = Fernet(self.load_key(file_path))
            
            with open(file_path,"r") as file:
                content = bytes(file.read(), 'utf-8')
                token = f.encrypt(content)
                
            with open(file_path,"w") as file:
                pass
            
            with open(file_path,"a") as file:
                token_decoded = token.decode('utf-8')
                file.write(token_decoded) 
            print(f"{Fore.WHITE}File Encrypted sucessfully!")  
            
        except TypeError:
            print("Invalid Type!")
        except ValueError:
            print("Invalid Value!")
        
        def encrypted_text(self,file_path):
                return open(file_path,"r").read()