def print_board(board):
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([spot != " " for row in board for spot in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    
    while True:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))
        
        if board[row][col] == " ":
            board[row][col] = players[current_player]
        else:
            print("That spot is already taken. Try again.")
            continue
        
        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player  # Switch player

if __name__ == "__main__":
    tic_tac_toe()
