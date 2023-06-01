# нужные библиотеки:
# pip install pyTelegramBotAPI
# pip install googletrans==4.0.0rc1
#
# ссылка на телеграмм бота:
# https://t.me/smart_cup_bot

# Не использовать ' и " при ответах
# Если будите запускать код повторно, то закоментируйте файл "Создание таблицы для юзеров" от 'Начало' до 'Конец'


import telebot
from googletrans import Translator
from telebot import types
import sqlite3

que_t1 = ['Enter weapons.', "Who do you dislike the most", "What is your boy friend's name???", 'The most cozy place.',
          'How old are you??', 'What kind of gift do you want for the new year???',
          'Write something to get your story.']
que_t2 = ['The coolest feature/technology.', "The best person.", 'What are you most afraid of???',
          'Write something to get your story.']

status1 = 0
status2 = ''
status3 = ''
ans_t1 = []
ans_t2 = []
all_text = []
ans = []
textr = ''
i = 0
# len_all_text = 0
translator = Translator()
bot = telebot.TeleBot('6136107778:AAFGCd8fnSaz_LfklhiKuIjbh1JM27dpThs')
new_list = []
n_lego = ()
l_lego = 0
lego_name = ''
m = 0
h = False


# Важные переменные
all_txt = sqlite3.connect('all_text.db', check_same_thread=False)
c = all_txt.cursor()
# Создание таблицы для юзеров
# Начало
try:
    c.execute("""CREATE TABLE all_txt(
        user_name text,
        txt text,
        like integer,
        comment text,
        id integer
    )""")

except sqlite3.OperationalError:
    ...
#Конец
all_txt.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    hero = types.KeyboardButton('Hero of the tribe')
    car = types.KeyboardButton('Programmer in a sports car')
    show = types.KeyboardButton('Recent published stories')
    # lego = types.KeyboardButton('Story builder')
    # story = types.KeyboardButton('Other stories')
    markup.add(hero, car, show)
    bot.send_message(message.chat.id,
                     f'Hello {message.from_user.first_name}.\n I am a bot who will write you your new story',
                     reply_markup=markup)
    


