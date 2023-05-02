from script import algo_color
from script import basic_fonction
from script import algo_duplication
from script import algo_frequency
from script import algo_missing

if __name__ == '__main__':
    game_type: str = ""
    game_data1 = None
    game_data2 = None
    card: dict = basic_fonction.open_json_card("card-5") #14

    game_type, game_data1, game_data2 = basic_fonction.recovery_data_card(card, game_type, game_data1, game_data2)

    if game_type == "couleur":
        algo_color.algo_color(game_data1)
    if game_type == "doublon":
        basic_fonction.calculate_time_execution(algo_duplication.algo_duplication, game_data1, 10000)
    if game_type == "fréquence":
        algo_frequency.algo_frequency(game_data1)
    if game_type == "manquant":
        algo_missing.algo_missing(game_data1)