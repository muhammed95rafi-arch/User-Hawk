# UserHawk - Username Wordlist Generator 🔍

> Generate possible usernames from a person's name, phone digits & birth year



![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)




![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)




![Tool](https://img.shields.io/badge/Tool-OSINT-red?style=flat-square)



---

## 📌 What is this?

Given a person's **full name**, **last digits of mobile number**, and **birth year**,  
this tool generates a list of **possible usernames** they might be using on social media.

Works perfectly with **UserHawk** to search those usernames across 8 platforms!

---

## 🚀 Usage

```bash
python3 username_gen.py
The tool will ask:
[*] Enter full name         → Muhammed Rafi
[*] Last digits of mobile   → 4523
[*] Birth year (optional)   → 1995
📸 Output Example
1.  muhammed_rafi
  2.  muhammed_rafi4523
  3.  mrafi95
  4.  rafi.muhammed
  5.  m_rafi4523
  6.  realmuhammed
  7.  muh4mm3d_r4f1
  8.  muhammed_rafi_1995
  ...
[+] Total: 80+ usernames generated
⚡ Features
👤 Name combinations with separators ( _ . - )
📱 Phone last digits — 2, 3, 4 digit combos
📅 Birth year combinations
🤖 Leet speak variants ( a→4, e→3, i→1, o→0 )
💾 Save results to .txt file
🔗 Direct integration with UserHawk
🔗 Use with UserHawk
# Step 1 - Generate wordlist
python3 username_gen.py

# Step 2 - Search a username from the list
python3 userhawk.py <username>
🛠️ Installation
🐧 Linux / Kali / Parrot OS
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python3 username_gen.py
📱 Termux (Android)
pkg update && pkg install git python -y
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python3 username_gen.py
🪟 Windows
git clone https://github.com/muhammed95rafi-arch/UserHawk.git
cd UserHawk
python username_gen.py
🛠️ Requirements
Python 3.x
No external libraries needed
⚠️ Disclaimer
This tool is intended for educational and ethical OSINT purposes only.
Only use it on accounts you own or have permission to investigate.
The author is not responsible for any misuse.
👤 Author
muhammed95rafi-arch
Bug Bounty Hunter | Security Researcher
HackerOne Profile
📄 License
MIT License — Free to use and modify.
