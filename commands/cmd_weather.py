# weather module
import pywapi
import pprint

pp = pprint.PrettyPrinter(indent=4)


# command weather action
def cmd_weather_action(b, update):
    forecast = get_forecast_for('ISXX0030')
    b.sendMessage(chat_id=update.message.chat_id, text=forecast)


def get_forecast_for(loc_id):
    # type: (str) -> none
    wdic = pywapi.get_weather_from_weather_com(loc_id, 'metric')
    loc = get_current(wdic, 'station')
    temperature = get_current(wdic, 'feels_like')
    temperature_units = get_units(wdic, 'temperature')
    forecast = "Forecast for {0}\nFeels like: {1} {2}".format(loc, temperature, str(temperature_units).lower())

    text = wdic['current_conditions']['text']
    if text:  # text is not empty
        forecast += "\n" + text + "."
    if forecast is None:
        forecast = "Can't access the weather right now, please try again."
    return forecast


def get_current(weather_dic, field):
    # type: (str, str) -> str
    return weather_dic['current_conditions'][field]


def get_units(weather_dic, field):
    # type: (str, str) -> str
    return weather_dic['units'][field]

'''
'ISXX0030' = be'er sheva
'''
