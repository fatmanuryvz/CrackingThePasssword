from flask import Flask, request, jsonify
from utils import generate_password, verify_password
import json

app = Flask(__name__)


@app.route("/get_password", methods=["GET"])
def get_password():
    password_hash = generate_password()
    response = jsonify({"password": password_hash})
    with open("password.json", "w") as f:
        json.dump({"password": password_hash}, f)
    return response


@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password")
    is_valid = verify_password(password)
    print(f"Gelen Şifre: {password}")
    print(f"Doğrulama Sonucu: {'Başarılı' if is_valid else 'Başarısız'}")

    if is_valid:
        return jsonify({"message": "Success"})
    else:
        return jsonify({"message": "Failed"})

if __name__ == "__main__":
    app.run(port=5000)
