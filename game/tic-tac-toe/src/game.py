class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to hold the board state
        self.current_player = 'X'  # Starting player

    def display_board(self):
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)               # Diagonal
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def start_game(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            self.display_board()
            try:
                position = int(input(f"Player {self.current_player}, enter your move (0-8): "))
                if position < 0 or position > 8:
                    print("Invalid position. Please enter a number between 0 and 8.")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 8.")
                continue

            if self.make_move(position):
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"Congratulations! Player {winner} wins!")
                    break
                if ' ' not in self.board:
                    self.display_board()
                    print("It's a tie!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
            else:
                print("Invalid move. The position is already taken. Try again.")

if __name__ == "__main__":
    game = Game()
    game.start_game()