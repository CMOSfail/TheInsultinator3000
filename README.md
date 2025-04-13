# The Insultinator 3000

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Unleash the power of personalized, printable insults with The Insultinator 3000!** This Telegram bot is your go-to solution for playfully roasting your friends (or enemies) with custom-generated PDF insults.

## 🚀 Features

* **Personalized Insults:** Generate unique, humorous insults tailored to the target's name.
* **PDF Delivery:** Receive insults as clean, printable PDF documents.
* **Easy Telegram Integration:** Simply use the `/mock <name>` command to get started.
* **Environment Variable Security:** Keeps your Telegram bot token safe using a `.env` file.
* **Automatic PDF Cleanup:** PDFs are deleted after being sent, ensuring a clean file system.

## 🛠️ Prerequisites

* Python 3.6+
* Telegram Bot Token (obtained from [BotFather](https://t.me/BotFather))

## 📦 Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/CMOSfail/The-Insultinator-3000.git](https://github.com/CMOSfail/The-Insultinator-3000.git)
    cd The-Insultinator-3000
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**

    Copy the `.env.example` file to `.env` and replace `"YOUR_BOT_TOKEN"` with your actual Telegram bot token:

    ```bash
    cp .env.example .env
    ```

    Then edit the .env file with your token.

    ```
    TELEGRAM_BOT_TOKEN="YOUR_BOT_TOKEN"
    ```

    **Important:** Replace `"YOUR_BOT_TOKEN"` with your actual bot token.

4.  **Run the bot:**

    ```bash
    python bot.py
    ```

## 🎮 Usage

1.  Start a chat with your Telegram bot.
2.  Use the `/mock <name>` command to generate a personalized insult PDF.

    **Example:** `/mock John`

## 🤝 Contributing

Feel free to contribute to The Insultinator 3000! If you have any ideas for new features, insult templates, or improvements, please submit a pull request or open an issue.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🧑‍💻 Credits

* Created by Itamar - [CMOSfail](https://github.com/CMOSfail)

## ⚠️ Disclaimer

This bot is intended for humorous purposes only. Please use it responsibly and avoid generating insults that could be genuinely hurtful or offensive.
