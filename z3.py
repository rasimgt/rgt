import telebot
bot = telebot.TeleBot('7239840132:AAES-Q82uIqGgSxK5ekglgI-iDnZAi53eK0')  # здесь ваш токен
@bot.message_handler(content_types=['text'])  # слушаем текстовые сообщения
def get_text(message):
    if message.text == "Привет!":  # проверяем сообщение от пользователя
        bot.send_message(message.chat.id, "Здравствуй, мой дорогой друг!")  # отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.chat.id, "напиши: Привет")
    else:
        bot.send_message(message.chat.id, "я тебя не понимаю, напиши '/help'")

bot.polling(none_stop=True, interval=0)  # бот постоянно будет опрашивать сервер