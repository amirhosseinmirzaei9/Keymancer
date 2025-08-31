# 🔑 Keymancer – The Ultimate Password Wizard 🧙‍♂️

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  


**Keymancer** is a **next-gen password & passphrase generator** designed to create secure, unique, and memorable credentials.  
It comes with both a **CLI tool** and a **modern web interface** powered by Streamlit.


## 🌍 Website  

🔗 Visit the official **Keymancer Website** here:  
👉 [https://keymancer.streamlit.app](https://keymancer.streamlit.app)  

No installation needed — everything runs directly in your browser.


## ✨ Features

- 🔐 Generate **random passwords** with flexible rules
- 🔢 Create secure **numeric PINs**
- 📖 Build **multi-language passphrases** (English, French, Japanese, and more)
- ⚡ Batch generation (hundreds of credentials at once)
- 📂 Export results as **CSV or JSON**
- 📋 Copy the first result directly to your clipboard (CLI)
- 💡 Daily **security tips** in the Web UI
- 🛡️ Privacy-first, open-source, modular design


## 🚀 Installation

### 1. Clone the repository

```sh
git clone https://github.com/your-username/keymancer.git
cd keymancer
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

Dependencies include: `streamlit`, `click`, `rich`, `mnemonic`, `pyperclip`


## 🖥️ Usage

### 🔹 Web Interface (Streamlit)

```sh
streamlit run keymancer_ui.py
```

➡ Open your browser at [http://localhost:8501](http://localhost:8501)

**Features in Web UI:**

- Select between **Random Password / PIN / Passphrase**
- Customize parameters (length, symbols, word count, etc.)
- Batch generation & CSV download
- Security tips sidebar


### 🔹 Command Line Interface (CLI)

```sh
python keymancer_cli.py [COMMAND] [OPTIONS]
```

#### Available Commands:

**Random Passwords**

```sh
python keymancer_cli.py random --length 20 --no-symbols --batch 3
```

**PINs**

```sh
python keymancer_cli.py pin --length 8 --batch 5 --copy
```

**Passphrases**

```sh
python keymancer_cli.py passphrase --words 5 --separator "_" --language english
```

#### Output Options:

- Default → Rich colored table
- Plain text → `--plain`
- JSON → `--json` or `--json-file results.json`


## 📂Project Structure

```
keymancer/
│── keymancer_core.py    # Core password generators
│── keymancer_cli.py     # CLI interface (Click + Rich)
│── keymancer_ui.py      # Web app (Streamlit)
│── keymancer_tips.py    # Security tips manager
│── tips.json            # Security tips data
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

## 🧩 Contributing

Want to improve **Keymancer**?

- Fork the repo → Make changes → Submit a Pull Request
- Add more password strategies to `keymancer_core.py`
- Expand `tips.json` with valuable security advice

Contributions are welcome ✨


## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.


## ⚠️ Disclaimer

This tool is intended for **personal and educational use**.  
The authors are **not responsible** for any misuse, security breaches, or damages caused by improper handling of generated credentials.