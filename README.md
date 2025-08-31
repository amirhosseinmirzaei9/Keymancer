# 🔐 Keymancer
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)
![Status](https://img.shields.io/badge/status-active-brightgreen)

Keymancer is a Streamlit-based password and security key generator with a user-friendly interface. It supports generating random passwords, PINs, and passphrases . The application leverages Python's `secrets` module for cryptographically secure random generation and includes batch generation and CSV export capabilities.

## ✨ Features

- **Multiple Generator Types**:
  - 🔑 **Random Password**: Generate passwords with customizable length, character sets (uppercase, lowercase, digits, symbols).
  - 🔢 **PIN**: Generate numeric PINs with adjustable length.
  - 🧠 **Passphrase**: Generate mnemonic-based passphrases with customizable word count and separator, using the `mnemonic` library.

- **Batch Generation**: Generate multiple passwords/keys in one go (up to 1000).
- **Secure Generation**: Uses `secrets` for cryptographically secure random selection.
- 📄 **CSV Export**: Download generated passwords with timestamps in CSV format.
- 🙈 **Masked Display**: Option to mask passwords in the UI for added privacy.
- **Responsive UI**: Built with Streamlit for an intuitive and interactive experience.

## 🧙‍♂️ Why Keymancer?
Keymancer isn’t just another password generator — it’s a wizard 🧙‍♂️ that gives you secure, customizable, and exportable keys with a touch of magic.


## 🚀 Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd keymancer
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `streamlit`
   - `mnemonic`

3. **Run the Application**:
   ```bash
   streamlit run keymancer.py
   ```

## Usage

1. Open the application in your browser (Streamlit will provide the URL, typically `http://localhost:8501`).
2. Select the generator type (Random, PIN, or Passphrase) from the dropdown.
3. Configure the options:
   - For **Random**: Adjust length and character set preferences or provide a custom character set.
   - For **PIN**: Set the desired length.
   - For **Passphrase**: Choose the number of words and separator.
4. Specify the batch size for generating multiple passwords.
5. Click **Generate** to create passwords.
6. View results in the UI (optionally masked) and download them as a CSV file.

## 🔐 Security Notes

- **Cryptographic Security**: The application uses Python's `secrets` module for secure random generation, suitable for cryptographic purposes.
- **Sensitive Data**: ⚠️ Never share or store generated passwords in public or unsecured environments.
- **Local Execution**: Ensure the application runs in a secure environment, as generated keys are sensitive.

## 📦 File Structure

- `keymancer.py`: Main application script containing the password generation logic and Streamlit UI.
- `requirements.txt`: List of required Python packages.

## Dependencies

- Python 3.10+
- Streamlit (`pip install streamlit`)
- Mnemonic (`pip install mnemonic`)

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🤝 Contributing

Contributions are welcome! Please submit a pull request or open an issue for bug reports, feature requests, or suggestions.

## ⚠️ Disclaimer

Use this tool responsibly. The authors are not liable for any misuse or security breaches resulting from improper handling of generated passwords.