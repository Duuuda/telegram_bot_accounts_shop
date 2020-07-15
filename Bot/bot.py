from telebot import TeleBot, apihelper
# ----------------------------------------------------------------------------------------------------------------------
from base64 import b64decode
import codecs
from threading import Thread
# ----------------------------------------------------------------------------------------------------------------------
from JsonGetter import JSON
# ----------------------------------------------------------------------------------------------------------------------
from Bot import MAIN_MARKUP, MAIN_COMMAND_INFO, MAIN_COMMAND_BUY,\
                INLINE_PAY_MARKUP, INLINE_COMMAND_PAY_BITCOIN, INLINE_COMMAND_PAY_CARDS,\
                info_handler, amount_accounts_handler


def start_up_bot():
    try:
        bot.polling(none_stop=True)
    except Exception as error:
        print(error)
        print('try to use/change proxy!')


# init_tools------------------------------------------------------------------------------------------------------------
config_getter = JSON()
TOKEN, *_ = config_getter()
# init_bot--------------------------------------------------------------------------------------------------------------
bot = TeleBot(TOKEN)
print('Bot was initialized!')
# ----------------------------------------------------------------------------------------------------------------------

# Slash_commands--------------------------------------------------------------------------------------------------------
SLASH_COMMAND_START_UP = ['start']
SLASH_COMMAND_ADMIN = ['admin']
SLASH_COMMAND_GET_SELF_ID = ['id', 'get_id', 'get_self_id']
# ----------------------------------------------------------------------------------------------------------------------
# Global_variable-------------------------------------------------------------------------------------------------------
ALL_CONTENT_TYPES = ['audio', 'photo', 'voice', 'video', 'document', 'text', 'location', 'contact', 'sticker']
# ----------------------------------------------------------------------------------------------------------------------


# getting_commands_and_handle-------------------------------------------------------------------------------------------
@bot.message_handler(commands=SLASH_COMMAND_START_UP)
def starting(message):
    bot.send_message(message.chat.id,
                     f'Добро пожаловать, {message.from_user.first_name}!\n' +
                     f'Я - <b>{bot.get_me().first_name}</b>, бот созданный для тестов.',
                     parse_mode="html", reply_markup=MAIN_MARKUP)


# @bot.message_handler(commands=SLASH_COMMAND_ADMIN)
# def admin(message):
#     bot.send_message(message.chat.id, "Выберете действие: ", parse_mode="html")


@bot.message_handler(commands=SLASH_COMMAND_GET_SELF_ID)
def get_id(message):
    bot.send_message(message.chat.id, str(message.chat.id), parse_mode="html")
# ----------------------------------------------------------------------------------------------------------------------


# getting_all_message_and_send_to_handle--------------------------------------------------------------------------------
@bot.message_handler(content_types=ALL_CONTENT_TYPES)
def all_message_getter(message):
    message.text = message.text.lower()
    if message.chat.type == 'private':
        if MAIN_COMMAND_INFO in message.text:
            info_handler(bot, message)
        elif MAIN_COMMAND_BUY in message.text:
            amount_accounts_handler(bot, message)
        else:
            bot.send_message(message.chat.id, 'Я не понимаю:(', parse_mode="html")
# ----------------------------------------------------------------------------------------------------------------------
