import telebot
from telebot import types

token = "6319621239:AAE86PCnkC-VZTXBSfcrCftFS_8jHVVjtQU"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("задание 202"))
    keyboard.add(types.KeyboardButton("задание 204"))
    keyboard.add(types.KeyboardButton("задание 203"))

    bot.send_message(user_id, "ffijsifjs", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def start(message):
    user_text = message.text
    user_id = message.from_user.id
    if user_text == 'задание 202':
        message = (
        """

        Условные: найти самое большое число кратное 5 из последовательности

        Решение для задание 20.2 выглядит так:
        print("Введите n")
        n = int(input())

        max = 0
        for i in range(n):
            num = int(input())
            if num % 5 == 0 and num > max:
                max = num
        """) 
        bot.send_message(user_id, message)
        
    if user_text == 'задание 204':
        message = (
        """
        Условные: найти самое большое число кратное 5 из последовательности

        Решение для задание 20.2 выглядит так:
        print("Введите n")
        n = int(input())

        max = 0
        for i in range(n):
            num = int(input())
            if num % 5 == 0 and num > max:
                max = num
        """) 
        bot.send_message(user_id, message)

        print(max)
        bot.send_message(user_id, message)
            
    if user_text == 'задание 203':
        message = (
        """
        print("введите числа")

        n = int(input())

        nums = []

        for i in range(n):
            num = int(input())
            nums.append(num)

        nums2 = []
        length = len(nums)
        index = 0
        while length >= 0:
        nums2[index] = nums[length]
        length-=1
        index += 1

        print(nums2) 
        """) 
        bot.send_message(user_id, message)
        
bot.polling(none_stop=True, interval=0)
