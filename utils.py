import hashlib
import random
import string
import json

def generate_password():
    """Random bir şifre oluştur ve MD5 hash'ini döndür."""
    password = "".join(random.choices(string.ascii_letters + string.digits, k=random.randint(8, 16)))
    password_hash= hashlib.md5(password.encode()).hexdigest()
    print(f"Oluşturulan Şifre: {password}, MD5 Hash: {password_hash}")  # Şifre ve hash'i yazdırır

    return password_hash

def verify_password(password):
    """Gönderilen şifreyi doğrula."""
    password_hash = hashlib.md5(password.encode()).hexdigest()
    with open("password.json", "r") as f:
        stored_password = json.load(f).get("password")
    return password_hash == stored_password
