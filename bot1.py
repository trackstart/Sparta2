import datetime
from pyowm import OWM
from time import sleep
from pyowm.utils import config
from pyowm.utils import timestamps

import asyncio
from aiogram import Bot, Dispatcher, types

async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} ?!, ola23",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    bot = Bot(token='5368490480:AAEWD5PqVCrX4tamRzY5NmSmM_Qf9szhgWM')
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        print('Бот запущен')
        await disp.start_polling()

    finally:
        await bot.close()

asyncio.run(main())


#lifePoints = 354

#while True:
#    owm = OWM('e93e24e090e1fce79904de77891fd189')
#    mgr = owm.weather_manager()
#    observation = mgr.weather_at_place('Moscow,RU')
#    w = observation.weather

#    degrees = w.temperature('celsius')
#    deg = degrees['temp']

#    lifePoints = lifePoints+(deg/100)
#    print('LP (LifePoints)', lifePoints)
#    print('Температура', deg)
#    print('Дельта', deg/100)
#    current_date_time = datetime.datetime.now()
#    current_time = current_date_time.time()
#    print('Время', current_time, '\n')


#   sleep (60)
