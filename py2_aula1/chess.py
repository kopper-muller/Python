class ChessBoard:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        # Create an 8x8 board
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Place pieces on the board
        # For simplicity, let's represent pieces with their initials
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[1] = ['P'] * 8
        board[6] = ['p'] * 8
        board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        return board

    def display_board(self):
        print("   a b c d e f g h")
        print("  +-----------------+")
        for i in range(7, -1, -1):  # Print rows in reverse order
            print(f"{i + 1} | {' '.join(self.board[i])} |")
        print("  +-----------------+")

    def move_piece(self, start, end):
        start_row, start_col = self.translate_position(start)
        end_row, end_col = self.translate_position(end)
        piece = self.board[start_row][start_col]
        if self.is_valid_move(piece, start_row, start_col, end_row, end_col):
            self.board[start_row][start_col] = ' '
            self.board[end_row][end_col] = piece
            return True
        else:
            return False

    def translate_position(self, pos):
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        row = int(pos[1]) - 1
        col = col_map[pos[0]]
        return row, col

    def is_valid_move(self, piece, start_row, start_col, end_row, end_col):
        # Add movement logic for each piece
        # For simplicity, let's assume all moves are valid for now
        return True


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'

    def play(self):
        while True:
            self.board.display_board()
            print(f"\n{self.current_player}'s turn:")
            move = input("Enter your move (e.g., 'e2 e4'): ")
            if move == 'exit':
                print("Exiting the game.")
                break
            if not self.is_valid_input(move):
                print("Invalid input. Please enter a move in the format 'e2 e4'.")
                continue
            start, end = move.split()
            if not self.board.move_piece(start, end):
                print("Invalid move. Please try again.")
                continue
            # Check for checkmate, stalemate, draw
            # Switch player
            self.current_player = 'black' if self.current_player == 'white' else 'white'

    def is_valid_input(self, move):
        if len(move) != 5:
            return False
        if move[0] not in 'abcdefgh' or move[1] not in '12345678' or \
                move[2] != ' ' or move[3] not in 'abcdefgh' or move[4] not in '12345678':
            return False
        return True


if __name__ == "__main__":
    game = ChessGame()
    game.play()