from cryptography.fernet import Fernet

def decrypter_text(text,keyd):
    try:
        f = Fernet(keyd)
        
        encryped_text = bytes(text, 'utf-8')
        
        decrypted_text = f.decrypt(encryped_text)
        decrypted_text_decoded = decrypted_text.decode('utf-8')
        
        return decrypted_text_decoded
    
    except KeyboardInterrupt:
        return "Program Interrupted."
    except ValueError:
        return "Invalid Value!"