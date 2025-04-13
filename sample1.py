import os

from dotenv import load_dotenv

from bale import (
    Bot,
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    MenuKeyboardMarkup,
    MenuKeyboardButton,
)

# Load environment variables from .env file
load_dotenv()

client = Bot(token=os.environ.get("BOT_TOKEN"))


@client.event
async def on_ready():
    print(client.user, "is Ready!")


@client.event
async def on_message(message: Message):
    if message.content == "/start":
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(
            InlineKeyboardButton(
                text="چه کاری میتونم براتون انجام بدم؟",
                callback_data="python-bale-bot:help",
            )
        )
        reply_markup.add(
            InlineKeyboardButton(
                text="سایت بله",
                url="https://web.bale.ai/",
            ),
            row=2,
        )
        reply_markup.add(
            InlineKeyboardButton(
                text="سایت گوگل",
                url="http://google.com/",
            ),
            row=2,
        )
        reply_markup.add(
            InlineKeyboardButton(
                text="کارهای دیگه",
                callback_data="others",
            ),
            row=3,
        )
        await message.reply(
            f"*سلام، به بات من خوش آمدید*",
            components=reply_markup,
        )

    elif message.content == "/keyboard":
        await message.reply(
            f"*سلام، به بات من خوش آمدید*",
            components=MenuKeyboardMarkup()
            .add(MenuKeyboardButton("سایت بله"))
            .add(MenuKeyboardButton("سایت گوگل")),
        )

    elif message.content in ["سایت بله", "سایت گوگل"]:
        await message.reply(
            "{} is {}".format(
                message.content,
                {
                    "سایت بله": "https://web.bale.ai/",
                    "سایت گوگل": "http://google.com/",
                }[message.content],
            ),
            components=MenuKeyboardMarkup(),
        )


@client.event
async def on_callback(callback: CallbackQuery):
    if callback.data == "python-bale-bot:help":
        await callback.message.reply("کمکی از دست من برنمیاد!")
    elif callback.data == "others":
        reply_markup = InlineKeyboardMarkup()
        reply_markup.add(
            InlineKeyboardButton(
                text="بیا تا گل برافشانیم و می در ساغر اندازیم",
                callback_data="gol barafshanim",
            ),
            row=1,
        )
        reply_markup.add(
            InlineKeyboardButton(
                text="فلک را سقف بشکافیم و طرحی نو براندازیم",
                callback_data="tarh noo",
            ),
            row=2,
        )

        await callback.message.reply(
            f"*بازم میتونی انتخاب کنی*",
            components=reply_markup,
        )
    elif callback.data == "gol barafshanim":
        await callback.message.reply("عه خبب باشه!")

    elif callback.data == "چقدر عااالی!!":
        pass


client.run()
