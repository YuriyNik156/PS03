# Сейчас игра получает английское слово и английское определение.
# Сделайте так, чтобы слова и определения этих слов были на русском.

import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_words = soup.find("div", id = "random_word").text.strip()
        word_definition = soup.find("div", id = "random_word_definition").text.strip()

        translated_word = GoogleTranslator(source='en', target='ru').translate(english_words)
        translated_definition = GoogleTranslator(source='en', target='ru').translate(word_definition)

        return {
            "english_words" : english_words,
            "translated_word" : translated_word,
            "translated_definition" : translated_definition
        }
    except:
        print("Произошла ошибка")

def word_game():
    print("Добро пожаловать в игру")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            continue

        word = word_dict.get("translated_word")
        word_definition = word_dict.get("translated_definition")

        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ").strip().lower()
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        play_again = input("Хотите сыграть еще раз? д/н").strip().lower()
        if play_again != "д":
            print("Спасибо за игру!")
            break

word_game()