from api_helper import get_md5_hash, post_password

if __name__ == "__main__":
    # 1. API'den MD5 hash'i al
    md5_hash = get_md5_hash("http://127.0.0.1:5000/get_password")
    print(f"Alınan MD5 Hash: {md5_hash}")


while True:
    if md5_hash:
        # 2. Kullanıcı tarafından tahmin edilen bir şifre
        user_password = input("Şifre tahmininizi girin: ")

        # 3. Şifreyi brute-force yöntemiyle kır veya kontrol et
        success = post_password("http://127.0.0.1:5000/check_password", user_password)

        if success:
            print("Şifre doğru!")
        else:
            print("Şifre yanlış!")
