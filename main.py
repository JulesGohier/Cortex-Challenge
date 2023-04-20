from script import algo_color
from script import basic_fonction
from script import algo_calculation

if __name__ == '__main__':
    #challenge 1 -> color
    game_type: str = ""
    game_data1: dict = dict()
    card: dict = basic_fonction.open_json_card("card-1")

    game_type, game_data1 = basic_fonction.recovery_data_card(card)
    algo_color.algo_color(game_data1)


    #challenge 2 -> calculation
    game_type_2: str = ""
    game_data2_1: int = 0
    game_data2_2: list = []
    card: dict = basic_fonction.open_json_card("card-3")

    game_type, game_data2_1, game_data2_2 = basic_fonction.recovery_data_card_special(card)
    print(algo_calculation.algo_calculation(game_data2_2, game_data2_1))





