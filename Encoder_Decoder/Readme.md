# Python Email and Data Security Tool

A simple yet powerful command-line tool for encoding and decoding messages and securely sending them via email. This project demonstrates core Python skills in data manipulation, file handling, and email automation.

## ✨ Features

* **Custom Encoding/Decoding:** A unique algorithm is used to encrypt and decrypt text messages.

* **Secure Email Sending:** Utilizes the `smtplib` library to send messages securely over SMTP.

* **Persistent Credentials:** On the first run, the tool prompts the user for their email and app password. It then securely saves this information in a `config.py` file, so you never have to enter it again.

* **User-Friendly Interface:** A simple command-line interface guides the user through the process.

## 🚀 How to Use

### Prerequisites

* Python 3.x installed on your system.

* An email account with **2-Step Verification enabled** and a generated **App Password** for your Python script.

### Getting Started

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/ZohabFaiz/Projects.git
   cd Projects/Encoder_Decoder
   ```

2. Run the script from your terminal.

   ```bash
   python Encoder_Decoder.py
   ```

### First-Time Setup

* The first time you run the script, it will ask for your email and your app password.

* Enter your credentials, and the script will automatically create a `config.py` file to save them for future use.

**Note:** For security, it is highly recommended to add `config.py` to your `.gitignore` file to prevent your credentials from being uploaded to GitHub.

## 🧑‍💻 Author

* Zohab Faiz
