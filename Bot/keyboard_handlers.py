from JsonGetter import JSON

from telebot.types import LabeledPrice, PreCheckoutQuery

config_getter = JSON()
_, _, PAYMENTS_PROVIDER_TOKEN, PROMOTION_SUBSCRIPTION_TITLE, PROMOTION_SUBSCRIPTION_DESCRIPTION, PRICE = config_getter()
ACCOUNT_PRICE = LabeledPrice(label='Promotion subscribe price', amount=PRICE)


def info_handler(bot, message):
    with open('info_message.txt', 'r', encoding='UTF-8') as file:
        info = file.read()
    bot.send_message(message.chat.id, info, parse_mode="html")


# ----------------------------------------------------------------------------------------------------------------------
def amount_accounts_handler(bot, message):
    def get_pay_way_step_handler(content):
        amount = content.text

    get_amount_msg = bot.send_message(message.chat.id, 'Отправьте кол-во аккаунтов для покупки:', parse_mode="html")
    bot.register_next_step_handler(get_amount_msg, get_pay_way_step_handler)

# ----------------------------------------------------------------------------------------------------------------------
