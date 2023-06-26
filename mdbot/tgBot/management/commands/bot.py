from django.core.management.base import BaseCommand
from django.conf import settings

import time
import logging

from telebot import TeleBot

from tgBot.functions.work_with_db import Sender
from tgBot.functions.bot_func import BotFuncs

bot = TeleBot(token=settings.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    obj = Sender(message, bot)
    bot_foo = BotFuncs(message, bot)


    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name}! \n \n' +

                     """Детское учреждение «Мир Детства» не стоит на месте, а активно продвигается в информационном пространстве. На этой ресурсной площадке мы сможем еще больше освещать самые яркие знаковые события из жизни детей на летних сменах, а также предоставить для вас исчерпывающую информацию о летнем отдыхе детей в нашем учреждении. Уверенны, что Ваша активность сделает нашу совместную работу полезной и содержательной!
                     
                     - с уважением, директор ЧУ ООД «Мир Детства», лауреат премии Губернатора Хабаровского края в области государственной молодёжной политики, Татьяна Степановна Колесникова.
                     
                     Больше информации на сайте https://mirdetstvakhv.ru""")

    time.sleep(1)
    obj.check_and_add_user(message)
    bot_foo.menu()


@bot.message_handler()
def bot_massage(message):
    obj = Sender(message, bot)
    bot_foo = BotFuncs(message, bot)

    text = message.text.lower()

    if text == 'работникам':

        obj.send_mes(1)
        bot.send_message(message.chat.id, 'Документы:')
        obj.send_doc(2, 5)
    elif text == 'детям':
        obj.send_mes(5)
    elif text == 'вакансии':
        obj.send_mes(6)
    elif text == 'новости':
        obj.send_mes(7)
    elif text == 'родителям':
        obj.send_mes(8)
        bot_foo.parent_btns()
    elif text == 'о сменах':
        obj.send_mes(9)
        obj.send_doc(10, 11)
    # docs for parents
    elif text == 'документы':
        obj.send_doc(11, 17)
    elif text == 'стоимость':
        obj.send_doc(17, 18)
    elif text == 'спам':
        obj.spam()
    elif text == 'назад':
        bot_foo.menu()
    elif text == 'обратная связь':
        bot_foo.back_btn()
        send = bot.send_message(message.chat.id, 'Если выбрал этот пункт по ошибке, нажми «Назад»')
        bot.register_next_step_handler(send, bot_foo.back_request)
    else:
        obj.send_mes(19, message, bot)


class Command(BaseCommand):
    help = 'Лагерный бот'

    def handle(self, *args, **options):
        while True:
            try:
                bot.polling(none_stop=True)
            except Exception as e:
                logging.exception(e)
