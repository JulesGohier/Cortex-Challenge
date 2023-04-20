""" File to initialize all the values for the functions """
import json


def open_json_card(file_name: str):
    """
    Function to open a json dictionary and put it in a dictionary
    :param file_name: Name of the json file
    :return: Return dictionary filled from json
    """
    with open(
            "./cortex_challenge_test/cards/" + file_name + ".json", "r", encoding="utf-8"
    ) as data_card_json:
        data_card: dict = json.load(data_card_json)

    return data_card


def recovery_data_card(card: dict):
    """
    Function that allows retrieving all the data of the game
    :param card: A game card that contains all the information
    :return: Returns the variable filled precedent
    """
    data_card: list = list(card)

    game_type: str = card[data_card[1]] # game_type: Variable containing the type of games
    game_data1 = card[data_card[2]] # game_data1: Variable containing the game data

    return game_type, game_data1


def recovery_data_card_special(card: dict):
    """
    Function that allows retrieving all the data of the game, specifically for calculation and reasoning algos
    :param card: A game card that contains all the information
    :return: Returns the variable filled precedent
    """
    data_card: list = list(card)

    game_type: str = card[data_card[1]]  # game_type: Variable containing the type of games
    game_data1 = card[data_card[2]]  # game_data1:  Variable containing the first game data
    game_data2 = card[data_card[3]]  # game_data2:  Variable containing the second game data

    return game_type, game_data1, game_data2
