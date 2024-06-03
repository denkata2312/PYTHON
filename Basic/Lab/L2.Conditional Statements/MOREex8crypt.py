from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

encrypt_token = f.encrypt(b"Denis Hasan IBAN:5152251251151")
print(encrypt_token)

decrypt_token = f.decrypt(encrypt_token)
print(decrypt_token)