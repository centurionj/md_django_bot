from django.core.management.base import BaseCommand
from django.conf import settings

import time

from telebot import TeleBot, types
# from pathlib import Path

from tgBot.models import SendData, UserId
from tgBot.functions.work_with_db import Sender
from tgBot.functions.bot_func import BotFuncs
from tgBot.functions.BadWordsChecker import have_bad_words

bot = TeleBot(token=settings.TOKEN)

# def back_request(message):
#     first = message
#     new_message = first.text
#
#     if message.chat.id == 621413330:
#         if new_message == 'Назад' or new_message == 'назад':
#             bot_foo.menu(message, bot)
#         elif have_bad_words(new_message.lower()) == True:
#             # to_chat_id = '621413330'  # Я
#             to_chat_id = '-1001554738139'  # Канал
#             bot.forward_message(to_chat_id, message.chat.id, message.message_id)
#             bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
#             bot_foo.menu(message, bot)
#         else:
#             bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
#             bot_foo.menu(message, bot)
#     else:
#         if new_message == 'Назад' or new_message == 'назад':
#             bot_foo.menu(message, bot)
#         elif have_bad_words(new_message.lower()) == True:
#             to_chat_id = '621413330'  # Я
#             # to_chat_id = '-1001554738139'  # Канал
#             bot.forward_message(to_chat_id, message.chat.id, message.message_id)
#             bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
#             bot_foo.menu(message, bot)
#         else:
#             bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
#             bot_foo.menu(message, bot)

obj = Sender()
bot_foo = BotFuncs()

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    name = message.from_user.first_name

    obj.check_and_add_user(user_id, name)
    bot.send_message(message.chat.id, f'Здравствуй, {name}! \n \n' +

                     """Детское учреждение «Мир Детства» не стоит на месте, а активно продвигается в информационном пространстве. На этой ресурсной площадке мы сможем еще больше освещать самые яркие знаковые события из жизни детей на летних сменах, а также предоставить для вас исчерпывающую информацию о летнем отдыхе детей в нашем учреждении. Уверенны, что Ваша активность сделает нашу совместную работу полезной и содержательной!
                     
                     - с уважением, директор ЧУ ООД «Мир Детства», лауреат премии Губернатора Хабаровского края в области государственной молодёжной политики, Татьяна Степановна Колесникова.
                     
                     Больше информации на сайте https://mirdetstvakhv.ru""")

    time.sleep(1)

    bot_foo.menu(message, bot)


@bot.message_handler()
def bot_massage(message):
    if message.text.lower() == 'работникам':

        obj.send_mes(1, message, bot)
        bot.send_message(message.chat.id, 'Документы:')
        # docs for workers
        for n in range(2, 5):
            obj.send_doc(n, message, bot)
    elif message.text.lower() == 'детям':
        obj.send_mes(5, message, bot)
    elif message.text.lower() == 'вакансии':
        obj.send_mes(6, message, bot)
    elif message.text.lower() == 'новости':
        obj.send_mes(7, message, bot)
    elif message.text.lower() == 'родителям':
        obj.send_mes(8, message, bot)
        bot_foo.parent_btns(message, bot)
    elif message.text.lower() == 'о сменах':
        obj.send_mes(9, message, bot)
        obj.send_doc(10, message, bot)
    # docs for parents
    elif message.text.lower() == 'документы':
        for n in range(11, 17):
            obj.send_doc(n, message, bot)
    elif message.text.lower() == 'стоимость':
        obj.send_doc(17, message, bot)
    elif message.text.lower() == 'спам':
        obj.spam(bot)
    elif message.text.lower() == 'назад':
        bot_foo.menu(message, bot)
    elif message.text.lower() == 'обратная связь':

        bot_foo.back_btn(message, bot)
        send = bot.send_message(message.chat.id, 'Если выбрал этот пункт по ошибке, нажми «Назад»')
        bot.register_next_step_handler(send, bot_foo.back_request(message, bot, bot_foo))
    else:
        obj.send_mes(19, message, bot)


class Command(BaseCommand):
    help = 'Лагерный бот'
    bot.polling(none_stop=True)

    # while True:
    #     try:
    #         bot.polling(none_stop=True)
    #     except:
    #         print('bolt')