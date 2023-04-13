from aiogram import *
from aiogram.types import *
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3

bot = Bot('5995066955:AAFUb9KRCR-b4NeUUmHcgJnHuS2I3IsNxk0')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

btnMain = KeyboardButton('Главное меню')
btnInfo = KeyboardButton('Информация')
btnTovar = KeyboardButton('Товары', web_app=WebAppInfo(url='https://acidic777.github.io/'))
btnReg = KeyboardButton('Зарегистрироваться')
btnTeach = KeyboardButton('Обучение', web_app=WebAppInfo(url='https://acidic777.github.io/acidic777.github.io-test/'))
meinMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfo, btnReg, btnTeach, btnTovar)
btnInfoCompany = KeyboardButton('О компании')
btnInfoSotr = KeyboardButton('Сотрудники')
btnQuation = KeyboardButton('Вопросы')
infoMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnInfoCompany, btnInfoSotr, btnQuation, btnMain)
btnIgra = KeyboardButton('Познакомиться с сотрудниками')
sotrMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnIgra, btnMain)


class user_reg(StatesGroup):
    login = State()
    tg = State()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user),
                           reply_markup=meinMenu)


@dp.message_handler(commands=['delete'])
async def main(message):
    conn = sqlite3.connect('pickle.sql')
    cur = conn.cursor()

    cur.execute("DELETE FROM users")
    cur.execute("DELETE FROM idusers")
    conn.commit()
    cur.close()
    conn.close()
    await bot.send_message(message.chat.id, 'таблица очищена')