@bot.message_handler(content_types=['text'])
def text_user(message):
    global status1, status2, status3, ans_t1, ans_t2, textr, i, all_text, all_txt, c, new_list, n_lego, l_lego, lego_name, ans, m, h

    if message.text == 'Hero of the tribe':
        status1 = 1
        ans_t1 = []
        i = 0
        bot.send_message(message.chat.id, 'Enter the race')

    elif message.text == 'Programmer in a sports car':
        status1 = -1
        ans_t1 = []
        i = 0
        bot.send_message(message.chat.id, 'If you were the owner of the company, what would it be called???')

    elif len(ans_t1) == 7 and status1 == 1:
        textr = ''

        textr = f"""A long time ago, a great battle took place in the world where {ans_t1[0]} lived.
{ans_t1[0].capitalize()} were well armed {ans_t1[1]}. Their goal was the same -
to protect their lands and wealth from {ans_t1[2]}.

In one of the battles, {ans_t1[0]} was heavily attacked, and {ans_t1[3].title()} ended up
behind enemy lines. He was forced to hide {ans_t1[4]} where he discovered
a magical amulet that could predict the future. {ans_t1[3].title()} decided
to put on an amulet to figure out how to get him out of {ans_t1[4]}.

The amulet lit up and showed the {ans_t1[5]} paths. {ans_t1[3].title()} chose the most
difficult path that led him to the leader of the enemies. With the help
his {ans_t1[1]}, {ans_t1[3].title()} defeated {ans_t1[2]} and saved his comrades.

After the war, {ans_t1[3].title()} returned to his homeland and was rewarded
{ans_t1[6]}. Later, {ans_t1[3].title()} became a great leader of his
country and helped everyone who needed his help."""

        c.execute(f"INSERT INTO all_txt VALUES ('{message.from_user.first_name}', '{textr}', 0, '', {message.chat.id})")            
        all_txt.commit()

        c.execute("SELECT * FROM all_txt")

        bot.send_message(message.chat.id, textr)
        status1 = 0
        ans_t1 = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tr = types.KeyboardButton('Translate this text')
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        show = types.KeyboardButton('Recent published stories')
        # lego = types.KeyboardButton('Story builder')
        # story = types.KeyboardButton('Other stories')
        markup.add(hero, car, show)
        bot.send_message(message.chat.id, 'Who will your next story be about???', reply_markup=markup)

    if len(ans_t2) == 4 and status1 == -1:
        textr = ''
        textr = f"""There were the fastest and most luxurious cars in the world, but
only one company created the real sports cars of the future -
"{ans_t2[0]}". These beautiful machines were capable of reaching the speed
of light and had the most innovative technologies, including {ans_t2[1]}.

One day, racers who owned "{ans_t2[0]}"
of different models gathered on the track. Among them were the racer {ans_t2[2].title()}, who was
a programmer who graduated from IFTIS and tried to implement into the car
his latest development, but for some reason it did not work out and there was an error that he could not figure out.

He asked many people who know English, but no one could translate the text that occurs when an error occurs. 
Before the race, he met a girl, Alina, who had excellent knowledge of foreign languages. She helped {ans_t2[2].title()} 
translate an error that no one could understand. 
Fortunately, in a few hours, the rider managed to fix an annoying mistake.

The race started and "{ans_t2[0]}" raced along the track, leaving a whirlwind behind them
of fire and smoke. The racer {ans_t2[2].title()} felt how his car reacted
to his every move. He enjoyed the speed and adrenaline
until he heard the voice of his car, which warned him about
{ans_t2[3]}.

He was forced to slow down, and at that moment another rider
rushed past him, but his "{ans_t2[0]}" began to lose speed due to
{ans_t2[3]}. The driver {ans_t2[2].title()} decided to take advantage of the situation to
finish first and win the race.

"{ans_t2[0].capitalize()}" continued to compete on the track, creating a real
the show is for all viewers, and the racer {ans_t2[2].title()} continued to improve their
cars to stay on top of the sports world."""

        c.execute(f"INSERT INTO all_txt VALUES ('{message.from_user.first_name}', '{textr}', 0, '', {message.chat.id})")            
        all_txt.commit()

        c.execute("SELECT * FROM all_txt")

        bot.send_message(message.chat.id, textr)
        status1 = 0
        ans_t2 = []
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        tr = types.KeyboardButton('Translate this text')
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        show = types.KeyboardButton('Recent published stories')
        # story = types.KeyboardButton('Other stories')
        markup.add(hero, car, show)
        bot.send_message(message.chat.id, 'Who will your next story be about???', reply_markup=markup)

    if message.text is not None and status1 == 1 and message.text != 'Hero of the tribe' and message.text != 'Programmer in a sports car':
        ans_t1.append(message.text)
        bot.send_message(message.chat.id, que_t1[i])
        i += 1

    elif message.text is not None and status1 == -1 and message.text != 'Programmer in a sports car' and message.text != 'Hero of the tribe':
        ans_t2.append(message.text)
        bot.send_message(message.chat.id, que_t2[i])
        i += 1

    elif message.text == 'Translate this text' and status1 == 0 and message.text is not None and status2 == '':
        trans = translator.translate(textr, src='en', dest='ru')
        bot.send_message(message.chat.id, trans.text)

#     elif message.text == 'Story builder':
#         bot.send_message(message.chat.id, 'Enter the name of your story')
#         status2 = 'lego_name'
    
#     elif message.text is not None and status2 == 'lego_name':
#         lego_name = str(message.text)
#         status2 = 'lego'
#         bot.send_message(message.chat.id, '''Enter your history by entering all questions in {}\n
# For example:\n\n
# Hello {What is your name?}''')
    
#     elif status2 == 'lego' and message.text is not None:
#         e = False
#         qt = ''
#         q = []
#         at = ''

