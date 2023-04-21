from script import basic_fonction
from script import algo_color
from script import algo_calculation
from script import algo_frequency
from script import algo_missing
from script import algo_duplication


if __name__ == '__main__':
    """
    # challenge 1 -> color
    game_type_1: str = ""
    game_data1_1: dict = dict()
    game_data1_2: str = ""
    card: dict = basic_fonction.open_json_card("card-1")

    game_type_1, game_data1_1, game_data1_2 = basic_fonction.recovery_data_card(card)
    print("/", game_type_1, " : ")
    algo_color.algo_color(game_data1_1)
    """

    # challenge 3 -> calculation
    game_type_3: str = ""
    game_data3_1: int = 0
    game_data3_2: list = []
    card: dict = basic_fonction.open_json_card("card-3")

    game_type_3, game_data3_1, game_data3_2 = basic_fonction.recovery_data_card(card)
    print("/", game_type_3, " : ")
    print(algo_calculation.algo_calculation(game_data3_2, game_data3_1))

    # challenge 4 -> frequency
    game_type_4: str = ""
    game_data4_1 = None
    game_data4_2: str = ""
    card: dict = basic_fonction.open_json_card("card-4")

    game_type_4, game_data4_1, game_data4_2 = basic_fonction.recovery_data_card(card)
    print("/", game_type_4, " : ")
    algo_frequency.algo_frequency(game_data4_1)


    # challenge 5 -> missing
    game_type_5: str = ""
    game_data5_1: dict = dict()
    game_data5_2: str = ""
    card: dict = basic_fonction.open_json_card("card-5")

    game_type_5, game_data5_1, game_data5_2 = basic_fonction.recovery_data_card(card)
    print("/", game_type_5, " : ")
    algo_missing.algo_missing(game_data5_1)

    # challenge 7 -> duplication
    game_type_7: str = ""
    game_data7_1 = None
    game_data7_2: str = ""
    card: dict = basic_fonction.open_json_card("card-7")

    game_type_7, game_data7_1, game_data7_2 = basic_fonction.recovery_data_card(card)
    print("/", game_type_7, " : ")
    algo_duplication.algo_duplication(game_data7_1)





