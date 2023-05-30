from django.core.management.base import BaseCommand
from django.conf import settings

import time

from telebot import TeleBot

from tgBot.functions.work_with_db import Sender
from tgBot.functions.bot_func import BotFuncs

bot = TeleBot(token=settings.TOKEN)




@bot.message_handler(commands=['start'])
def start(message):
    obj = Sender(message, bot)
    bot_foo = BotFuncs(message, bot)

    user_id = message.from_user.id
    name = message.from_user.first_name

    obj.check_and_add_user(user_id, name)
    bot.send_message(message.chat.id, f'Здравствуй, {name}! \n \n' +

                     """Детское учреждение «Мир Детства» не стоит на месте, а активно продвигается в информационном пространстве. На этой ресурсной площадке мы сможем еще больше освещать самые яркие знаковые события из жизни детей на летних сменах, а также предоставить для вас исчерпывающую информацию о летнем отдыхе детей в нашем учреждении. Уверенны, что Ваша активность сделает нашу совместную работу полезной и содержательной!
                     
                     - с уважением, директор ЧУ ООД «Мир Детства», лауреат премии Губернатора Хабаровского края в области государственной молодёжной политики, Татьяна Степановна Колесникова.
                     
                     Больше информации на сайте https://mirdetstvakhv.ru""")

    time.sleep(1)

    bot_foo.menu()


@bot.message_handler()
def bot_massage(message):
    obj = Sender(message, bot)
    bot_foo = BotFuncs(message, bot)

    if message.text.lower() == 'работникам':

        obj.send_mes(1)
        bot.send_message(message.chat.id, 'Документы:')
        # docs for workers
        for n in range(2, 5):
            obj.send_doc(n)
    elif message.text.lower() == 'детям':
        obj.send_mes(5)
    elif message.text.lower() == 'вакансии':
        obj.send_mes(6)
    elif message.text.lower() == 'новости':
        obj.send_mes(7)
    elif message.text.lower() == 'родителям':
        obj.send_mes(8)
        bot_foo.parent_btns()
    elif message.text.lower() == 'о сменах':
        obj.send_mes(9)
        obj.send_doc(10)
    # docs for parents
    elif message.text.lower() == 'документы':
        for n in range(11, 17):
            obj.send_doc(n)
    elif message.text.lower() == 'стоимость':
        obj.send_doc(17)
    elif message.text.lower() == 'спам':
        obj.spam()
    elif message.text.lower() == 'назад':
        bot_foo.menu()
    elif message.text.lower() == 'обратная связь':

        bot_foo.back_btn()
        send = bot.send_message(message.chat.id, 'Если выбрал этот пункт по ошибке, нажми «Назад»')
        bot.register_next_step_handler(send, bot_foo.back_request)
    else:
        obj.send_mes(19, message, bot)


class Command(BaseCommand):
    help = 'Лагерный бот'
    # bot.polling(none_stop=True)
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(str(e))