#         for x in message.text:
#             if x == '{':
#                 e = True
#                 at += x
#             elif x == '}':
#                 e = False
#                 if not qt in q:
#                     q.append(qt)
#                 at += f'{q.index(qt)}'
#                 at += x
#                 qt = ''
#             elif not e:
#                 at += x
#             elif e:
#                 qt += x
#         print(q, at)
#         work = ''
#         for nam, i in enumerate(q):
#             m = nam
#             work += str(nam + 1) + ')\t' + i + '\n\n'
#         print(work)
#         print(lego_name)
#         c.execute(f"INSERT INTO lego VALUES ('{lego_name}', '{at}', '{work}', {m})")
#         all_txt.commit()
#         bot.send_message(message.chat.id, 'Your story has been added successfully')
#         status2 = ''

    
#     elif message.text == 'Other stories' and status2 == '':
#         c.execute("SELECT rowid, name, txt, ques, m FROM lego")
#         n_lego = c.fetchall()
#         all_txt.commit()
#         print(n_lego)
#         status2 = 'other'
#         l_lego = len(n_lego) - 1
#         h = True
    
#     if (status2 == 'other' and message.text is not None and l_lego != -1 and status3 == '') or (h and status3 == ''):
#         print(n_lego)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
#         no = types.KeyboardButton('Nex story')
#         yes = types.KeyboardButton('Write this story')
#         ex = types.KeyboardButton('Exit')
#         markup.add(yes, no, ex)
#         bot.send_message(message.chat.id, n_lego[l_lego][1], reply_markup=markup)
#         if message.text == 'Nex story':
#             l_lego -= 1
#         elif message.text == 'Write this story':
#             bot.send_message(message.chat.id, 'Answer the questions (each answer with a new line)')
#             bot.send_message(message.chat.id, n_lego[l_lego][3])
#             status3 = 'ans'
#         elif message.text == 'Exit':
#             ...
#         h = False
        
#     elif status3 == 'ans' and status2 == 'other' and message.text is not None:
#         if len(ans) != n_lego[l_lego][4]:
#             ans.append(message.text)
#         else:
#             t = f'{n_lego[l_lego][2]}'
#             print(t)
#             print(n_lego[l_lego][4])
#             for j in range(n_lego[l_lego][4]):
#                 t.replace('{' + str(j) + '}', ans[j])
#             # e = False
#             # n = ''
#             # for x in n_lego[l_lego][2]:
#             #     if x == '{':
#             #         t += x
#             #         e = True
#             #     elif x == '}':
#             #         n = int(n)
#             #         t += x
#             #         e = True
#             #         n = ''
#             #     elif e:
#             #         n += x
#             #     elif not e:
#             #         t += x

