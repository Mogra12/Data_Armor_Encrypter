from modules.cli_cleaner import cli_cleaner
from interface.layout import layout
from modules.text.txt_encrypter import text_encrypter
from modules.text.txt_decrypter import decrypter_text
from modules.file.file_encrypter import FileEncrypter
from modules.file.file_decrypter import decrypter_by_keycli
from questionary import select, Style, text
from colorama import Fore

class App:    
    def __init__(self):
        self.custom_theme = Style([
            ('question', 'bold'),
            ('pointer', '#00FFFF'),
            ('selected', '#000000'),
            ('text', '#00FFFF')
        ])
        self.file_encrypter = FileEncrypter()
        
    def run(self):
        cli_cleaner
        layout()
        while True:
            try:
                user_input = select(
                    "Options: ",
                    choices=[
                        "Text Encrypter",
                        "File Encrypter",
                        "Decrypter",
                        "Exit"
                    ],
                    style=self.custom_theme,
                    qmark="",
                    instruction=" "
                ).ask()
                    
                if user_input == "Text Encrypter":
                        cli_cleaner()
                        layout()
                        text_input = text("Enter text:",
                                        style=self.custom_theme,
                                        qmark=""
                                        ).ask()
                        text_encrypter(text_input)
                
                if user_input == "File Encrypter":
                    cli_cleaner()
                    layout()
                    filepath = text("Enter File Path: ",
                                    style=self.custom_theme,
                                    qmark="").ask()
                    self.file_encrypter.file_encrypter(filepath)
                    
        
                if user_input == "Decrypter":
                    cli_cleaner()
                    layout()
                    user_input_decrypter = select(
                        "Decrypter Options:",
                        choices=[
                            "Decrypt Text",
                            "Decrypt File"
                        ],
                        style=self.custom_theme,
                        qmark="",
                        instruction=" "
                    ).ask()
                    if user_input_decrypter == "Decrypt File":
                        user_input_keydecrypter = select(
                            "Key Options:",
                            choices=[
                                "By Key CLI",
                                "By .key file"
                            ],
                            style=self.custom_theme,
                            qmark="",
                            instruction=" "
                        ).ask()
                        try:
                            if user_input_keydecrypter == "By .key file":
                                print(f"{Fore.CYAN}\n The Key have to be in key.key!\n")
                                filepath = text("Enter File Path: ",
                                                    style=self.custom_theme,
                                                    qmark="").ask()
                                
                            elif user_input_keydecrypter == "By Key CLI":
                                filepath = text("Enter File Path: ",
                                                    style=self.custom_theme,
                                                    qmark="").ask()
                                keycli = text("Enter Key: ",
                                                    style=self.custom_theme,
                                                    qmark="").ask()
                                print(f"\n{Fore.WHITE}Decripted File: {Fore.CYAN}{decrypter_by_keycli(filepath,keycli)}\n") 
                            self.file_encrypter.encrypted_text(filepath)
                        except AttributeError:
                            print("An attribute error occurred!")
                    elif user_input_decrypter == "Decrypt Text":
                            textcli = text("Enter Token: ",
                                                style=self.custom_theme,
                                                qmark="").ask()
                            key = text("Enter Key: ",
                                                style=self.custom_theme,
                                                qmark="").ask()
                            print(f"{Fore.CYAN}Text Decrypted: {Fore.WHITE}{decrypter_text(textcli,key)}")
                if user_input == "Exit":
                    print(f"\n{Fore.GREEN}  Goodbye!\n")
                    break
            except KeyboardInterrupt:
                return "Program Interrupted."
                
if "__main__" == __name__:
    app = App()
    app.run()