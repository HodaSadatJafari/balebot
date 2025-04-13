import os

from dotenv import load_dotenv

from bale import (
    Bot,
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

# Load environment variables from .env file
load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))


# Define the main menu
def main_menu():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Menu 1", callback_data="menu1")
    button2 = InlineKeyboardButton("Menu 2", callback_data="menu2")
    markup.add(button1, row=1)
    markup.add(button2, row=2)
    return markup


# Define the submenus for Menu 1
def submenu1():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Submenu 1-1", callback_data="submenu1-1")
    button2 = InlineKeyboardButton("Submenu 1-2", callback_data="submenu1-2")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_main")
    markup.add(button1, row=1)
    markup.add(button2, row=1)
    markup.add(return_button, row=2)
    return markup


def submenu1_1():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 1-1", callback_data="button")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_submenu1")
    markup.add(button, row=1)
    markup.add(return_button, row=2)
    return markup


def submenu1_2():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 1-2", callback_data="button")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_submenu1")
    markup.add(button, row=1)
    markup.add(return_button, row=2)

    return markup


# Define the submenus for Menu 2
def submenu2():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Submenu 2-1", callback_data="submenu2-1")
    button2 = InlineKeyboardButton("Submenu 2-2", callback_data="submenu2-2")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_main")
    markup.add(button1, row=1)
    markup.add(button2, row=1)
    markup.add(return_button, row=2)

    return markup


def submenu2_1():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 2-1", callback_data="button")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_submenu2")
    markup.add(button, row=1)
    markup.add(return_button, row=2)

    return markup


def submenu2_2():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 2-2", callback_data="button")
    return_button = InlineKeyboardButton("Return", callback_data="return_to_submenu2")
    markup.add(button, row=1)
    markup.add(return_button, row=2)

    return markup


@bot.event
async def on_ready():
    print(bot.user, "is Ready!")


@bot.event
async def on_message(message: Message):
    if message.content == "/start":
        await message.reply(
            "You are in main menu. Choose an option:",
            components=main_menu(),
        )


# Callback query handler
@bot.event
async def on_callback(call: CallbackQuery):
    if call.data == "menu1":
        await call.message.reply(
            text="You are in menu1",
            components=submenu1(),
        )

    elif call.data == "submenu1-1":
        await call.message.reply(
            text="You are in submenu1-1",
            components=submenu1_1(),
        )

    elif call.data == "submenu1-2":
        await call.message.reply(
            text="You are in submenu1-2",
            components=submenu1_2(),
        )

    elif call.data == "menu2":
        await call.message.reply(
            text="You are in menu2",
            components=submenu2(),
        )

    elif call.data == "submenu2-1":
        await call.message.reply(
            text="You are in submenu2-1",
            components=submenu2_1(),
        )

    elif call.data == "submenu2-2":
        await call.message.reply(
            text="You are in submenu2-2",
            components=submenu2_2(),
        )

    elif call.data == "return_to_main":
        await call.message.reply(
            text="You are in main menu. Choose an option:",
            components=main_menu(),
        )

    elif call.data == "return_to_submenu1":
        await call.message.reply(
            text="You are in submenu1",
            components=submenu1(),
        )

    elif call.data == "return_to_submenu2":
        await call.message.reply(
            text="You are in submenu2",
            components=submenu2(),
        )


bot.run()
