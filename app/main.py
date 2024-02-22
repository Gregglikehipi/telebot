from bot import bot
import time
from receiver import *


@bot.message_handler(commands=["start"])
def handle_role_selection(message):
    bot.send_message(message.chat.id, 'Есть 9 команд:\n'
                                      '/start получить список команд\n'
                                      '/add добавить товар в базу API по ID\n'
                                      '/get получить товар из API по ID\n'
                                      '/getAll получить все товары из API по ID\n'
                                      '/delete удалить товар из API по ID'
                                      '/minMax найти максимальную и минимальную цену за 6 месяцев'
                                      '/average найти разницу в цене товара и стредней по категории'
                                      '/countGroup найти количество товара по категориям'
                                      '/countAll найти количество всего товара'
                                      '/historyPrice найти динамику цены по товару')

@bot.message_handler(commands=["add"])
def add_command(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_id_add)

def write_id_add(message):
    api_add(int(message.text))
    bot.send_message(message.chat.id, 'Добавлено')

@bot.message_handler(commands=["get"])
def get_command(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_id_get)

def write_id_get(message):
    ans = api_get(int(message.text))
    bot.send_message(message.chat.id, 'Есть 5 команды:\n')

@bot.message_handler(commands=["getAll"])
def getAll_command(message):
    bot.send_message(message.chat.id, 'Товары')
    ans = api_get_all()

@bot.message_handler(commands=["delete"])
def delete_command(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_id_delete)

def write_id_delete(message):
    api_delete(int(message.text))
    bot.send_message(message.chat.id, 'Удаленно')

@bot.message_handler(commands=["minMax"])
def statistic_minMax(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_statistic_minMax)

def write_statistic_minMax(message):
    ans = api_priceHistory(int(message.text))
    bot.send_message(message.chat.id, 'Есть 5 команды:\n')

@bot.message_handler(commands=["average"])
def statistic_average(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_statistic_average)

def write_statistic_average(message):
    ans = api_priceHistory(int(message.text))
    bot.send_message(message.chat.id, 'Есть 5 команды:\n')

@bot.message_handler(commands=["priceHistory"])
def statistic_priceHistory(message):
    bot.send_message(message.chat.id, 'Введите ID товара')
    bot.register_next_step_handler(message, write_statistic_priceHistory)

def write_statistic_priceHistory(message):
    ans = api_priceHistory(int(message.text))
    bot.send_message(message.chat.id, 'Есть 5 команды:\n')

@bot.message_handler(commands=["countGroup"])
def statistic_countGroup(message):
    bot.send_message(message.chat.id, 'Введите ID группы')
    bot.register_next_step_handler(message, write_statistic_countGroup)

def write_statistic_countGroup(message):
    ans = api_priceHistory(int(message.text))
    bot.send_message(message.chat.id, 'Есть 5 команды:\n')

@bot.message_handler(commands=["countAll"])
def statistic_countAll(message):
    ans = api_priceHistory(int(message.text))
    bot.send_message(message.chat.id, 'Количество товара')



while True:
    try:
        bot.polling()
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)