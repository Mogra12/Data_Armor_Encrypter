from cryptography.fernet import Fernet
from colorama import Fore

class DataArmor_deenc:
    def generate_key(self) -> str:
        key: bytes = Fernet.generate_key()
        key_decoded: str = key.decode('utf-8')
        with open("key.key", "a") as file:
                file.write(key_decoded)
                
        return key_decoded
            
    def load_key(self) -> bytes:
        self.generate_key()
        with open("key.key","rb") as file:
                return file.read()
    
    def file_encrypter(self, file_path) -> str:
        try:
            f = Fernet(self.load_key())
            
            with open(file_path,"r") as file:
                content:bytes = bytes(file.read(), 'utf-8')
                token:bytes = f.encrypt(content)
                
            with open(file_path,"w") as file:
                pass
            
            with open(file_path,"a") as file:
                token_decoded:str = token.decode('utf-8')
                file.write(token_decoded) 
                
            print(f"{Fore.WHITE}File Encrypted sucessfully!")  
            
        except TypeError:
            print("Invalid Type!")
        except ValueError:
            print("Invalid Value!")
        
    def encrypted_text(self,file_path) -> str:
        return open(file_path,"r").read()
        
    def decrypter_by_keyfile(self, filepath):
        try:
            key:bytes = self.load_key()
            
            f:bytes = Fernet(key)
            
            encryped_text:bytes = bytes(self.encrypted_text(filepath), 'utf-8')
            decrypted_text:bytes = f.decrypt(encryped_text)
            decrypted_text_decoded:str = decrypted_text.decode('utf-8')
            
            with open(filepath,"w") as file:
                pass
            
            with open(filepath,"a") as file:
                file.write(decrypted_text_decoded)
                
            print(f"\n{Fore.LIGHTGREEN_EX}File decrypted sucessfully!{Fore.RESET}\n")    
            
        except ValueError:
            return "Invalid Value!"
        except AttributeError:
            return "Atribute Error!"
        except Exception:
            return "An Error occurred!"

    def decrypter_by_keycli(self, filepath, key_cli):
        try:
            f = Fernet(key_cli)
            
            encryped_text1 = bytes(self.encrypted_text(filepath), 'utf-8')
            
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