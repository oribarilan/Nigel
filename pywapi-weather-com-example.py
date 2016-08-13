#!/usr/bin/env python3

import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)

ta = pywapi.get_loc_id_from_weather_com("Be'er-Sheva")
kalamata = pywapi.get_weather_from_weather_com('ISXX0030','metric')

pp.pprint(kalamata)
