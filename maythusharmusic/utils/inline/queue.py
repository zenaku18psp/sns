from typing import Union
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur_buttons = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    
    # Choose which button set to use based on DURATION
    buttons = not_dur if DURATION == "Unknown" else dur_buttons
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def queue_back_markup(_, CPLAY):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data=f"queue_back_timer {CPLAY}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
