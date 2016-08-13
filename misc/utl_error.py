import logging

logger = logging.getLogger('__main__')


def utl_error_action(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))
