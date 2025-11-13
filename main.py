import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Escribe 1 para ver el menú.")

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "1":
        await update.message.reply_text("Pizza $10\nHamburguesa $8")
    else:
        await update.message.reply_text("Escribe 1 para el menú.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))
    app.run_polling()

if __name__ == "__main__":
    main()
