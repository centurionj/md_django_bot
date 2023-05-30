from telebot import types

from tgBot.functions.BadWordsChecker import have_bad_words

class BotFuncs:
    def __init__(self, message, bot):
        self.message = message
        self.bot = bot

    def menu(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        workers = types.KeyboardButton('Работникам')
        parents = types.KeyboardButton('Родителям')
        child = types.KeyboardButton('Детям')
        news = types.KeyboardButton('Новости')
        reviews = types.KeyboardButton('Обратная связь')
        prop = types.KeyboardButton('Вакансии')
        markup.add(workers, parents, child, news, reviews, prop)
        self.bot.send_message(self.message.chat.id, 'Выбери раздел:', reply_markup=markup)

    def parent_btns(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item1 = types.KeyboardButton('О сменах')
        item2 = types.KeyboardButton('Документы')
        item3 = types.KeyboardButton('Стоимость')
        item4 = types.KeyboardButton('Назад')
        markup.add(item1, item2, item3, item4)
        self.bot.send_message(self.message.chat.id, 'Отлично, выбери пункт:', reply_markup=markup)

    def back_btn(self):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        item = types.KeyboardButton('Назад')
        markup.add(item)
        self.bot.send_message(self.message.chat.id, 'Напиши нам свой честный отзыв, критику или предложения!',
                         reply_markup=markup)

    def back_request(self):
        first = self.message
        new_message = first.text

        if self.message.chat.id == 621413330:
            if new_message == 'Назад' or new_message == 'назад':
                self.menu()
            elif have_bad_words(new_message.lower()):
                # to_chat_id = '621413330'  # Я
                to_chat_id = '-1001554738139'  # Канал
                self.bot.forward_message(to_chat_id, self.message.chat.id, self.message.message_id)
                self.bot.send_message(self.message.chat.id, 'Спасибо за обратную связь!')
                self.menu()
            else:
                self.bot.send_message(self.message.chat.id, f'Ай-ай-ай, {self.message.from_user.first_name}, как не стыдно?')
                self.menu()
        else:
            if new_message == 'Назад' or new_message == 'назад':
                self.menu()
            elif have_bad_words(new_message.lower()):
                to_chat_id = '621413330'  # Я
                # to_chat_id = '-1001554738139'  # Канал
                self.bot.forward_message(to_chat_id, self.message.chat.id, self.message.message_id)
                self.bot.send_message(self.message.chat.id, 'Спасибо за обратную связь!')
                self.menu()
            else:
                self.bot.send_message(self.message.chat.id, f'Ай-ай-ай, {self.message.from_user.first_name}, как не стыдно?')
                self.menu()