#             bot.send_message(message.chat.id, f'{t}')



    elif message.text == 'Recent published stories':

        # c.execute("SELECT rowid FROM all_txt")
        # print(c.fetchall()[-1][0] - 1)
        c.execute("SELECT user_name, txt, like, comment, id, rowid FROM all_txt")
        # len_all_text = c.fetchall()[-1][0] - 1# * len(c.fetchall()[-1])
        # c.execute("SELECT rowid FROM all_txt")
        for i in c.fetchall():
            q = [i[0], i[1], i[2], i[3], i[4], i[5]]
            new_list.append(q)
        status2 = 'show'
        all_txt.commit()

    if message.text is not None and status2 == 'show' and not (message.text in ['Like', 'Comment', 'Subscribe this author', 'Translate this text', 'Exit', 'Next']) and new_list != []:
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        like = types.KeyboardButton('Like')
        com = types.KeyboardButton('Comment')
        # sub = types.KeyboardButton('Subscribe this author')
        next = types.KeyboardButton('Next story')
        tr = types.KeyboardButton('Translate this text')
        ex = types.KeyboardButton('Exit')
        markup.add(like, com, next, tr, ex)

        # c.execute("SELECT * FROM all_txt")
        # print(c.fetchall())

        # li = 
        bot.send_message(message.chat.id, f"{new_list[-1][0]}", reply_markup=markup)
        bot.send_message(message.chat.id, f"{new_list[-1][1]}")
        bot.send_message(message.chat.id, f"Like: {new_list[-1][2]}")
        bot.send_message(message.chat.id, f"Comments:\n\n{new_list[-1][3]}")
    #     q = ''
    #     for j in  all_text[len_all_text]["comment"]:
    #         q += j + '\n\n'
    #     if q:
    #         bot.send_message(message.chat.id, q)

    if message.text == 'Like' and status2 == 'show':
        # all_text[len_all_text]['like'] += 1
        # print('Первое', new_list)
        li = new_list[-1][2] + 1
        # c.execute("SELECT like FROM all_txt")
        # li = c.fetchall()[len_all_text][2] + 1
        # print(li)
        
        # c.execute("SELECT rowid FROM all_txt")
        id_us = new_list[-1][-1]
        # print('Второе', id_us)

        c.execute(f"UPDATE all_txt SET like = ? WHERE rowid = ?", (li, id_us))

        new_list[-1][2] = new_list[-1][2] + 1
        # print('Опять список',new_list)

        all_txt.commit()

        bot.send_message(message.chat.id, f"Like: {new_list[-1][2]}")

    elif status2 == 'comment' and message.text is not None:
        status2 = 'show'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        like = types.KeyboardButton('Like')
        com = types.KeyboardButton('Comment')
        # sub = types.KeyboardButton('Subscribe this author')
        next = types.KeyboardButton('Next story')
        tr = types.KeyboardButton('Translate this text')
        ex = types.KeyboardButton('Exit')
        markup.add(like, com, next, tr, ex)

        co = new_list[-1][3] + message.text + '\n\n'
        id_us = new_list[-1][-1]

        c.execute("UPDATE all_txt SET comment = ? WHERE rowid = ?", (co, id_us))

        all_txt.commit()

        new_list[-1][3] = co

        bot.send_message(message.chat.id, f"Comments:\n\n{new_list[-1][3]}", reply_markup=markup)




        # all_txt = sqlite3.connect('all_text.db')
        # c = all_txt.cursor()
        # c.execute("SELECT * FROM all_txt")
        # all_txt.commit()
        # c.fetchall()[len_all_text] = (c.fetchall()[len_all_text][0], c.fetchall()[len_all_text][1], c.fetchall()[len_all_text][2], c.fetchall()[len_all_text][3] + "{}\n".format(message.text), c.fetchall()[len_all_text][4])
        # bot.send_message(message.chat.id, "Comments:")
        # bot.send_message(message.chat.id, c.fetchall()[len_all_text][3])
        # all_txt.close()







    #     # all_text[len_all_text]['comment'].append(message.text)
    #     # status2 = 'show'
    #     # bot.send_message(message.chat.id, 'Comments:')
    #     # for c in all_text[len_all_text]['comment']:
    #     #     bot.send_message(message.chat.id, c)

    elif message.text == 'Comment' and status2 == 'show':
        bot.send_message(message.chat.id, 'Enter a comment')
        status2 = 'comment'
        # while message.text is None:
        #     pass

    elif message.text == 'Translate this text' and status2 == 'show':
        trans = translator.translate(str(new_list[-1][1]), src='en', dest='ru')
        bot.send_message(message.chat.id, trans.text)
    #     if status2 == 'show':
    #         status2 = 'trans'
    #     if status2 == 'trans':    
    #         all_txt = sqlite3.connect('all_text.db')
    #         cursor = all_txt.cursor()
    #         cursor.execute("SELECT * FROM all_txt")
    #         all_txt.commit()
            
    #         trans = translator.translate( cursor.fetchall()[len_all_text][0], src='en', dest='ru')
    #         bot.send_message(message.chat.id, trans.text)
    #         status2 = 'show'
            
    #         all_txt.close()

    elif message.text == 'Exit' and status3 == '':
        status2 = ''
        new_list = []

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        show = types.KeyboardButton('Recent published stories')
        # story = types.KeyboardButton('Other stories')
        markup.add(hero, car, show)
        bot.send_message(message.chat.id,'Exit', reply_markup=markup)
    
    elif message.text == 'Next story' and status2 == 'show' and len(new_list) == 0:
        status2 = ''
        new_list = []

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        hero = types.KeyboardButton('Hero of the tribe')
        car = types.KeyboardButton('Programmer in a sports car')
        show = types.KeyboardButton('Recent published stories')
        # lego = types.KeyboardButton('Story builder')
        # story = types.KeyboardButton('Other stories')
        markup.add(hero, car, show)
        bot.send_message(message.chat.id,'That is all', reply_markup=markup)

    elif message.text == 'Next story' and status2 == 'show':
        # print(new_list, '\n\n')
        del new_list[-1]
        # print(new_list)




bot.polling(none_stop=True)
