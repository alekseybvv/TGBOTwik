import telebot, wikipedia, re
from telebot import types

bot = telebot.TeleBot('TOKEN')

wikipedia.set_lang("ru")

def getwiki(s):
    try:
        ny = wikipedia.page(s)

        wikitext=ny.content[:1000]

        wikimas=wikitext.split('.')

        wikimas = wikimas[:-1]

        wikitext2 = ''

        for x in wikimas:
            if not('==' in x):

                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break

        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2

    except Exception as e:
        return 'В энциклопедии нет информации об этом'


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Нажми меня')
    markup.add(item)
    bot.send_message(message.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
@bot.message_handler(func=lambda message: message.text == "Нажми меня")
def handle_button_click(message):
    user_query = message.text
    print(f'User clicked the button with text: {user_query}')

    result = getwiki(user_query)
    bot.send_message(message.chat.id, result)


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    result = getwiki(message.text)
    bot.send_message(message.chat.id, result)

bot.polling(none_stop=True, interval=0)