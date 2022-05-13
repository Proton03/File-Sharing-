#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>υηιту вяσ</a>\n○ Unity Member: 🛡 This Bot will Help you to get Best Digital Marketing and Trading Contents 🌴 \n ✍🏻 𝗖𝗼𝗽𝘆 & 𝗙𝗼𝗿𝘄𝗮𝗿𝗱𝗶𝗻𝗴 is off Due to Copyrigh€ Issues \n ⚔️ All 10k+ Content Course are available in our Membership must Read this 👉🏻👉🏻 \n 🔗<a href="https://telegra.ph/Unity-Premium-Membership-05-13">Click Me</a> </code>\n○ Support Channel : @MegaUnityGroup</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
