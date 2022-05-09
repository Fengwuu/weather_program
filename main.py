import eel
import pyowm

owm = pyowm.OWM("f2a349d52db19dfdd2bd50bdb6ba4573")


@eel.expose
def get_weather(place):

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    return "В городе " + place + " сейчас " + str(temp) + " градусов!"


eel.init("web")
eel.start("main.html", size=(700, 700))
