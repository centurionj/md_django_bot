from telebot import types

from tgBot.functions.BadWordsChecker import have_bad_words

class BotFuncs:
    def __init__(self, message, bot):
        self.message = message
        self.bot = bot

    def menu(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(
            types.KeyboardButton('Работникам'),
            types.KeyboardButton('Родителям'),
            types.KeyboardButton('Детям'),
            types.KeyboardButton('Новости'),
            types.KeyboardButton('Обратная связь'),
            types.KeyboardButton('Вакансии')
        )
        self.bot.send_message(self.message.chat.id, 'Выбери раздел:', reply_markup=markup)

    def parent_btns(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(
            types.KeyboardButton('О сменах'),
            types.KeyboardButton('Документы'),
            types.KeyboardButton('Стоимость'),
            types.KeyboardButton('Назад'),
        )
        self.bot.send_message(self.message.chat.id, 'Отлично, выбери пункт:', reply_markup=markup)

    def back_btn(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(
            types.KeyboardButton('Назад')
        )
        self.bot.send_message(self.message.chat.id, 'Напиши нам свой честный отзыв, критику или предложения!',
                         reply_markup=markup)

    def back_request(self, message):
        first = message
        new_message = first.text

        if message.chat.id == 621413330:
            if new_message.lower() == 'назад':
                self.menu()

            to_chat_id = '-1001554738139'  # Канал
            self.bot.forward_message(to_chat_id, message.chat.id, message.message_id)
            self.bot.send_message(message.chat.id, 'Спасибо за обратную связь!')
            self.menu()

        else:
            if new_message.lower() == 'назад':
                self.menu()
            elif have_bad_words(new_message.lower()):
                to_chat_id = '621413330'  # Я
                self.bot.forward_message(to_chat_id, message.chat.id, message.message_id)
                self.bot.send_message(self.message.chat.id, 'Спасибо за обратную связь!')
                self.menu()
            else:
                self.bot.send_message(message.chat.id, f'Ай-ай-ай, {message.from_user.first_name}, как не стыдно?')
                self.menu()