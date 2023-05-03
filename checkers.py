from terms import database, items


def read_language(message):
    if message.text == "Русский":
        database[message.chat.id]['language'] = 'RU'
        return True
    elif message.text == "English":
        database[message.chat.id]['language'] = 'EN'
        return True
    elif message.text == "Український":
        database[message.chat.id]['language'] = 'UA'
        return True
    elif message.text == "中文":
        database[message.chat.id]['language'] = 'CN'
        return True
    elif message.text == "Français":
        database[message.chat.id]['language'] = 'FR'
        return True
    else:
        return False


def check_age(message):
    text = message.text
    try:
        int(text)
        return True
    except:
        return False


def check_bottoms(message):
    for i in range(1, 7):
        if message.text == items[f'variant_{i}']:
            database[message.chat.id]['question_7'] = message.text
            return True
    return False
