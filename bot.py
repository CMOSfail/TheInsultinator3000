"""
Telegram bot for generating and sending insult PDFs using .env for token.
"""

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from insult_generator.generator import generate_insult
from pdf_generator.pdf_maker import create_insult_pdf
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


async def mock(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /mock command. Generates an insult and sends it as a PDF.
    """
    name = ' '.join(context.args)
    if not name:
        await update.message.reply_text("Please provide a name. Use /mock <name>")
        return

    try:
        insult = generate_insult(name)
        pdf_path = create_insult_pdf(name, insult)

        # Send the PDF
        with open(pdf_path, 'rb') as pdf_file:
            await context.bot.send_document(chat_id=update.effective_chat.id, document=pdf_file)

        os.remove(pdf_path)  # Clean up

    except FileNotFoundError:
        await update.message.reply_text("Error generating PDF.")
    except Exception as e:
        print(f"Error: {e}")
        await update.message.reply_text("An unexpected error occurred.")


def main() -> None:
    """
    Starts the Telegram bot.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        print("Error: TELEGRAM_BOT_TOKEN not found in .env file.")
        return

    app = ApplicationBuilder().token(bot_token).build()
    app.add_handler(CommandHandler("mock", mock))

    print("TheInsultinator3000 is now running...")
    app.run_polling()


if __name__ == '__main__':
    main()
