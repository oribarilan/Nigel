#!/usr/bin/env python
#
# Nigel PA Bot

import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from misc import utl_error
from commands import cmd_start, cmd_weather, cmd_timer
from messaging import msg_echo, msg_unknown

# enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


# data
d_weather = \
    {
        'location_id': 'ISXX0030'
    }

users = \
    {
        'Name': 'Ori',
        'City': "Be'er Sheva",
        'Weather': d_weather
    }


# init
def main():
    # fields
    updater = Updater(token='259155519:AAEzSS5-vaVthHH-gWTM4LK3eM-jnyJ2Wf8')
    dispatcher = updater.dispatcher
    bot = telegram.Bot(token='259155519:AAEzSS5-vaVthHH-gWTM4LK3eM-jnyJ2Wf8')

    # --> commands
    # start
    start_handler = CommandHandler('start', cmd_start.cmd_start_action)
    dispatcher.add_handler(start_handler)
    # weather
    w_handler = CommandHandler('w', cmd_weather.cmd_weather_action)
    dispatcher.add_handler(w_handler)
    # timer
    timer_handler = CommandHandler('timer', cmd_timer.cmd_timer_set, pass_args=True, pass_job_queue=True)
    timer_stop_handler = CommandHandler('stop', cmd_timer.cmd_timer_unset)
    dispatcher.add_handler(timer_handler)
    dispatcher.add_handler(timer_stop_handler)

    # --> messaging
    echo_handler = MessageHandler([Filters.text], msg_echo.msg_echo_action)
    dispatcher.add_handler(echo_handler)

    # --> misc
    # unknown command (must be last)
    unknown_handler = MessageHandler([Filters.command], msg_unknown.msg_unknown_action)
    dispatcher.add_handler(unknown_handler)
    # error logger
    dispatcher.add_error_handler(utl_error.utl_error_action)

    # getMe
    nigel = None
    try:
        nigel = bot.getMe()
    except telegram.TelegramError:
        print 'Error occurred. Nigel is not initialized.'

    if nigel is None:
        exit()

    nigel_dict = nigel.to_dict()

    print "Nigel is alive !"
    for p in nigel_dict:
        print p, ':', nigel_dict[p]

    # start the bot
    updater.start_polling()

    # Block until you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
