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


def algo_color(dictionary_card: dict) -> str:
    """
    Compares each key-value pair (with the key translated in english) and returns the key which is identical with value
    :param dictionary_card: Dictionary whose key-value pairs have to be compared
    :return: The key of the pair which is identical to its value
    """
    for key, value in dictionary_card.items():
        key_translated = translate_word(key, "en", "fr")
        if key_translated == value:
            return key
