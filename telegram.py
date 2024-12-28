from config import TELEGRAM_BOT_TOKEN, CHAT_ID
from printer import print_ok, print_receipt, print_plain
from utils import check_internet, poweroff
import telebot
import time

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def send_startup_message():
    bot.send_message(CHAT_ID, "The server has started successfully!")

@bot.message_handler(commands=['health'])
def send_health_check(message):
    try:
        print_ok()
        bot.reply_to(message, 'Alhamdulillah sehat')
    except Exception as e:
        bot.reply_to(message, f'error: {e}')
        
@bot.message_handler(commands=['poweroff'])
def send_health_check(message):
    try:
        bot.reply_to(message, 'Shutting Down System')
        print_plain("System Off.")
        poweroff()
    except Exception as e:
        bot.reply_to(message, f'error: {e}')
        
# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        # bot.reply_to(message, "Successfully printed")
        if message.text[:7] == "[plain]":
            print(message.text)
            err, msg = print_plain(message.text[7:])
            if not err :
                bot.reply_to(message, "Successfully printed")
            else:  
                bot.reply_to(message, f"Unsuccess: {msg}")
                print(msg)  
        else:
            err, msg = print_receipt(message.text)
            if not err :
                bot.reply_to(message, "Successfully printed")
            else:  
                bot.reply_to(message, f"Unsuccess: {msg}")
                print(msg)  
    except Exception as e:
        bot.reply_to(message, f"Unsuccess: {e}")
        print(e)

def start_bot():
    retry_count = 0
    if check_internet():
        print_plain("Internet OK.")
    else:
        print_plain("No internet connection.")
        while retry_count < 50:
            if check_internet():
                print_plain("Internet OK.")
                break
            time.sleep(10)
        else:
            print_plain("Internet gagal tersambung. Cabut sumber daya dan sambungkan kembali setelah Wi-Fi dapat diakses.")
            print_plain("System Off.") 
            poweroff()
        
    send_startup_message()
    print_ok()
    bot.polling()
