import time
import threading
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import telebot

# Ваш токен бота
bot = telebot.TeleBot('YOUR_TOKEN')
items_archive = []


def is_dict_in_list(dictionary, list_of_dictionaries, key):
    for d in list_of_dictionaries:
        if d.get(key) == dictionary.get(key):
            return True
    return False


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Старт')


updates = bot.get_updates()
chat_id = updates[0].message.chat.id


def search_loop():
    ser = Service('chromedriver.exe')
    driver = Chrome(service=ser)
    while True:
        try:
            # Сылка на интересующую группу товаров Авито
            driver.get('YOUR_LINK')
            news_elements = driver.find_elements(By.CLASS_NAME, "iva-item-body-KLUuy")
            for x in news_elements:
                des = x.find_element(By.CLASS_NAME, 'iva-item-descriptionStep-C0ty1')
                title = x.find_element(By.CLASS_NAME, 'title-root-zZCwT')
                price = x.find_element(By.CLASS_NAME, 'price-text-_YGDY')
                url_inner = x.find_element(By.CLASS_NAME, 'link-link-MbQDP')
                url = url_inner.get_attribute('href')
                checklist = (
                    # Ключи для поиска в теле объявления
                    'KEY1', 'KEY2', 'KEY3')
                for itm in checklist:
                    if itm in des.text.lower():
                        item = {
                            'title': title.text,
                            'price': price.text,
                            'desc': des.text,
                            'url': url
                        }
                        if not is_dict_in_list(item, items_archive, 'url'):
                            print(item['title'])
                            print(item['price'])
                            print(item['desc'])
                            print(item['url'])
                            bot.send_message(chat_id, f"Цена: {item['price']}\n-------\n{item['url']}")
                            items_archive.insert(0, item)
                            if len(items_archive) > 40:
                                items_archive.pop(-1)
            time.sleep(300)
            print("Новый поиск")
        except Exception as ex:
            print(ex)


search_thread = threading.Thread(target=search_loop)
search_thread.start()
bot.polling(none_stop=True, interval=0)
