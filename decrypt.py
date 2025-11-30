#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet, InvalidToken

exclude = ["README.md", "License","ransomware.py", "secret.key", "decrypt.py", "encrypt.py"]

# Load the key
with open("secret.key", "rb") as kf:
    key = kf.read()

for file in os.listdir():
    if file in exclude:
        continue

    # Only decrypt .enc files
    if not file.endswith(".enc"):
        continue

    if os.path.isfile(file):
        with open(file, "rb") as f:
            encrypted_data = f.read()

        try:
            decrypted = Fernet(key).decrypt(encrypted_data)
        except InvalidToken:
            print(f"[!] InvalidToken: Wrong key or corrupted file → {file}")
            continue

        # remove the .enc extension
        original_name = file[:-4]
        with open(original_name, "wb") as f:
            f.write(decrypted)

        # delete encrypted file
        os.remove(file)

        print(f"Decrypted: {file} → {original_name}")

print("Decryption complete.")
