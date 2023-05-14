""" File to initialize all the values for the functions """
import json
import time


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


def recovery_data_card(card: dict, game_type: str, game_data1, game_data2):
    """
    Function that allows retrieving all the data of the game
    :param card: A game card that contains all the information
    :param game_type: Variable containing the type of games
    :param game_data1:  Variable containing the game data
    :param game_data2:  Variable containing the game data
    :return: Returns the variable filled precedent
    """
    data_card: list = list(card)

    game_type = card[data_card[1]]
    game_data1 = card[data_card[2]]
    if len(card) > 3:
        game_data2 = card[data_card[3]]
    else:
        game_data2 = None
    return game_type, game_data1, game_data2


def calculate_time_execution(algorithm, game_data1, game_data2,  nb_iteration: int):
    """
    Function to calculate the average execution time for a number of iterations
    :param algorithm: Algorithm to be tested
    :param game_data1: First parameter of the algorithm
    :param game_data2: Second parameter of the algorithm
    :param nb_iteration: Number of test iterations
    :return: Average time
    """
    run_time: list = list()
    for i in range(nb_iteration):
        start = time.time()
        if game_data2 is not None:
            algorithm(game_data1, game_data2)
        else:
            algorithm(game_data1)
        end = time.time()
        run_time.append(end - start)

    # Calcule la moyenne des temps d'exécution
    average_time_run = sum(run_time) / len(run_time)

    print("Average run time : ", average_time_run)