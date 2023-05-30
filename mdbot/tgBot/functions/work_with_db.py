from tgBot.models import SendData, UserId

from pathlib import Path


class Sender:
    def send_mes(self, id: int, message, bot):
        data = SendData.objects.filter(id=id)
        for d in data:
            s = f"\n{d.text}\n\n"
            try:
                media = d.file.file
                if Path(f'{media}').suffix.lower() == '.mp4' or Path(f'{media}').suffix == '.mov' \
                        or Path(f'{media}').suffix == '.pdf' or Path(f'{media}').suffix == '.docx':
                    bot.send_document(message.chat.id, media, caption=s)
                else:
                    bot.send_photo(message.chat.id, media, caption=s)
            except Exception as e:
                print(e)
                bot.send_message(message.chat.id, s)

    def send_doc(self, id: int, message, bot):
        data = SendData.objects.filter(id=id)
        for d in data:
            try:
                media = d.file.file
                if Path(f'{media}').suffix == '.pdf' or Path(f'{media}').suffix == '.docx':
                    bot.send_document(message.chat.id, media)
            except Exception as e:
                print(e)

    def spam(self, bot):
        users = UserId.objects.all()
        spam = SendData.objects.filter(description='спам')

        for user in users:
            to_chat_id = str(user.user_id)
            for sp in spam:
                s = f"\n{sp.text}\n\n"
                try:
                    media = sp.file.file
                    if Path(f'{media}').suffix.lower() == '.mp4' or Path(f'{media}').suffix == '.mov' \
                            or Path(f'{media}').suffix == '.pdf' or Path(f'{media}').suffix == '.docx':
                        bot.send_document(to_chat_id, media, caption=s)
                    else:
                        bot.send_photo(to_chat_id, media, caption=s)
                except Exception as e:
                    print(e)
                    bot.send_message(to_chat_id, s)

    def check_and_add_user(self, user_id, name):
        try:
            user = UserId.objects.get(user_id=user_id)
            print("Пользователь уже существует в базе данных.")
        except UserId.DoesNotExist:

            new_user = UserId(user_id=user_id, name_from_tg=name)
            new_user.save()
            print("Пользователь успешно добавлен в базу данных.")