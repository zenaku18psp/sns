from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def close_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def supp_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_9"],
                url=SUPPORT_CHAT,
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
