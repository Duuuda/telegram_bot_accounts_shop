from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Main_keyboard---------------------------------------------------------------------------------------------------------
# Commands
MAIN_COMMAND_INFO = 'информация'
MAIN_COMMAND_BUY = 'buy accounts'
# Init_keyboard
MAIN_MARKUP = ReplyKeyboardMarkup(resize_keyboard=True)
# Init_buttons
MAIN_BUTTON_INFO = KeyboardButton(MAIN_COMMAND_INFO)
MAIN_BUTTON_BUY = KeyboardButton(MAIN_COMMAND_BUY)
# Add_buttons
MAIN_MARKUP.add(MAIN_BUTTON_INFO)
MAIN_MARKUP.add(MAIN_BUTTON_BUY)
# ----------------------------------------------------------------------------------------------------------------------

# Inline_keyboards------------------------------------------------------------------------------------------------------
# Inline_main_keyboard--------------------------------------------------------------------------------------------------
# Commands
INLINE_COMMAND_PAY_BITCOIN = 'Pay Bitcoin'
INLINE_COMMAND_PAY_CARDS = 'Pay Cards'
# Init_keyboard
INLINE_PAY_MARKUP = InlineKeyboardMarkup(row_width=1)
# Init_buttons
INLINE_BUTTON_PAY_BITCOIN = InlineKeyboardButton(INLINE_COMMAND_PAY_BITCOIN,
                                                 callback_data=INLINE_COMMAND_PAY_BITCOIN)
INLINE_BUTTON_PAY_CARDS = InlineKeyboardButton(INLINE_COMMAND_PAY_CARDS,
                                               callback_data=INLINE_COMMAND_PAY_CARDS)
# Add_buttons
INLINE_PAY_MARKUP.add(INLINE_BUTTON_PAY_BITCOIN, INLINE_BUTTON_PAY_CARDS)
# ----------------------------------------------------------------------------------------------------------------------
