import os
import sqlite3
from pyrogram import (
    Client,
    Filters,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


@pyrogram.Client.on_message(pyrogram.Filters.command(["home"]))
async def start(bot, update):
    # logger.info(update)
    #TRChatBase(update.from_user.id, update.text, "/home")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Config.START_TEXT.format(update.from_user.first_name, Config.USER_NAME), 
        parse_mode="html",
        reply_to_message_id=update.message_id,
        reply_markup=InlineKeyboardMarkup(
        [
          [
          InlineKeyboardButton('📫 UPDATES', url='https://t.me/Ts_bots'),
          InlineKeyboardButton('📕 ABOUT ME', callback_data='about')
          ],
          [
          InlineKeyboardButton('💡 HELP', callback_data="help"),
          InlineKeyboardButton('🔐 CLOSE', callback_data="close")
          ]
        ]
      )
    )
