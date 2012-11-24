#!/usr/bin/env python

from decimal import Decimal
import urllib
from xml.etree import ElementTree

import radiotherm
from django.conf import settings

from hometemp.models import Record

WUNDER_URL = 'http://api.wunderground.com/weatherstation/WXCurrentObXML.asp?ID=%s'


def home_temps():
    """
    fetches current and target temps from thermostat. Uses IP specified in
    settings if any, otherwise uses the auto-discovery protocol.

    :return:    current and target temperatures of home
    :rtype:     tuple of Decimals
    """
    thermostat = radiotherm.get_thermostat(getattr(settings, 'THERMOSTAT_IP', None))
    data = thermostat.tstat['raw']
    temp = Decimal(str(data['temp']))
    if 't_heat' in data:
        target = Decimal(str(data['t_heat']))
    elif 't_cool' in data:
        target = Decimal(str(data['t_cool']))
    else:
        target = None
    return temp, target


def outside_temp():
    """
    Gets the current temp from a weather station via weather underground. The
    station's ID must be set as settings.WEATHER_STATION

    :return:    current temperature outside in degrees F
    :rtype:     Decimal
    """
    url = WUNDER_URL % settings.WEATHER_STATION
    req = urllib.urlopen(url)
    temp = ElementTree.fromstring(req.read()).find('temp_f').text
    return Decimal(temp)


def main():
    home, target = home_temps()
    outside = outside_temp()
    r = Record(home_temp=home, target_temp=target, outside_temp=outside)
    r.save()


if __name__ == '__main__':
    main()
