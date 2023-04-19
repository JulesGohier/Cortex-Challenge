from script import algo_color
from script import basic_fonction

if __name__ == '__main__':
    game_type: str = ""
    game_data1: dict = dict()
    card: dict = basic_fonction.open_json_card("card-10")

    game_type, game_data1 = basic_fonction.recovery_data_card(card, game_type, game_data1)
    algo_color.algo_color(game_data1)
