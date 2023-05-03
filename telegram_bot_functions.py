import telebot
from telebot import types
from terms import database, items, bot


def chose_language(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    button1 = types.KeyboardButton(text="Русский")
    button2 = types.KeyboardButton(text="English")
    button3 = types.KeyboardButton(text="Український")
    button4 = types.KeyboardButton(text="中文")
    button5 = types.KeyboardButton(text="Français")
    keyboard.add(button1, button2, button3, button4, button5)
    try:
        database[message.chat.id]
    except KeyError:
        database[message.chat.id] = {}
    bot.send_message(message.chat.id, "Choose your language:", reply_markup=keyboard)


def introduction(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, items[f'introduction_{language}'], reply_markup=keyboard)


def question_1(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    message_send = bot.send_message(message.chat.id, items[f'question_1_{language}'], reply_markup=keyboard)


def question_2(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'man_{language}'])
    btn2 = types.KeyboardButton(text=items[f'woman_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, items[f'question_2_{language}'], reply_markup=keyboard)


def question_3(message):
    language = database[message.chat.id]['language']
    bot.send_message(message.chat.id, items[f'question_3_{language}'])


def question_4(message):
    language = database[message.chat.id]['language']
    bot.send_message(chat_id=message.chat.id, text=items[f'question_4_{language}'])


def question_5(message):
    language = database[message.chat.id]['language']
    bot.send_message(chat_id=message.chat.id, text=items[f'question_5_{language}'])


def question_6(message):
    language = database[message.chat.id]['language']
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(items[f'children_{language}'], callback_data="children"),
               types.InlineKeyboardButton(items[f'disabled_person_{language}'], callback_data="invalids"),
               types.InlineKeyboardButton(items[f'siblings_{language}'], callback_data="parents"))
    markup.add(types.InlineKeyboardButton("✓", callback_data="done"))
    bot.send_message(chat_id=message.chat.id, text=items[f"question_6_{language}"], reply_markup=markup)


def check_question_6(message):
    language = database[message.chat.id]['language']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(chat_id=message.chat.id, text=items[f"check_question_{language}"], reply_markup=keyboard)


def question_7(message):
    database[message.chat.id]['select'] = question_6
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items['variant_1'])
    btn2 = types.KeyboardButton(text=items['variant_2'])
    btn3 = types.KeyboardButton(text=items['variant_3'])
    btn4 = types.KeyboardButton(text=items['variant_4'])
    btn5 = types.KeyboardButton(text=items['variant_5'])
    btn6 = types.KeyboardButton(text=items['variant_6'])
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, items[f'question_7_{language}'], reply_markup=keyboard)


def question_8(message):
    language = database[message.chat.id]['language']
    bot.send_message(message.chat.id, items[f'question_8_{language}'])


def question_9(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items['variant_1'])
    btn2 = types.KeyboardButton(text=items['variant_2'])
    btn3 = types.KeyboardButton(text=items['variant_3'])
    btn4 = types.KeyboardButton(text=items['variant_4'])
    btn5 = types.KeyboardButton(text=items['variant_5'])
    btn6 = types.KeyboardButton(text=items['variant_6'])
    keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(message.chat.id, items[f'question_9_{language}'], reply_markup=keyboard)


def question_10(message):
    database[message.chat.id]['select'] = question_9
    language = database[message.chat.id]['language']
    bot.send_message(message.chat.id, items[f'question_10_{language}'], reply_markup=create_range_slider())


def question_11(message):
    database[message.chat.id]['select'] = question_10
    language = database[message.chat.id]['language']
    bot.send_message(message.chat.id, items[f'question_11_{language}'], reply_markup=create_range_slider())


def question_12(message):
    database[message.chat.id]['select'] = question_11
    language = database[message.chat.id]['language']
    bot.send_message(message.chat.id, items[f'question_12_{language}'])


def question_13(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, items[f'question_13_{language}'], reply_markup=keyboard)


def question_14(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, items[f'question_14_{language}'], reply_markup=keyboard)


def question_15(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    language = database[message.chat.id]['language']
    btn1 = types.KeyboardButton(text=items[f'yes_{language}'])
    btn2 = types.KeyboardButton(text=items[f'no_{language}'])
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, items[f'question_15_{language}'], reply_markup=keyboard)


def send_goodbye(message):
    language = database[message.chat.id]['language']
    bot.send_message(chat_id=message.chat.id, text=items[f'good_bye_{language}'])


def create_range_slider():
    markup = types.InlineKeyboardMarkup()
    first_column = [" ", 0.1, 0.3, 0.5, 0.7, 0.9]
    second_column = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    for i in range(6):
        if i == 0:
            btn1 = types.InlineKeyboardButton(f" ", callback_data=f"none")
        else:
            btn1 = types.InlineKeyboardButton(f"{first_column[i]}", callback_data=f"value:{first_column[i]}")
        btn2 = types.InlineKeyboardButton(f"{second_column[i]}", callback_data=f"value:{second_column[i]}")
        markup.row(btn1, btn2)
    return markup
