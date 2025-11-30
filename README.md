**Readme**
---

# 🔐 **Ransomware Simulation (Educational)**

A lightweight, fully offline **Python-based ransomware simulation** designed for learning file encryption, decryption, key management, and basic ransomware behavior using **Fernet** from the `cryptography` library.

> ⚠️ **For Educational & Research Use Only**
> This project must *only* be used in controlled environments on systems you own or have explicit permission to test.
> Unauthorized use is illegal and unethical.

---

## ✨ **Key Capabilities**

* 🔒 **Strong encryption** using Fernet (AES-128-CBC + HMAC)
* 📁 **Automatic file discovery**
* 🧩 **Prevents double-encryption**
* 🗝️ **Safe key handling** (no overwriting)
* 🔄 **Full decryption support**
* 📎 **Restores original filenames**
* 🏃 Works completely **offline**
* 🧼 Clean structure and beginner-friendly code

---

## 📂 **Project Structure**

```
Ransomware/
│
├── ransomware.py     # Encrypts: filename.ext → filename.ext.enc
├── decrypt.py        # Decrypts: filename.ext.enc → filename.ext
├── secret.key        # Generated once (stores the Fernet key)
├── README.md         # Documentation
│
└── (your files...)   # Any files you place here will be encrypted/decrypted
```

---

## 🛠️ **Installation**

Install dependencies:

```bash
pip install cryptography
```

---

## 🔒 **Encryption Process**

Run:

```bash
python3 ransomware.py
```

The script will:

* Generate `secret.key` if missing
* Load the Fernet key
* Scan the directory for encryptable files
* Encrypt them and append `.enc`
* Delete unencrypted originals

**Example:**

```
report.pdf → report.pdf.enc
```

---

## 🔓 **Decryption Process**

Run:

```bash
python3 decrypt.py
```

The script will:

* Load `secret.key`
* Find all `.enc` files
* Decrypt them
* Restore original names
* Remove encrypted versions

**Example:**

```
report.pdf.enc → report.pdf
```

---

## 🚫 **Files Automatically Excluded**

To avoid self-destruction and key loss:

```
README.md
ransomware.py
decrypt.py
secret.key
```

---

## ⚠️ **Legal Notice**

This repository exists **solely** for:

* Cybersecurity training
* Malware behavior analysis
* Classroom simulations
* Research & defensive development

Using this code on unauthorized systems is **a criminal offense**.
Responsibility lies entirely with the user.

---

## 🤝 **Contributing**

Got ideas or improvements?
Open an issue or submit a pull request — contributions are welcome.

---

## 📬 **Contact**

**GitHub:** [notfawadmir](https://github.com/notfawadmir)
**Email:** [fawadmeer000@gmail.com](mailto:fawadmeer000@gmail.com)

---

## ⭐ **Support the Project**

If this project helped you learn something new, consider giving it a **⭐ star**!

---

