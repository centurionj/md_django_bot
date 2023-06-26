import logging

from tgBot.models import SendData, UserId

from pathlib import Path
import telebot


class Sender:
    def __init__(self, message, bot):
        self.message = message
        self.bot = bot

    def send_mes(self, id: int):
        data = SendData.objects.filter(id=id)
        for d in data:
            s = f"\n{d.text}\n\n"
            try:
                media = d.file.file
                if Path(f'{media}').suffix.lower() in ['.mp4', '.mov', '.docx', '.pdf']:
                    self.bot.send_document(self.message.chat.id, media, caption=s)
                else:
                    self.bot.send_photo(self.message.chat.id, media, caption=s)
            except Exception as e:
                logging.exception(e)
                self.bot.send_message(self.message.chat.id, s)

    def send_doc(self, start, stop):
        file_paths = []
        for n in range(start, stop):
            data = SendData.objects.filter(id=n)
            for d in data:
                try:
                    media = d.file.file
                    file_paths.append(telebot.types.InputMediaDocument(open(Path(f'{media}'), 'rb')))
                except Exception as e:
                    logging.exception(e)
        self.bot.send_media_group(self.message.chat.id, file_paths)

    def spam(self):
        users = UserId.objects.all()
        spam = SendData.objects.filter(description='спам')

        for user in users:
            to_chat_id = user.user_id
            for sp in spam:
                s = f"\n{sp.text}\n\n"
                try:
                    with open(f'{sp.file.file}', 'rb') as file:
                        if Path(f'{sp.file.file}').suffix.lower() == '.docx':
                            self.bot.send_document(to_chat_id, file, caption=s)
                        elif Path(f'{sp.file.file}').suffix.lower() == '.mp4' \
                                or Path(f'{file}').suffix.lower() == '.mov':
                            self.bot.send_video(to_chat_id, file, caption=s)
                        else:
                            self.bot.send_photo(to_chat_id, file, caption=s)
                except Exception as e:
                    logging.exception(e)
                    self.bot.send_message(to_chat_id, s)

    def check_and_add_user(self, message):
        user_id = message.from_user.id
        name = message.from_user.first_name
        try:
            user = UserId.objects.get(user_id=user_id)
            s = "Вы уже добавлены в базу данных для рассылок."
            self.bot.send_message(self.message.chat.id, s)
        except UserId.DoesNotExist:

            new_user = UserId(user_id=user_id, name_from_tg=name)
            new_user.save()
            s = "Вы успешно добавлены в базу данных для рассылок."
            self.bot.send_message(self.message.chat.id, s)
