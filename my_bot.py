import telebot;
import webbrowser

bot = telebot.TeleBot('7935685520:AAGE8Ov2jk4vakLFHGE20YL3W-uAZ2xrn88')

y_data = 0



"""@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://onixschool.ru/')"""

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Давай знакомится! Я rBot. Я умею отгадывать дни рождения. Ты готов?')

@bot.message_handler(content_types=['text'])
def action_1(message):
    if message.text.lower() == 'да':
        bot.send_message(message.chat.id, 'Умножай дату рождения на 2. Потом к полученному числу прибавь 5. Результат умножай на 50. К полученному числу прибавляй месяц рождения. Результат отправь мне.')
    bot.register_next_step_handler(message, action_2)

@bot.message_handler(content_types=['text'])
def action_2(message):
    global y_data
    y_data = message.text
    y_data = int(y_data)
    y_data = y_data - 250
    age = y_data // 100
    mo = y_data % 100
    if mo == 1:
        moth = 'январь'
    elif mo == 2:
        moth = 'февраль'
    elif mo == 3:
        moth = 'март'
    elif mo == 4:
        moth = 'апрель'
    elif mo == 5:
        moth = 'май'
    elif mo == 6:
        moth = 'июнь'
    elif mo == 7:
        moth = 'июль'
    elif mo == 8:
        moth = 'август'
    elif mo == 9:
        moth = 'сентябрь'
    elif mo == 10:
        moth = 'октябрь'
    elif mo == 11:
        moth = 'ноябрь'
    else:
        moth = 'декабрь'
    bot.send_message(message.chat.id, f'Дата Вашего рождения {y_data // 100} {moth}')
    bot.register_next_step_handler(message, main)


"""@bot.message_handler()  
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.message_handler()
def send_age(message):
    bot.send_message(message_chat.id, 'В каком году ты родился(-ась)?')"""

#bot.polling(none_stop=True)
bot.polling(none_stop=True, interval=0)