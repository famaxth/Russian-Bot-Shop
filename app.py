# - *- coding: utf- 8 - *-

#Production by Berlin
#Telegram - @por0vos1k


import telebot
import time
from datetime import datetime
import random
import mine
import urllib
import config
import SimpleQIWI
from io import BytesIO
from telebot import types
from time import sleep
from SimpleQIWI import *


bot = telebot.TeleBot(config.token, parse_mode=None)
print("Start")


joinedFile = open("joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()



@bot.message_handler(commands=["start"])
def send_welcome(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(str(message.chat.id))
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "Добро пожаловать в RatHouse❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными теневыми услугами\n\n◼️ Хочешь научиться работать по-черному, но у тебя нет нужных материалов - ты попал по адресу!\n\n◼️ В RatHouse присутствует доска объявлений о поиске сотрудников, а также реферальная система с помощью которых вы сможете заработать\n\n◼️ Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=mine.start)
    elif message.chat.id == config.admin_id:
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "Добро пожаловать в RatHouse❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными теневыми услугами\n\n◼️ Хочешь научиться работать по-черному, но у тебя нет нужных материалов - ты попал по адресу!\n\n◼️ В RatHouse присутствует доска объявлений о поиске сотрудников, а также реферальная система с помощью которых вы сможете заработать\n\n◼️ Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=mine.admibro)
    else:
        print("\nБот был запущен. ID: "+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "Добро пожаловать в RatHouse❗️\n\n◼️ Здесь ты можешь воспользоваться всеми возможными теневыми услугами\n\n◼️ Хочешь научиться работать по-черному, но у тебя нет нужных материалов - ты попал по адресу!\n\n◼️ В RatHouse присутствует доска объявлений о поиске сотрудников, а также реферальная система с помощью которых вы сможете заработать\n\n◼️ Огромный выбор услуг и товаров")
        bot.send_message(message.from_user.id, 'Выберите нужный раздел: ', reply_markup=mine.start)


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n\n/start - Для начала работы с ботом\n/help - Список доступных команд\n/info - Узнать информацию о боте\n\n⚙️Этот раздел пока находится в разработке")


@bot.message_handler(commands=["info"])
def send_info(message):
    bot.send_message(message.chat.id, "Shop by RatHouse")


@bot.message_handler(commands=["contact"])
def send_contact(message):
    bot.send_message(message.chat.id, "📎Контакты:\n\n◼️ Наши проекты - @kykl0vod\n\nУслуги гаранта(5%) - @Kukol6 ✔️")


@bot.message_handler(commands=["liu4eg7hok"])
def send_deepweb(message):
    bot.send_message(message.chat.id, "Бот создан разработчиком Berlin.")


@bot.message_handler(commands=["sticker"])
def send_sticker(message):
    if message.chat.id == config.admin_id:
        bot.send_sticker(config.admin_id, config.logo_stick)
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.message_handler(commands=["send"])
def send_sticker(message):
    if message.chat.id == config.admin_id:
        for user in joinedUsers:
            bot.send_message(user, message.text[message.text.find(' '):])
    else:
        bot.send_message(message.chat.id, "❌ В доступе отказано!")


@bot.message_handler(commands=["balance"]) 
def send_balance(message):
	if message.chat.id == config.admin_id:
		api = QApi(token=config.token_qiwi, phone=config.qiwi)
		balance = api.balance[0]
		bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *"+str(balance)+"* руб", parse_mode='Markdown')
	else:
		bot.send_message(message.chat.id, "❌ В доступе отказано!")



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == '⬅️ Назад':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.keyboard)
        elif call.data == '🛒Услуги':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.koret)
        elif call.data == 'Мтс':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🎲Подключаем скидки на связь.\n\nМЕГАФОН 30-50%\nМтс 20%\nЦена? - как 2 кофе☕️\nНа билайн нет ничего!\nНа Корпоратив не действует!!!\n-------------------------------\n📱Теле2\n•Можно сделать бесплатный месяц\n•Безлимит на ваш тариф со скидой 65%\n•Архивный тариф на ваш номер, тем самым сэкономя вам копеечку💲📱\nНужно смс для входа 😘Семье подключаешь - скидку получаешь👍")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Возврат денег за такси':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🚖Возврат денег за такси\n\nЦена - обговаривается индивидуально с менеджером.\n\nНеобходимо чтобы на аккаунте было не менее 3 не рефнутых поездок по карте\n\nРекомендуйте друзьям - получайте их 20% на карту")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Накрутка':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔶НАКРУТКА И ПРОДВИЖЕНИЕ ВСЕХ СОЦ.СЕТЕЙ\n\n🔷ГЛОБАЛЬНОЕ СНИЖЕНИЕ ЦЕН\n🔸Instagrаm\n🔹Telegram\n🔸Вконтакте\n\nДоступные типы:\nЖивые Подписчики, Лайки, Просмотры, Комменты, Репосты.\n\n🔹Все делается качественно и надолго, приятные цены.\n🔸Делаем инвайт в ваши чаты тг.\n🔹Скидка 10% на первый заказ\n")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == '💻 Программист':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💻 Услуги программиста\n\n📌Предлагаю вам свои услуги Python программиста. Могу делать ботов в телеграмм практически любой сложности(telebot, aiogram), парсеры, чекеры, а также веб-приложения на Django.\nЧтобы заказать эту услугу напишите нашему менеджеру.\n\nЦена: обговаривается индивидуально")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Бренд':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👑 Брендовые вещи за 50% стоимости\n\nЧасы, одежда, аксессуары и многое другое всегда в наличии.\nЕсли нужна какая-то определенная вещь или аксессуар - пишите нашему менеджеру\n\nВСЯ ОДЕЖДА НОВАЯ И ОРИГИНАЛЬНАЯ")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Пробив':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🔍 Предоставляем услуги комплексного пробива человека\n\nПолный список:\n\n- Детализация номера\n- Пробив по номеру телефона\n- Паспортные данные владельца номера\n- Поиск номера по сотовым операторам\n- Роспаспорт\n- Информация по физ. Лицам по линии ФНС,ПФР,МВД,ГАИ,РОСРЕЕСТР\n")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == '🔑Софт':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.ret)
        elif call.data == '📚Схемы':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.zxc)
        elif call.data == 'Instagram':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💰Схема💰\n\nНазвание: Заработок с помощью Instagram\n\nЦена: 1200 рублей\n\n📌Что нужно для заработка: \n\n•Аккаунт почты GMAIL\n\n•Браузер Google Chrome (Можно и в других браузерах, если есть поддержка расширении Chrome)\n\n•Instagram аккаунт (Лучше сразу перед началом работы, авторизоваться в браузере).")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Скам фортнайт':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💰Схема💰\n\nНазвание: Скам фортнайт\n\nЦена: 750 рублей\n\n📌Немного про заработок: \n\n•Это метод зароботка для людей, которые хотят минимум вложение и +/- стабильной прибыли!\n\n•Для схемы нужны небольшие вложения для рега инсты, кошелька на левый номер! (Анонимность) и так же иметь Qiwi/Yandex деньги на левый пасс. VPN и так далее по вашему желанию! (лично я ебашил без VPN'a, proxy и т.д). И еще, не будьте даунами и *****айте деньги через Bitcoin! (Total money отлично подойдет - НЕ реклама!)")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Аккаунты Facebook':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💰Схема💰\n\nНазвание: Получаем от 1500р в месяц с Facebook аккаунта\n\nЦена: 3200 рублей\n\n📌Немного про заработок: \n\n•Условия для аккаунтов: Аккаунты из Украины, России, Киргизии, Казахстана, Узбекистана, Турции, Кубы, Литвы, Латвии. Необходимые параметры: не менее 100 друзей, не менее 2 лет существования аккаунта.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Схема VK 2020 (PREMIUM)':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="""💲Схема💲\n\nНазвание: Схема VK + Файлообменник 2020 (PREMIUM)\n\nЦена: 5100 рублей\n\n✔"РАБОЧАЯ схема с доходом 100000р за 100р"\nВы серьезно?😈\n\nКачественный материал не может стоить таких денег❗️Запомни❗️В лучшем случае тебе дадут схему по которой заработаешь не больше 100р за месяц или вовсе пустышку...если не полетишь в ЧС...\n\nМы на рынке онлайн-заработка больше 5-ти лет. Есть опыт, о чем поделиться👍🏿\n\nПассивный заработок...Да, да! Он самый!\n\nВ нашей схеме мы научим тебя как генерировать деньги из VK - с помощью еще одного скрытного сервиса.\n\nИтак что по схеме:\n\n🎩 Белая и пушистая как твой кот.\n⌚️ Пассивная - то есть 1 раз настроил по нашей схеме и всегда получаешь деньги.\n💣 Абсолютно не требует вложений.\n🔞 Легка в настройке - справиться любой.""")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Посредничество на фрилансе':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="💰Схема💰\n\nНазвание: Заработок с помощью Instagram\n\nЦена: 2000 рублей\n\n📌Немного про заработок: \n\n•Большое количество людей в наше время хотят заниматься фрилансом, но не могут найти клиентов, так как не имеют отзывов и хорошо раскрученного аккаунта на фриланс бирже. Мы же будем неким посредником для них, для нас плюс в том, что мы имеем небольшую постоянную прибыль, а для работников в том, что имеют клиентов не заморачиваясь с их нахождением. Например, заказчик написал о том, что хочет заказать работу. Мы пересылаем все сообщения работнику и занижаем заявленую цену, чтобы получить чистую прибыль.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == '💳 Деньги':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.rich)
        elif call.data == 'Qiwi':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'ЯД/Юмани':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'BTC':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Физ. карты':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'PAYEER':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🗂Обучение':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.typer)
        elif call.data == 'МУЗЫКА, БИТЫ':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🎵МУЗЫКА, БИТЫ\n\nСписок курсов:\n\n- [Slava Marlow] Курс от Marlow Beats (2020)\n- [IY Beats] слив курсов битмейкинга (2020)\n- [Сергей Live] Профессиональное сведение и мастеринг\n- FL Studio с нуля до создания трека за 6 часов\n- FL STUDIO 12: Высший пилотаж\n\nЦена: 250 рублей")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == '3D МОДЕЛИРОВАНИЕ':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🖌3D МОДЕЛИРОВАНИЕ\n\nСписок курсов:\n\n- Дмитрий Смирнов - Онлайн-курс 3D моделирование для начинающих в 3ds max (2019)\n- [Blender3D] Артём Слаква - Курс по основам Blender 2.8+ (2019)\n- [ГРАФИКАНА] 3DS Max для всех. Моделирование и визуализация (2018)\n- [CGSociety] Моделирование окружения для игр\n- [Udemy] Zoia Voronina - 3Д моделирование в SketchUp (2020)\n- David Bittorf - Моделирование транспортных средств на твердой поверхности в Maya (2020)\n- Комплект курсов по 2D и 3D-моделированию и визуализации в AutoCAD\n\nЦена: 300 рублей")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'РАЗРАБОТКА ИГР':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="👾РАЗРАБОТКА ИГР\n\nСписок курсов:\n\n- [devtodev] Геймдизайн: как делать игры, которые нравятся и приносят деньги (2019)\n- [Udemy] Создание игры на Unity и C# | Полный курс| 2D Space Shooter (2019)\n- [Unity Study] UNITY БАЗОВЫЙ / СОЗДАЕМ 3D ИГРУ (2018)\n- [Unity Study] Unity Старт + Unity Базовый (2019)\n- Unity Tutorials на англ.\n\nЦена: 170 рублей")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == '🎮Аккаунты':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.gopa)
        elif call.data == 'Avito (пустой)':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Avito (раскрученный)':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🍔Еда за 40%':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.linux)
        elif call.data == '📎Товары':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.tovar)
        elif call.data == 'Авито':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите подкатегорию")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.rend)
        elif call.data == '📱Анонимный телефон':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🍟Макдональдс':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🍦Бургер Кинг':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🧲Магнит':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '♻️Пятерочка':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🍕Яндекс':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '💻 Анонимный ноутбук':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == '🕹 Анонимная флешка':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'GOOGLE DRIVE UNLIMITED':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="❗️GOOGLE DRIVE UNLIMITED❗️\n\nЦена: 500 рублей\n\n📌Для подключения услуги необходима только ваша почта Gmail.\n\n На вашем личном аккаунте GoogleDrive появится новая вкладка которая будет безлимитной! Вы сможете поделиться доступом вплоть до 300 человек и загружать в нее любые файлы!\n\n•Никак не изменяет ваш аккаунт\n\n•Вы сможете делиться своими данными и пространством с кем-либо.")
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.oplati)
        elif call.data == 'Софт Магнита':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Adobe Photoshop':
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="К сожалению, данный товар закончился")
        elif call.data == 'Оплатить':
            bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, inline_message_id=call.inline_message_id, reply_markup=mine.cash)
        elif call.data == 'Узнать настройки':
            if call.message.chat.id == config.admin_id:
                f = open("config.py", "r")
                bot.send_message(config.admin_id, f.read())
            else:
                bot.send_message(call.message.chat.id, "❌ В доступе отказано!")
        else:
            bot.send_message(call.message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")



@bot.message_handler(content_types=["text"])
def send_otziv(message):
    if message.text == '💌 Отзывы':
        print('Нажал Отзывы. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Оставить первый отзыв", url="https://t.me/g5u675fvm")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "💌 Отзывы\n\nЧестные отзывы о нашем магазине, по ссылке ниже", reply_markup=keyboard)
    elif message.text == '🏛 Новости':
        print('Нажал Новости. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Присоединиться", url="https://t.me/joinchat/AAAAAFj0WHiR5Eq-5KHWTg")
        keyboard.add(url_button)
        bot.send_message(message.chat.id, "❗️Наш новостной канал - https://t.me/joinchat/AAAAAFj0WHiR5Eq-5KHWTg", reply_markup=keyboard)
    elif message.text == '💼 Контакты':
        print('Нажал Контакты. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "📎Контакты:\n\n◼️ Наши проекты - @kykl0vod\n\nУслуги гаранта(5%) - @Kukol6 ✔️")
    elif message.text == 'Работа с RatHouse':
        print('Нажал Работа. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "На данный момент работы нет...")
    elif message.text == '🗂 Каталог товаров':
        print('Нажал Каталог. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "Что мы можем вам предложить?", reply_markup=mine.keyboard)
    elif message.text == '👤 Мой кабинет':
        print('Нажал Кабинет. ID: '+str(message.chat.id)+'    Дата/время: '+str(datetime.now()))
        bot.send_message(message.chat.id, "👤 Личный кабинет\n\nНикнейм: "+message.chat.username+"\nID: "+str(message.chat.id)+"\nЯзык: Ru")
    elif message.text == '🔥АДМИН ПАНЕЛЬ🔥':
            if message.chat.id == config.admin_id:
                bot.send_message(config.admin_id, "☎️ Админ панель", reply_markup=mine.abc)
            else:
                bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '💰Баланс':
        if message.chat.id == config.admin_id:
            api = QApi(token=config.token_qiwi, phone=config.qiwi)
            balance = api.balance[0]
            bot.send_message(config.admin_id, "🥝 Баланс вашего Киви: *"+str(balance)+"* руб", parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '🦋Стикеры':
        if message.chat.id == config.admin_id:
            bot.send_sticker(config.admin_id, config.logo_stick)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '⬅️ Назад':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, '⬅️ Вы вернулись в главное меню', reply_markup=mine.admibro)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '😈Админы':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, '🧊Список Админов: 🧊\n\n@admin', reply_markup=mine.nice)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '📩 Рассылка':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "Выберите нужное действие", reply_markup=mine.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == 'Отправить новое сообщение':
        if message.chat.id == config.admin_id:
            bot.send_message(config.admin_id, "Начнем!\n\nВы можете отправить подписчикам одно или несколько сообщений, в том числе любые файлы, музыку,картинки и т.д\n\nДля того, чтобы сделать рассылку нажмите /send и введите ваше сообщение.", reply_markup=mine.krekin)
        else:
            bot.send_message(message.chat.id, "❌ В доступе отказано!")
    elif message.text == '🛍 Мои покупки':
        bot.send_message(message.chat.id, '🎉 Мои покупки:')
    else:
        bot.send_message(message.chat.id, "Ничего не понятно!\n\nСписок доступных команд /help")


#Start bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
