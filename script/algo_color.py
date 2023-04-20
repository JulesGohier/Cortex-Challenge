""" This python program allows to solve the color challenge of the cortex game """
from googletrans import Translator

"""
DISCLAIMER : you need to replace the line 222 of googletrans/client.py with :

try:
translated_parts=list(map(lambda part: TranslatedPart(part[0], part[1] if len(part) >= 2 else []), parsed[1][0][0][5]))
except TypeError: # because of the gender-specific translate results
    translated_parts = [ TranslatedPart(parsed[1][0][1][0], [parsed[1][0][0][0], parsed[1][0][1][0]]) ]
    
"""


translator = Translator()


def translate_word(word: str, la1: str, la2: str) -> str:
    """
    A function that translate a word from a targeted language to the desired language
    :param word: word to translate
    :param la1: language to translate into
    :param la2: language source
    :return: the word translated in the desired language
    """
    translation = translator.translate(word, dest=la1, src=la2)
    new_key: str = translation.text
    new_key = new_key.lower()
    return new_key


def translate_dictionary_keys(dictionary_to_translate: dict) -> dict:
    """
    A function that translate all the key of a dictionary if they are not, and return a new dictionary
    :param dictionary_to_translate:
    :return: the dictionary with all his pairs key-value translated in english
    """
    dictionary_translated: dict = {}
    for key, value in dictionary_to_translate.items():
        new_key: str = translate_word(key, "en", "fr")
        dictionary_translated[new_key] = value

    return dictionary_translated


def compare_keys_values(dictionary: dict) -> str:
    """
    A function that compares each key-value pair and return the key which is identical with its value
    :param dictionary: Dictionary whose key-value pairs have to be compared
    :return: The key of the pair which is identical
    """
    for key, value in dictionary.items():
        if key == value:
            new_key: str = translate_word(key, "fr", "en")
            return print(new_key)

    return print("No value found")


def algo_color(dictionary_card: dict) -> str:
    """
    This function allows you to solve the colour challenge
    :param dictionary_card: the dictionary from the challenge card selected
    :return: The word or key of the element that is identical in both dictionaries
    """
    dictionary_translated = translate_dictionary_keys(dictionary_card)
    return compare_keys_values(dictionary_translated)
