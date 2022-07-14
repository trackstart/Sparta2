import datetime
from pyowm import OWM
from time import sleep
from pyowm.utils import config
from pyowm.utils import timestamps

lifePoints = 354

while True:
    owm = OWM('e93e24e090e1fce79904de77891fd189')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('Moscow,RU')
    w = observation.weather

    degrees = w.temperature('celsius')
    deg = degrees['temp']

    lifePoints = lifePoints+(deg/100)
    print('LP (LifePoints)', lifePoints)
    print('Температура', deg)
    print('Дельта', deg/100)
    current_date_time = datetime.datetime.now()
    current_time = current_date_time.time()
    print('Время', current_time, '\n')


    sleep (60)









#w.detailed_status         # 'clouds'
#w.wind()                  # {'speed': 4.6, 'deg': 330}
#w.humidity                # 87
#w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#w.rain                    # {}
#w.heat_index              # None
#w.clouds                  # 75
#print(w.temperature('celsius'))
#print(w.wind())
#print(w.detailed_status)

# Will it be clear tomorrow at this time in Milan (Italy) ?
#forecast = mgr.forecast_at_place('Milan,IT', 'daily')
#answer = forecast.will_be_clear_at(timestamps.tomorrow())