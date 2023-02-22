import telegram
import openai
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


openai.api_key = "TU_CLAVE_DE_ACCESO_DE_OPENAI"

def handle_messages(update, context):
    # Obtiene el ID del chat al que se envió el mensaje
    chat_id = update.effective_chat.id
    # Obtiene el contenido del mensaje
    message = update.message.text
    
    # Utiliza ChatGPT para generar una respuesta automática al mensaje recibido
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message}\n",
        max_tokens=2048,
        temperature=0.5,
    ).get("choices")[0].get("text")
    
    # Envía la respuesta generada al chat
    context.bot.send_message(chat_id, response)

# Establece filtros a los mensajes nuevos
chat_handler = MessageHandler(Filters.text & (~Filters.command), handle_messages)

if __name__== "__main__":

	updater = Updater(token="TOKEN_TELEGRAM")

	dispatcher = updater.dispatcher
	dispatcher.add_handler(chat_handler)

	updater.start_polling()


