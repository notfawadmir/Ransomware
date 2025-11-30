
# 📄 **README.md — Ransomware**

```md
# Ransomware  
A simple educational ransomware simulation written in Python.  
This project demonstrates basic file encryption and decryption using the **Fernet** module from the `cryptography` library.

> ⚠️ **Educational Use Only**  
> This repository is intended strictly for learning purposes.  
> Do not deploy this code on systems you do not own or have explicit permission to test.  
> Misuse can lead to legal consequences.

---

## 🚀 Features
- File encryption using **Fernet (AES-128-CBC + HMAC)**  
- Appends `.enc` extension to encrypted files  
- Restores original filenames on decryption  
- Prevents key overwriting  
- Avoids double encryption  
- Works entirely offline  

---

## 📁 Repository Structure
```

Ransomware/
│
├── ransomware.py      # Encrypts files → filename.ext.enc
├── decrypt.py      # Decrypts files → restores original name
├── secret.key      # Encryption key (generated once)
├── README.md       # Documentation
└── (your files...) # Files that will be encrypted/decrypted

````

---

## 🔑 Requirements

Install dependencies:

```bash
pip install cryptography
````

---

## 🔒 How Encryption Works

Run:

```bash
python3 ransomware.py
```

Behavior:

* Generates `secret.key` (if not present)
* Encrypts all files in the directory, except excluded ones
* Writes output as `filename.ext.enc`
* Deletes the original unencrypted file

Example:

```
notes.txt → notes.txt.enc
```

---

## 🔓 How Decryption Works

Run:

```bash
python3 decrypt.py
```

Behavior:

* Loads `secret.key`
* Decrypts every `.enc` file in the directory
* Restores original filename by removing `.enc`
* Deletes the encrypted file

Example:

```
notes.txt.enc → notes.txt
```

---

## 📌 Excluded Files

The following files are automatically ignored during encryption/decryption:

```
README.md
ransomware.py
decrypt.py
secret.key
```

---

## ⚠️ Legal Disclaimer

This project is intended **only for cybersecurity education and research**.
Running this code on devices without permission is illegal.

You are solely responsible for how you use this tool.

---

## 🤝 Contributing

Contributions and improvements are welcome.
Feel free to fork the repo and submit a pull request.

---

## 📬 Contact

**GitHub:** [notfawadmir](https://github.com/notfawadmir)
**Email:** [fawadmeer000@gmail.com](mailto:fawadmeer000@gmail.com)

---

## ⭐ Support

If you found this useful, please ⭐ star the repository!

```
 

Just tell me.
```
