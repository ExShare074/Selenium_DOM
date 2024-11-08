# Домашнее Задание. Написать программу, с помощью которой можно искать информацию на Википедии с помощью консоли.
# 1. Спрашивать у пользователя первоначальный запрос.
# 2. Переходить по первоначальному запросу в Википедии.
# 3. Предлагать пользователю три варианта действий:
# листать параграфы текущей статьи;
# перейти на одну из связанных страниц — и снова выбор из двух пунктов:
# - листать параграфы статьи;
# - перейти на одну из внутренних статей.
# выйти из программы.


from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki")
time.sleep(2)


def search():
    query = input("Введите ваш запрос: ")
    search_by =browser.find_element(By.ID, "searchInput").send_keys(query, Keys.ENTER)
    time.sleep(5)

    while True: # предлагаем варианты действий
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц — и снова выбор из двух пунктов:")
        print("3. Выйти из программы")
        action = input("Введите номер действия: ")

        if action == "1": # листать параграфы текущей статьи
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for i, paragraph in enumerate(paragraphs):
                print(f"{i + 1}. {paragraph.text}")
                if i<len(paragraphs)-1:
                    input("Нажмите Enter для перехода к следующему параграфу")

        elif action == "2": # перейти на одну из внутренних статей
            links = browser.find_elements(By.TAG_NAME, "a")
            related_links = [link for link in links if link.get_attribute("href") and "/wiki/" in link.get_attribute("href")]

            if not related_links:
                print("Связанные страницы не найдены.")
                continue

            print("Выберите одну из связанных страниц:")
            for i, link in enumerate(related_links[:3]): # предлагаем 3 варианта
                print(f"{i +1}. {link.text}")

            choice = input("Введите номер варианта: ")

            if choice.isdigit() and 1 <= int(choice) <= 3:
                related_link = related_links[int(choice) - 1]
                browser.get(related_link.get_attribute("href"))
                time.sleep(5)
            else:
             print("Некорректный ввод.")


        elif action == "3": # выйти из программы
            break

        else:
            print("Неверный выбор, попробуйте снова.")

search()





