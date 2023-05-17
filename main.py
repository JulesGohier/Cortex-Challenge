from script import basic_function
from script import algo_color
from script import algo_reflection
from script import algo_calculate
from script import algo_frequency
from script import algo_missing
from script import algo_labyrinth
from script import algo_duplication
from script import algo_reasoning


if __name__ == '__main__':
    # game_type: str = ""
    # game_data1 = None
    # game_data2 = None
    card: dict = basic_function.open_json_card("card-7")

    game_type, game_data1, game_data2 = basic_function.recovery_data_card(card)

    if game_type == "couleur":
        print(algo_color.algo_color(game_data1))
        basic_function.calculate_time_execution(algo_color.algo_color, game_data1, game_data2, 100000)

    if game_type == "réflexion":
        print(algo_reflection.algo_reflection(game_data1))
        basic_function.calculate_time_execution(algo_reflection.algo_reflection, game_data1, game_data2, 100000)

    if game_type == "calcul":
        print(algo_calculate.algo_calculate(game_data1, game_data2))
        basic_function.calculate_time_execution(algo_calculate.algo_calculate, game_data1, game_data2, 100000)

    if game_type == "fréquence":
        print(algo_frequency.algo_frequency(game_data1))
        basic_function.calculate_time_execution(algo_frequency.algo_frequency, game_data1, game_data2, 100000)

    if game_type == "manquant":
        print(algo_missing.algo_missing(game_data1))
        basic_function.calculate_time_execution(algo_missing.algo_missing, game_data1, game_data2, 100000)

    if game_type == "labyrinthe":
        print(algo_labyrinth.algo_labyrinth(game_data1))
        basic_function.calculate_time_execution(algo_labyrinth.algo_labyrinth, game_data1, game_data2, 100000)

    if game_type == "doublon":
        print(algo_duplication.algo_duplication(game_data1))
        basic_function.calculate_time_execution(algo_duplication.algo_duplication, game_data1, game_data2, 100000)

    if game_type == "raisonnement":
        print(algo_reasoning.algo_reasoning(game_data1, game_data2))
        basic_function.calculate_time_execution(algo_reasoning.algo_reasoning, game_data1, game_data2, 100000)
