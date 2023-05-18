def main_game_logic():
    def get_player_position(matrix, player):
        for row_index, row_data in enumerate(matrix):
            if player in row_data:
                return row_index, row_data.index(player)

    rows, cols = 8, 8
    first_player, second_player = 'w', 'b'
    matrix = [input().split(' ') for _ in range(rows)]
    first_player_position = get_player_position(matrix, first_player)
    second_player_position = get_player_position(matrix, second_player)
    first_change, second_change = -1, + 1
    capture_condition, queen_condition = False, False

    while not queen_condition and not capture_condition:
        first_player_row, first_player_column = first_player_position
        second_player_row, second_player_column = second_player_position

        first_player_row += first_change
        first_player_position = (first_player_row, first_player_column)

        if first_player_row == second_player_row \
                and abs(first_player_column - second_player_column) == 1:
            capture_condition = True
            first_player_position = (first_player_row, second_player_column)
        elif first_player_row in [0, rows - 1]:
            queen_condition = True
        else:
            first_player_position, second_player_position \
                = second_player_position, first_player_position
            first_change, second_change = second_change, first_change
            first_player, second_player = second_player, first_player

    return first_player_position, first_player, capture_condition


def print_func(position_data, player_win, capture_condition):
    row, column = position_data
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    position_name = f'{column_names[column]}{row_names[row]}'
    if capture_condition:
        return f'Game over! {player_win} win, capture on {position_name}.'
    else:
        f'Game over! {player_win} is promoted to a queen at {position_name}'


position_data, first_player, capture_condition = main_game_logic()
player_win = 'White' if first_player == 'w' else 'Black'
print(print_func(position_data, player_win, capture_condition))
