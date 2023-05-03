from terms import database, items, bot
from telegram_bot_functions import chose_language, introduction, question_1, question_2, question_3, question_4, question_5, question_6, check_question_6, question_7, question_8, question_9, question_10, question_11, question_12, question_13, question_14, question_15, send_goodbye
import checkers


questions = [chose_language, introduction, question_1, question_2, question_3, question_4, question_5, question_6,
             check_question_6, question_7, question_8, question_9, question_10, question_11, question_12, question_13,
             question_14, question_15, send_goodbye]


@bot.message_handler(commands=["back"])
def back_command(message):
    bot.send_message(message.chat.id, "Вы нажали кнопку /back. Вам придется заново ответить на"
                                      "все вопросы, начиная с предыдущего.")
    try:
        if database[message.chat.id]['current_position'] > 0:
            database[message.chat.id]['current_position'] -= 1
            questions[database[message.chat.id]['current_position']](message)
    except KeyError:
        pass


@bot.message_handler(commands=["start"])
def start_command(message):
    database[message.chat.id] = {}
    database[message.chat.id]['current_position'] = 0
    questions[database[message.chat.id]['current_position']](message)


@bot.message_handler(content_types=["text"])
def answer_question(message):
    print(database[message.chat.id]['current_position'])
    print(message.chat.id)
    next = True
    step = 1
    if database[message.chat.id]['current_position'] == 0:
        if not checkers.read_language(message):
            step = 0
            bot.send_message(chat_id=message.chat.id, text="Write from keyboard, please")
    elif database[message.chat.id]['current_position'] == 1:
        language = database[message.chat.id]['language']
        if message.text == items[f'no_{language}']:
            next = False
            step = 0
            database[message.chat.id]['introduction'] = 'No'
            bot.send_message(message.chat.id, items[f'rejection_{language}'])
        elif message.text == items[f'yes_{language}']:
            database[message.chat.id]['introduction'] = 'Yes'
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 2:
        language = database[message.chat.id]['language']
        if message.text == items[f'yes_{language}']:
            database[message.chat.id]['relocant'] = 'yes'
        elif message.text == items[f'no_{language}']:
            next = False
            step = 0
            database[message.chat.id]['relocant'] = 'no'
            bot.send_message(message.chat.id, items[f'nonrelocant_{language}'])
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 3:
        language = database[message.chat.id]['language']
        if message.text == items[f'man_{language}']:
            database[message.chat.id]['question_2'] = 'man'
        elif message.text == items[f'woman_{language}']:
            database[message.chat.id]['question_2'] = 'woman'
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 4:
        language = database[message.chat.id]['language']
        if checkers.check_age(message):
            database[message.chat.id]['question_3'] = message.text
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'age_error_{language}'])
    elif database[message.chat.id]['current_position'] == 5:
        database[message.chat.id]['question_4'] = message.text
    elif database[message.chat.id]['current_position'] == 6:
        database[message.chat.id]['question_5'] = message.text
    elif database[message.chat.id]['current_position'] == 8:
        language = database[message.chat.id]['language']
        if message.text == items[f'yes_{language}']:
            pass
        elif message.text == items[f'no_{language}']:
            step = -1
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 9:
        language = database[message.chat.id]['language']
        if checkers.check_bottoms(message):
            database[message.chat.id]['question_7'] = message.text
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 10:
        database[message.chat.id]['question_9'] = message.text
    elif database[message.chat.id]['current_position'] == 11:
        language = database[message.chat.id]['language']
        if checkers.check_bottoms(message):
            database[message.chat.id]['question_8'] = message.text
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 12:
        language = database[message.chat.id]['language']
        if checkers.check_bottoms(message):
            database[message.chat.id]['question_11'] = message.text
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 14:
        database[message.chat.id]['question_13'] = message.text
    elif database[message.chat.id]['current_position'] == 15:
        language = database[message.chat.id]['language']
        if message.text == items[f'no_{language}']:
            database[message.chat.id]["question_14"] = "no"
        elif message.text == items[f'yes_{language}']:
            database[message.chat.id]["question_14"] = "yes"
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 16:
        language = database[message.chat.id]['language']
        if message.text == items[f'no_{language}']:
            database[message.chat.id]["question_15"] = "no"
        elif message.text == items[f'yes_{language}']:
            database[message.chat.id]["question_15"] = "yes"
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    elif database[message.chat.id]['current_position'] == 17:
        language = database[message.chat.id]['language']
        if message.text == items[f'no_{language}']:
            database[message.chat.id]["question_16"] = "no"
        elif message.text == items[f'yes_{language}']:
            database[message.chat.id]["question_16"] = "yes"
        else:
            step = 0
            bot.send_message(chat_id=message.chat.id, text=items[f'keyboard_error_{language}'])
    else:
        next = False
        step = 0
    if next:
        print("in next position: ", database[message.chat.id]['current_position'])
        print("in next step: ", step)
        database[message.chat.id]['current_position'] += step
        questions[database[message.chat.id]['current_position']](message)


@bot.callback_query_handler(func=lambda call: call.data in ["children", "parents", "invalids"])
def select_category(call):
    database[call.message.chat.id]["selected_categories"] = []
    database[call.message.chat.id]["selected_categories"].append(call.data)
    bot.answer_callback_query(callback_query_id=call.id, text="Selected: " + call.data)


@bot.callback_query_handler(func=lambda call: call.data == "done")
def submit_categories(call):
    language = database[call.message.chat.id]["language"]
    if database[call.message.chat.id]["selected_categories"]:
        message = items[f"selected_categories_{language}"] + ", ".join(
            database[call.message.chat.id]["selected_categories"])
    else:
        message = items[f'nobody_selected_{language}']
    bot.answer_callback_query(callback_query_id=call.id, text=message)
    bot.send_message(chat_id=call.message.chat.id, text=message)
    database[call.message.chat.id]["categoies"] = database[call.message.chat.id]["selected_categories"]
    database[call.message.chat.id]['current_position'] += 1
    questions[database[call.message.chat.id]['current_position']](call.message)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'none':
        pass
    elif 'value:' in call.data:
        value = call.data.split(':')[-1]
        if database[call.message.chat.id]['select'] == question_9:
            database[call.message.chat.id]['question_9'] = value
            bot.send_message(call.message.chat.id, f"You selected {value}.")
            database[call.message.chat.id]['current_position'] += 1
            questions[database[call.message.chat.id]['current_position']](call.message)
        elif database[call.message.chat.id]['select'] == question_10:
            database[call.message.chat.id]['question_11'] = value
            bot.send_message(call.message.chat.id, f"You selected {value}.")
            database[call.message.chat.id]['current_position'] += 1
            questions[database[call.message.chat.id]['current_position']](call.message)