@dp.message_handler(commands=['start'])
async def info(message: types.Message, state=FSMContext):
    conn = sqlite3.connect('pickle.sql')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS info (id int, info str)')
    cur.execute('CREATE TABLE IF NOT EXISTS text (id int, info str)')
    cur.execute("INSERT INTO text (id, info) VALUES ('%s', '%s')" % (1, 'asas'))
    conn.commit()

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'О чем хотите узнать?', reply_markup=infoMenu)
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
    elif message.text == 'О компании':
        buttons = [types.InlineKeyboardButton(text='Перейти на сайт',
                                              url='https://acidic777.github.io/acidic777.github.io-site-1/')]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)


        await bot.send_photo(chat_id=message.chat.id,
                             photo='https://sun6-20.userapi.com/s/v1/if1/C8pSYcTpNbmeoedany6TFExa0ChOw4xJcT6y5GcrqTWP10urlTLXiSWsgphYGk6G6l0UTphR.jpg?size=1704x1707&quality=96&crop=457,0,1704,1707&ava=1')


        await bot.send_message(message.chat.id, 'Компания "Green Life" занимается производством и продажей экологически чистых товаров, проведением обучающих семинаров, организацией благотворительных акций, предоставлением консультаций и разработкой инновационных технологий для сохранения окружающей среды. Цель компании - создание более чистой и здоровой среды для жизни и улучшение качества жизни людей.',
                               reply_markup=keyboard)
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()

    elif message.text == 'Познакомиться с сотрудниками':
        conn = sqlite3.connect('pickle.sql')

        cur = conn.cursor()

        cur.execute("SELECT * FROM idusers")
        users = cur.fetchall()

        for el in users:
            i = str(el)

            i = i[1:-2]
            i = int(i)
            if i != message.from_user.id:
                await bot.send_message(i, 'Вас приглашает поиграть в доту @{0.username}'.format(message.from_user))
            else:
                await bot.send_message(message.from_user.id, 'Приглашение отправлено')

        cur.close()
        conn.close()
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()

    elif message.text == 'Обучение':
        await bot.send_message(message.from_user.id,
                               'Давай займемся обучением в виде простого теста, после которого ты обучишься нашему ремеслу'
                               )
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
    elif message.text == 'Товары':
        await bot.send_message(message.from_user.id,
                               'Посмотрите товары, может что-то приглянется)'
                               )
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
    elif message.text == 'Сотрудники':
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
        await bot.send_message(message.from_user.id, 'Сотрудники компании', reply_markup=sotrMenu)

        conn = sqlite3.connect('pickle.sql')

        cur = conn.cursor()

        cur.execute("SELECT * FROM users")
        users = cur.fetchall()

        info = ''
        for el in users:
            info += f'Имя: {el[1]}, Логин тг: @{el[2]}\n'

        cur.close()
        conn.close()
        await bot.send_message(message.chat.id, info)
    elif message.text == 'Главное меню':
        await bot.send_message(message.from_user.id, 'Вы вернулись в главное меню', reply_markup=meinMenu)
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
    elif message.text == 'Вопросы':
        await bot.send_message(message.from_user.id, '''Какие товары производит и продает компания "Green Life"?
Компания "Green Life" производит и продает экологически чистые товары, такие как товары для дома, косметика, продукты питания и т.д.''')
        await bot.send_message(message.from_user.id, '''Какие мероприятия проводит компания "Green Life"?
Компания "Green Life" проводит обучающие семинары, благотворительные акции и предоставляет консультации по вопросам экологии.''')
        await bot.send_message(message.from_user.id, '''Какие цели преследует компания "Green Life"?
Цель компании "Green Life" - создать более чистую и здоровую среду для жизни и улучшить качество жизни людей.''')
        await bot.send_message(message.from_user.id, '''Какие преимущества предоставляет компания "Green Life" своим клиентам?
Компания "Green Life" предоставляет своим клиентам экологически чистые товары, которые не наносят вред окружающей среде. Кроме того, компания предоставляет консультации и обучающие семинары по вопросам экологии.
''')
        await bot.send_message(message.from_user.id, '''Какие проекты по сохранению окружающей среды разрабатывает компания "Green Life"?
Компания "Green Life" занимается разработкой инновационных технологий, которые помогут сохранить окружающую среду, такие как технологии для утилизации отходов и уменьшения выбросов вредных веществ.''')
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
    elif message.text == 'Зарегистрироваться':
        conn = sqlite3.connect('pickle.sql')
        cur = conn.cursor()
        user_id = message.from_user.id

        cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
        conn.commit()
        conn = sqlite3.connect('pickle.sql')

        cur = conn.cursor()

        cur.execute("SELECT * FROM idusers")
        users = cur.fetchall()
        ls = []
        for el in users:
            i = str(el)

            i = i[1:-2]
            i = int(i)
            ls.append(i)
        if message.from_user.id not in ls:
            conn = sqlite3.connect('pickle.sql')
            cur = conn.cursor()
            cur.execute(
                'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, login varchar(50), tg varchar(50))')
            cur.execute('CREATE TABLE IF NOT EXISTS idusers (id int)')
            conn.commit()
            await bot.send_message(message.chat.id, 'Введите Имя')
            await user_reg.login.set()

            @dp.message_handler(state=user_reg.login)
            async def addlogin(message: types.Message, state=FSMContext):
                global login
                login = message.text
                conn = sqlite3.connect('pickle.sql')
                cur = conn.cursor()
                user_id = message.from_user.id

                cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
                conn.commit()
                await state.finish()
                await bot.send_message(message.chat.id, 'Введите логин телеграмма')
                await user_reg.tg.set()

            @dp.message_handler(state=user_reg.tg)
            async def addtg(message: types.Message, state=FSMContext):
                tg = message.text
                conn = sqlite3.connect('pickle.sql')
                cur = conn.cursor()
                user_id = message.from_user.id

                cur.execute("INSERT INTO info (id, info) VALUES ('%s', '%s')" % (user_id, message.text))
                conn.commit()

                conn = sqlite3.connect('pickle.sql')
                cur = conn.cursor()
                user_id = message.from_user.id

                cur.execute("INSERT INTO users (login, tg) VALUES ('%s','%s')" % (login, tg))
                cur.execute("INSERT INTO idusers (id) VALUES ('%s')" % (user_id))
                conn.commit()

                await bot.send_message(message.chat.id, 'Вы зарегистрированы')
                await state.finish()
        else:
            await bot.send_message(message.chat.id, 'Вы уже зарегистрированы')




executor.start_polling(dp)
