SECRET_KEY = "AKIA1234567890EXAMPLE"
encrypted_secret_key = SECRET_KEY[:4] + (len(SECRET_KEY) - 4) * "*"
print(encrypted_secret_key)
