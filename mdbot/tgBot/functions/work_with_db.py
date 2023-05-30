from tgBot.models import SendData, UserId

from pathlib import Path


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
                print(e)
                self.bot.send_message(self.message.chat.id, s)

    def send_doc(self, id: int):
        data = SendData.objects.filter(id=id)
        for d in data:
            try:
                media = d.file.file
                if Path(f'{media}').suffix in ['.pdf', '.docx']:
                    self.bot.send_document(self.message.chat.id, media)
            except Exception as e:
                print(e)

    def spam(self):
        users = UserId.objects.all()
        spam = SendData.objects.filter(description='спам')

        for user in users:
            to_chat_id = str(user.user_id)
            for sp in spam:
                s = f"\n{sp.text}\n\n"
                try:
                    media = sp.file.file
                    if Path(f'{media}').suffix.lower() in ['.mp4', '.mov', '.docx']:
                        self.bot.send_document(to_chat_id, media, caption=s)
                    else:
                        self.bot.send_photo(to_chat_id, media, caption=s)
                except Exception as e:
                    print(e)
                    self.bot.send_message(to_chat_id, str(e))

    def check_and_add_user(self, user_id, name):
        try:
            user = UserId.objects.get(user_id=user_id)
            print("Пользователь уже существует в базе данных.")
        except UserId.DoesNotExist:

            new_user = UserId(user_id=user_id, name_from_tg=name)
            new_user.save()
            print("Пользователь успешно добавлен в базу данных.")
