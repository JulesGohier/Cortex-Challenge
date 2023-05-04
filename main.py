from script import basic_function
from script import algo_color
from script import algo_calculate
from script import algo_frequency
from script import algo_missing
from script import algo_labyrinth
from script import algo_duplication
from script import algo_reasoning


if __name__ == '__main__':

    # challenge 1 -> color
    game_type_1: str = ""
    game_data1_1: dict = dict()
    game_data1_2: str = ""
    card: dict = basic_function.open_json_card("card-1")

    game_type_1, game_data1_1, game_data1_2 = basic_function.recovery_data_card(card)
    print("/", game_type_1, " : ")
    print(algo_color.algo_color(game_data1_1))
    basic_function.calculate_time_execution(algo_color.algo_color, game_data1_1, 2)

    """
    # challenge 2 -> reflection
    game_type_2: str = ""
    game_data2_1 = None
    game_data2_2: str = ""
    card: dict = basic_function.open_json_card("card-2")

    game_type_2, game_data2_1, game_data2_2 = basic_function.recovery_data_card(card)
    print("/", game_type_2, " : ")
    print(algo_reflection.algo_reflection(game_data2_1))
    basic_function.calculate_time_execution(algo_reflection.algo_reflection, game_data2_1, 1000)
    """

    # challenge 3 -> calculate
    game_type_3: str = ""
    game_data3_1 = None
    game_data3_2 = None
    card: dict = basic_function.open_json_card("card-3")

    game_type_3, game_data3_1, game_data3_2 = basic_function.recovery_data_card(card)
    print("/", game_type_3, " : ")
    print(algo_calculate.algo_calculate(game_data3_2, game_data3_1))
    basic_function.calculate_time_execution2(algo_calculate.algo_calculate, game_data3_2, game_data3_1, 1000)


    # challenge 4 -> frequency
    game_type_4: str = ""
    game_data4_1 = None
    game_data4_2: str = ""
    card: dict = basic_function.open_json_card("card-4")

    game_type_4, game_data4_1, game_data4_2 = basic_function.recovery_data_card(card)
    print("/", game_type_4, " : ")
    print(algo_frequency.algo_frequency(game_data4_1))
    basic_function.calculate_time_execution(algo_frequency.algo_frequency, game_data4_1, 1000)
    

    # challenge 5 -> missing
    game_type_5: str = ""
    game_data5_1: dict = dict()
    game_data5_2: str = ""
    card: dict = basic_function.open_json_card("card-5")

    game_type_5, game_data5_1, game_data5_2 = basic_function.recovery_data_card(card)
    print("/", game_type_5, " : ")
    print(algo_missing.algo_missing(game_data5_1))
    basic_function.calculate_time_execution(algo_missing.algo_missing, game_data5_1, 1000)


    # challenge 6 -> labyrinth
    game_type_6: str = ""
    game_data6_1 = None
    game_data6_2 = None
    card: dict = basic_function.open_json_card("card-14")
    
    game_type_6, game_data6_1, game_data6_2 = basic_function.recovery_data_card(card)
    print("/", game_type_6, " : ")
    print(algo_labyrinth.algo_labyrinth(game_data6_1))
    basic_function.calculate_time_execution(algo_labyrinth.algo_labyrinth, game_data6_1, 1000)
    

    # challenge 7 -> duplication
    game_type_7: str = ""
    game_data7_1 = None
    game_data7_2: str = ""
    card: dict = basic_function.open_json_card("card-7")

    game_type_7, game_data7_1, game_data7_2 = basic_function.recovery_data_card(card)
    print("/", game_type_7, " : ")
    print(algo_duplication.algo_duplication(game_data7_1))
    basic_function.calculate_time_execution(algo_duplication.algo_duplication, game_data7_1, 1000)

    
    # challenge 8 -> reasoning
    game_type_8: str = ""
    game_data8_1 = None
    game_data8_2 = None
    card: dict = basic_function.open_json_card("card-16")

    game_type_8, game_data8_1, game_data8_2 = basic_function.recovery_data_card(card)
    print("/", game_type_8, " : ")
    print(algo_reasoning.algo_reasoning(game_data8_1, game_data8_2))
    basic_function.calculate_time_execution2(algo_reasoning.algo_reasoning, game_data8_1, game_data8_2, 1000)
