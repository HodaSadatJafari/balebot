import os

from dotenv import load_dotenv

from bale import (
    Bot,
    CallbackQuery,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
import requests

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"  # OPTIONAL: Change model (gpt-4, etc.)
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")

bot = Bot(token=os.environ.get("BOT_TOKEN"))

users_word = {}


def call_openai(user_prompt: str):
    # call chatGPT

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a English teacher. You help students to learn new English worlds.",
            },
            {
                "role": "user",
                "content": user_prompt or f"What is the meaning of {user_prompt}",
            },
        ],
        "temperature": 0.7,
    }
    response = response = requests.post(
        OPENAI_BASE_URL,
        headers=headers,
        json=data,
    )

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code}, {response.text}")
    return None


# Define the main menu
def main_menu():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("وارد کردن لغت", callback_data="menu1")
    button2 = InlineKeyboardButton("پیشنهاد لغت", callback_data="menu2")
    markup.add(button1, row=1)
    markup.add(button2, row=2)
    return markup


# Define the submenus for Menu 1
def submenu1():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("مترادف ها", callback_data="submenu1-1")
    button2 = InlineKeyboardButton("متضاد ها", callback_data="submenu1-2")
    button3 = InlineKeyboardButton("توضیح فارسی", callback_data="submenu1-3")
    button4 = InlineKeyboardButton("توضیح انگلیسی", callback_data="submenu1-4")

    return_button = InlineKeyboardButton("بازگشت", callback_data="return_to_main")
    markup.add(button1, row=1)
    markup.add(button2, row=1)
    markup.add(button3, row=2)
    markup.add(button4, row=2)
    markup.add(return_button, row=3)
    return markup


def submenu1_1(input: str):
    # Call chatgpt API and return its answer
    user_prompt = f"for the word {input}, list at least 10 synonyms and categorize them by common usage (formal, informal, academic, slang, etc.)."
    user_prompt += " The user should not know that You are a trained model. Just answer the question."
    return call_openai(user_prompt)


def submenu1_2():
    return "Call chatgpt API submenu1_2"


def submenu1_3():
    return "Call chatgpt API submenu1_3"


def submenu1_4():
    return "Call chatgpt API submenu1_4"


# Define the submenus for Menu 2
def submenu2():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("A1", callback_data="submenu2-1")
    button2 = InlineKeyboardButton("A2", callback_data="submenu2-2")
    button3 = InlineKeyboardButton("B1", callback_data="submenu2-3")
    button4 = InlineKeyboardButton("B2", callback_data="submenu2-4")
    button5 = InlineKeyboardButton("C1", callback_data="submenu2-5")
    button6 = InlineKeyboardButton("C2", callback_data="submenu2-6")

    return_button = InlineKeyboardButton("بازگشت", callback_data="return_to_main")
    markup.add(button1, row=1)
    markup.add(button2, row=1)
    markup.add(button3, row=2)
    markup.add(button4, row=2)
    markup.add(button5, row=3)
    markup.add(button6, row=3)
    markup.add(return_button, row=4)

    return markup


def submenu2_1():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 2-1", callback_data="button")
    return_button = InlineKeyboardButton("بازگشت", callback_data="return_to_submenu2")
    markup.add(button, row=1)
    markup.add(return_button, row=2)

    return markup


def submenu2_2():
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Button in 2-2", callback_data="button")
    return_button = InlineKeyboardButton("بازگشت", callback_data="return_to_submenu2")
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
            "یک گزینه را انتخاب کنید:",
            components=main_menu(),
        )
    else:
        answer_obj: Message = message
        users_word[answer_obj.from_user.id] = answer_obj.content
        await message.reply(
            text=f"کلمه شما {answer_obj.content} است. یک گزینه را انتخاب کنید:",
            components=submenu1(),
        )


# Callback query handler
@bot.event
async def on_callback(call: CallbackQuery):
    if call.data == "menu1":
        await call.message.reply("کلمه مورد نظر خود را تایپ کنید:")
    elif call.data == "submenu1-1":
        await call.message.reply(
            text=submenu1_1(users_word[call.from_user.id]),
            components=submenu1(),
        )

    elif call.data == "submenu1-2":
        await call.message.reply(submenu1_2())

    elif call.data == "submenu1-3":
        await call.message.reply(submenu1_3())

    elif call.data == "submenu1-4":
        await call.message.reply(submenu1_4())

    elif call.data == "menu2":
        await call.message.reply(
            text="تعیین سطح",
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
            text="یک گزینه را انتخاب کنید:",
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
