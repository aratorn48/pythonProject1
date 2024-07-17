def send_email(message,  recipient,  sender = "university.help@gmail.com"):
    true_sfx = [".com", ".ru", ".net"]
    def true_email(email_address):
        return "@" in email_address and any(email_address.endswith(suffix) for suffix in true_sfx)

    if not true_email(sender) or not true_email(recipient):
        print("Невозможно отправить письмо с адреса", sender, "на адрес",  recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')