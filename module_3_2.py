def str_check (text:str): # функция проверки адреса отправителя/получателя на корректность
    variants = (".com", ".ru", ".net")
    if "@" in text and text.endswith(variants):
        return True
    else:
        return False

def send_email(message:str, recipient:str, sender = "university.help@gmail.com"):
    if not str_check(recipient) or not str_check(sender):
        print(f"Невозможно отправить письмо с адреса {sender} oна адрес {recipient}")
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} oна адрес {recipient}")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
