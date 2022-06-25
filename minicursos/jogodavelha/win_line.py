verde = (0, 255, 0)

def win_line(window, board_array, end_game, X_or_O_turn, pg):
    
    newPosition = []

    if compare_line(board_array, 0):
        newPosition = [(30, 100),(570,100),10]
    elif compare_line(board_array, 1):
        newPosition = [(30,300), (570, 300), 10]
    elif compare_line(board_array, 2):
        newPosition = [(30,500), (570, 500), 10]
    elif condition_diagonal(board_array): 
        newPosition = [(100,30), (300, 580), 10]
    elif condition_column(board_array, 0):
        newPosition = [(500,30), (500, 580), 10]
    elif condition_column(board_array, 1):
        newPosition = [(30,30), (580, 580), 10]
    elif condition_column(board_array, 2):
        newPosition = [(580,30), (30, 580), 10]
    else:
        return end_game, X_or_O_turn
 
    return resolution_of_condition(pg, 1, 'x', newPosition)

def compare_line(board_array, number_of_line):
    return condition_compare_value_line(board_array, number_of_line, 'x') or condition_compare_value_line(board_array, number_of_line, 'o')

def condition_compare_value_line(board_array, value_of_line, game_type):
    return board_array[value_of_line][0] == game_type and board_array[value_of_line][1] == game_type and board_array[value_of_line][2] == game_type

def condition_column(board_array, number_of_column):
    return condition_compare_value_column(board_array, number_of_column, 'x') or condition_compare_value_column(board_array, number_of_column, 'o')

def condition_compare_value_column(board_array, value_of_column, game_type):
    return board_array[0][value_of_column] == game_type and board_array[1][value_of_column] == game_type and board_array[2][value_of_column] == game_type

def condition_compare_value_diagonal(board_array, game_type):
    return board_array[0][0] == game_type and board_array[1][1] == game_type and board_array[2][2] == game_type

def condition_diagonal(board_array):
    return condition_compare_value_diagonal(board_array, 'x') or condition_compare_value_diagonal(board_array, 'o')

def resolution_of_condition(pg, end_game, X_or_O_turn, newPosition):
    pg.draw.line(
        window, 
        verde, 
        newPosition[0], 
        newPosition[1], 
        newPosition[2]
    )

    end_game = 1
    X_or_O_turn = 'x'

    return end_game, X_or_O_turn
