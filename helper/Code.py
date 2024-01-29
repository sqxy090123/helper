from cryptography.fernet import Fernet
import base64

class Bad

def encrypt_string(s, password):
    cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode()))
    encrypted_bytes = cipher_suite.encrypt(s.encode())
    encrypted_string = base64.urlsafe_b64encode(encrypted_bytes).decode()
    return "@"+encrypted_string+"!"

def decrypt_string(s, password):
    if not s.startswith("@") and s.endswith("!"):
        raise 
    cipher_suite = Fernet(base64.urlsafe_b64encode(password.encode()))
    decrypted_bytes = cipher_suite.decrypt(base64.urlsafe_b64decode(s.encode()))
    decrypted_string = decrypted_bytes.decode()
    return decrypted_string