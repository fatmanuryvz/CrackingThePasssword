import hashlib
import itertools
import string


def brute_force_md5(md5_hash, max_length=8):
    """Brute-force yöntemiyle MD5 hash'ini kır ve deneme sayısını yazdır."""
    characters = string.ascii_letters + string.digits + string.punctuation
    attempt_count = 0  # Deneme sayacı

    for length in range(1, max_length + 1):
        print(f"{length} karakter uzunluğundaki kombinasyonlar deneniyor...")  # Hangi uzunlukta olduğumuzu gösterir
        for guess in itertools.product(characters, repeat=length):
            attempt_count += 1  # Her denemede artır
            guess = ''.join(guess)
            if hashlib.md5(guess.encode()).hexdigest() == md5_hash:
                print(f"Şifre {attempt_count}. denemede bulundu: {guess}")
                return guess

    print(f"Şifre bulunamadı. Toplam deneme: {attempt_count}")
    return None
