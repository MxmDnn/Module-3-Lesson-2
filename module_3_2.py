
def send_email(message, recipient, *, sender='university.help@gmail.com') :
    if ('@' and ('.com' or '.ru' or '.net') in (str(recipient) and str(sender))) is False :

    #if ('@') in (recipient and sender) and ('.com' or '.ru' or '.net') in (recipient and sender) is False :

    #if recipient.find('@' and '.com' or '.ru' or '.net') and sender.find('@' and '.com' or '.ru' or '.net') < 0 :
        print('Невозможно отправить письмо с адреса', str(sender), 'на адрес', str(recipient))

    elif recipient == sender :
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com' :
        print('Письмо успешно отправлено с адреса', str(sender), 'на адрес', str(recipient))
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', str(sender), 'на адрес', str(recipient))

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')