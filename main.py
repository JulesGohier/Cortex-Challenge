from script import algo_color
from script import basic_fonction
from script import algo_duplication

if __name__ == '__main__':
    game_type: str = ""
    game_data1 = ""
    game_data2 = ""
    card: dict = basic_fonction.open_json_card("card-7")

    game_type, game_data1, game_data2 = basic_fonction.recovery_data_card(card, game_type, game_data1, game_data2)

    if game_type == "couleur":
        algo_color.algo_color(game_data1)
    if game_type == "doublon":
        algo_duplication.algo_duplication(game_data1)
    else:
        print("NONE")
