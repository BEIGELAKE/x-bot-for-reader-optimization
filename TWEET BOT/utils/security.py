from cryptography.fernet import Fernet
import os

# Generate encryption key (should only be done once and stored securely)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load encryption key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the token
def encrypt_token(token):
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_token = cipher_suite.encrypt(token.encode())
    return encrypted_token

# Decrypt the token
def decrypt_token(encrypted_token):
    key = load_key()
    cipher_suite = Fernet(key)
    token = cipher_suite.decrypt(encrypted_token).decode()
    return token
