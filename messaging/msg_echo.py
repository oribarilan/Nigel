from telegram import parsemode


def msg_echo_action(b, update):
    text = update.message.text
    answer = text
    if text == 'ping':
        answer = 'pong'
    b.sendMessage(chat_id=update.message.chat_id, text=answer, parse_mode=parsemode.ParseMode.MARKDOWN)
