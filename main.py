import json
import telebot
from AstroCollector import Horoscope


template_route = 'templates/text.json'

with open('token.txt','r') as tk:
    token = tk.readline()



with open (template_route,'r',encoding='UTF8') as text:
    loaded_template_file = json.load(text)


bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['Start','Hello','start','hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, loaded_template_file['start'], reply_markup=markup)


markup = telebot.types.InlineKeyboardMarkup(row_width=2)
itembtnaries = telebot.types.InlineKeyboardButton('Овен' + '♈',callback_data = 'aries') #1
itembtntaurus = telebot.types.InlineKeyboardButton('Телец' + '♉', callback_data = 'taurus') #2
itembtngemini = telebot.types.InlineKeyboardButton('Близнецы' + '♊', callback_data = 'gemini') #3
itembtncancer = telebot.types.InlineKeyboardButton('Рак' + '♋', callback_data = 'cancer') #4
itembtnleo = telebot.types.InlineKeyboardButton('Лев' + '♌', callback_data = 'leo') #5
itembtnvirgo = telebot.types.InlineKeyboardButton('Дева' + "♍", callback_data = 'virgo') #6
itembtnlibra = telebot.types.InlineKeyboardButton('Весы' + '♎', callback_data = 'libro') #7
itembtnscorpio = telebot.types.InlineKeyboardButton('Скорпион' + '♏', callback_data = 'scorpio') #8
itembtnsagittarius = telebot.types.InlineKeyboardButton('Стрелец' + '♐', callback_data = 'sagittarius') #9
itembtncapricron = telebot.types.InlineKeyboardButton('Козерог' + '♑', callback_data ='capricron') #10
itembtnaquarius = telebot.types.InlineKeyboardButton('Водолей' + '♒', callback_data ='aquarius') #11
itembtnpisces = telebot.types.InlineKeyboardButton('Рыбы' + '♓', callback_data ='pisces') #12
markup.row(itembtnaries,itembtntaurus, itembtngemini,itembtncancer)
markup.row(itembtnleo, itembtnvirgo, itembtnlibra, itembtnscorpio )
markup.row(itembtnsagittarius,itembtncapricron,itembtnaquarius,itembtnpisces)


@bot.callback_query_handler(func= lambda call: True)
def get_text(call):
    mark = call.data
    zodiac = Horoscope(mark=mark)
    bot.send_message(call.message.chat.id, zodiac.get_predict()[mark])



@bot.message_handler(commands=['key','keyboard'])
def get_keyboard(message):
    bot.send_message(message.chat.id, loaded_template_file['key'], reply_markup=markup)

# zodiacs = ('aries', 'taurus', 'gemini', 'cancer','leo', 'virgo',
#            'libra', 'scorpio', 'sagittarius','capricorn', 'aquarius',
#            'pisces')


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
