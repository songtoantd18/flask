from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("7194002941:AAHZscwofpuDVoTl_xAvJNlrqllpx4c2TlY").build()
print(app)

app.add_handler(CommandHandler("hello", hello))

app.run_polling()