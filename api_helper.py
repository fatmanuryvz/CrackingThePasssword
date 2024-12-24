import requests


def get_md5_hash(url):
    """API'den MD5 hash'i al."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("password")
    return None


def post_password(url, password):
    """Doğrulama için şifreyi POST isteğiyle gönder."""
    response = requests.post(url, json={"password": password})
    if response.status_code == 200:
        return response.json().get("message") == "Success"
    return False
