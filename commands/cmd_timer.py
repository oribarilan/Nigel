from telegram.ext import Job
from telegram.parsemode import ParseMode

timers = dict()


# def alarm(bot, job):
#     """Function to send the alarm message"""
#     bot.sendMessage(context, text='Beep!')


def cmd_timer_set(bot, update, args, job_queue):
    """Adds a job to the queue"""
    chat_id = update.message.chat_id
    try:
        # args[0] should be either h.m or m
        h = 0
        m = 0
        if '.' not in args[0]:
            m = int(args[0])
        else:
            time = args[0].split(".")
            if len(time) is not 2:
                raise ValueError
            h = int(time[0])
            m = int(time[1])
        beep = '*Beep!*'
        del(args[0])
        # rest is the alert message
        alarm_text = None
        if len(args) >= 1:
            alarm_text = ' '.join(args)
            alarm_text = 'Your alert is:\n'+alarm_text
        if h is 0 and m is 0:
            bot.sendMessage(chat_id, text="At least 1 minute is needed.")
            return

        def alarm(bot, job):
            bot.sendMessage(job.context, text=beep, parse_mode=ParseMode.MARKDOWN)
            if alarm_text is not None:
                bot.sendMessage(job.context, text=alarm_text)
            job.schedule_removal()
            del timers[chat_id]

        # Add job to queue
        job = Job(alarm, to_seconds(h, m), repeat=False, context=chat_id)
        timers[chat_id] = job
        job_queue.put(job)

        bot.sendMessage(chat_id,
                        text='Timer successfully set! {0} hours and {1} minutes to your alert'.format(str(h), str(m)))

    except (IndexError, ValueError):
        bot.sendMessage(chat_id,
                        text='*Usage:* /timer m _[optional text]_\nor\t\t/timer h.m _[optional text]_',
                        parse_mode=ParseMode.MARKDOWN)


def cmd_timer_unset(bot, update):
    """Removes the job if the user changed their mind"""
    chat_id = update.message.chat_id

    if chat_id not in timers:
        bot.sendMessage(chat_id, text='You have no active timer.')
        return

    job = timers[chat_id]
    job.schedule_removal()
    del timers[chat_id]

    bot.sendMessage(chat_id, text='Timer stopped.')


def to_seconds(hours, minutes):
    return minutes*60+hours*3600
