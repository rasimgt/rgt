import telebot;
bot = telebot.TeleBot('7239840132:AAES-Q82uIqGgSxK5ekglgI-iDnZAi53eK0'); #тут токен бота
@bot.message_handler(content_types=['text']) #слушаем бота
def get_text(message):
    if message.text == "Привет": #проверям сообщение от пользователя
        bot.send_message(message.from_user.id, "Здравствуй, мой дорогой друг!") #отвечаем пользователю
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "напиши: Привет")
    else:
        bot.send_message(message.from_user.id, "я тебя не понимаю, напиши '/help'")
bot.polling(none_stop=True, interval=0)# бот постоянно будет опрашивает сервер