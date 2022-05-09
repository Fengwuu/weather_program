import eel
import pyowm

owm = pyowm.OWM("your api")


@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return "В городе " + place + " сейчас " + str(temp) + " градусов!"


eel.init("web")
eel.start("main.html", size=(700, 700))
