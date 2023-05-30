from telebot import TeleBot, types

from tgBot.functions.BadWordsChecker import have_bad_words

class BotFuncs:
    def menu(self, message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        workers = types.KeyboardButton('Работникам')
        parents = types.KeyboardButton('Родителям')
        child = types.KeyboardButton('Детям')
        news = types.KeyboardButton('Новости')
        reviews = types.KeyboardButton('Обратная связь')
        prop = types.KeyboardButton('Вакансии')
        markup.add(workers, parents, child, news, reviews, prop)
        bot.send_message(message.chat.id, 'Выбери раздел:', reply_markup=markup)

    def parent_btns(self, message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item1 = types.KeyboardButton('О сменах')
        item2 = types.KeyboardButton('Документы')
        item3 = types.KeyboardButton('Стоимость')
        item4 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Отлично, выбери пункт:', reply_markup=markup)


    def back_btn(self, message, bot):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item = types.KeyboardButton('Назад')
        markup.add(item)
        bot.send_message(message.chat.id, 'Напиши нам свой честный отзыв, критику или предложения!',
                         reply_markup=markup)

    # def back_request(self, message, bot, obj):
    #     first = message
    #     new_message = first.text
    #
    #     if message.chat.id == 621413330:
    #         if new_message == 'Назад' or new_message == 'назад':
    #             obj.menu(message, bot)
    #         elif have_bad_words(new_message.lower()) == True:
    #             # to_chat_id = '621413330'  # Я
    #             to_chat_id = '-1001554738139'  # Канал
    #             bot.forward_message(to_chat_id, message.chat.id, message.message_id)
    #             bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
    #             obj.menu(message, bot)
    #         else:
    #             bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
    #             obj.menu(message, bot)
    #     else:
    #         if new_message == 'Назад' or new_message == 'назад':
    #             obj.menu(message, bot)
    #         elif have_bad_words(new_message.lower()) == True:
    #             to_chat_id = '621413330'  # Я
    #             # to_chat_id = '-1001554738139'  # Канал
    #             bot.forward_message(to_chat_id, message.chat.id, message.message_id)
    #             bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
    #             obj.menu(message, bot)
    #         else:
    #             bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
    #             obj.menu(message, bot)

    def back_request(self, message, bot, obj):
        first = message
        new_message = first.text

        if message.chat.id == 621413330:
            if new_message == 'Назад' or new_message == 'назад':
                obj.menu(message, bot)
            elif have_bad_words(new_message.lower()) == True:
                # to_chat_id = '621413330'  # Я
                to_chat_id = '-1001554738139'  # Канал
                bot.forward_message(to_chat_id, message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
                obj.menu(message, bot)
            else:
                bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
                obj.menu(message, bot)
        else:
            if new_message == 'Назад' or new_message == 'назад':
                obj.menu(message, bot)
            elif have_bad_words(new_message.lower()) == True:
                to_chat_id = '621413330'  # Я
                # to_chat_id = '-1001554738139'  # Канал
                bot.forward_message(to_chat_id, message.chat.id, message.message_id)
                bot.send_message(message.chat.id, 'Спасибо за обраную связь!')
                obj.menu(message, bot)
            else:
                bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
                obj.menu(message, bot)