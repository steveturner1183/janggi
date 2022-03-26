# Author: Steven Turner
# Date: 3/11/2021
# Description: Simulator for the Korean Chess game Janggi

from JanggiBoard import GameBoard

class JanggiGame:
    """
    Represents the Korean chess game 'Janggi'. The make_move method can be given a starting location and new location.
    Any illegal moves will return false, and game state will reflect the winning player when checkmate is reached.
    """

    def __init__(self):
        """
        Initialize board, game state requirements, and conversion table.
        """
        self._let_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}
        self._board = GameBoard()
        self._game_state = "UNFINISHED"
        self._red_check = False
        self._blue_check = False
        self._store_new_loc = ""

    def set_game_state(self, game_state):
        """Sets current game state"""
        self._game_state = game_state

    def get_game_state(self):
        """Checks current status of game"""
        return self._game_state

    def get_player_turn(self):
        return self._board.get_player_turn()

    def display_player_turn(self):
        if self.get_player_turn() == "R":
            return "Red Player "
        else:
            return "Blue Player"

    def is_in_check(self, color):
        """Checks if given player is in check"""
        if color == 'blue':
            return self._blue_check
        elif color == 'red':
            return self._red_check

    def revert_game_board(self, cur_loc, new_loc):
        """
        When make_move searches for a check scenario, the game board state is changed. If make_move is false after
        the board state is changed, it must be reverted back using revert_game_board. This allows the game to continue
        even with a false move.
        """
        cur_col = self._let_to_num[cur_loc[0]]
        cur_row = int(cur_loc[1:3])
        new_col = self._let_to_num[new_loc[0]]
        new_row = int(new_loc[1:3])

        # Revert board and piece locations
        self._board.set_square(cur_row, cur_col, self._board.get_square(new_row, new_col))
        self._board.set_square(new_row, new_col, self._store_new_loc)
        self._board.get_square(cur_row, cur_col).set_cur_loc(cur_loc)

        # Revert deletion of piece from player
        if self._board.get_square(new_row, new_col) != 0:
            if self._board.get_player_turn() == "R":
                self._board.add_piece_to_player("B", self._store_new_loc)
            elif self._board.get_player_turn() == "B":
                self._board.add_piece_to_player("R", self._store_new_loc)

        # Recalculate available moves
        self._board.find_piece_available_moves(self._board.get_square(cur_row, cur_col))
        self._board.set_all_possible_moves("B")
        self._board.set_all_possible_moves("R")

        return False

    def make_move(self, cur_loc, new_loc):
        """
        Player makes a move by passing make_move the current position of a piece, and then new position of the piece.
        First initial values and checks are made. Then the move is validated. Finally check and checkmate conditions
        are set, and the turn changes to the other player.

        Conditions that will return false:
            - Piece is not owned by current player
            - There is no piece in current location
            - Move is invalid per Janggi rules
            - Player is in check and does not move out
            - Player moves themselves into check

        When a player is forced into checkmate, the game status will update to show that player has won.
        """

        #  ------------------------------------------
        #  Make move pre-requisite checks and set initial values
        #  ------------------------------------------

        # Check if the game has already finished
        if self._game_state != "UNFINISHED":
            print("The game is finished")
            return False

        # Player passes their turn by not moving a piece
        if cur_loc == new_loc:
            if self._board.get_player_turn() == "R":
                self._board.set_player_turn("B")
            elif self._board.get_player_turn() == "B":
                self._board.set_player_turn("R")
            return True

        # Convert current and new locations to row and column numbers
        cur_col = self._let_to_num[cur_loc[0]]
        cur_row = int(cur_loc[1:3])
        new_col = self._let_to_num[new_loc[0]]
        new_row = int(new_loc[1:3])

        # Check if there is a piece in the current location
        location = self._board.get_square(cur_row, cur_col)
        if location == 0:
            print("No piece in this location")
            return False

        # Sets current and new location in the piece object at the current location
        self._board.get_square(cur_row, cur_col).set_cur_loc(cur_loc)
        self._board.get_square(cur_row, cur_col).set_new_loc(new_loc)
        self._board.set_cur_loc(cur_loc)
        self._board.set_new_loc(new_loc)

        # Check if the piece belongs to the player who's turn it currently is
        if location.get_player() != self._board.get_player_turn():
            print("Selected piece does not belong to player")
            return False

        #  ------------------------------------------
        #  Make move using board object's check_move method
        #  ------------------------------------------

        if self._board.check_move("MOVE") is False:
            return False

        # Once all checks have passed, change the game board
        self._store_new_loc = self._board.get_square(new_row, new_col)  # Used to revert board

        if self._board.get_square(new_row, new_col) != 0:  # Capture piece
            if self._board.get_player_turn() == "R":
                self._board.del_piece_from_player("B", self._store_new_loc)
            elif self._board.get_player_turn() == "B":
                self._board.del_piece_from_player("R", self._store_new_loc)

        self._board.get_square(cur_row, cur_col).set_cur_loc(new_loc)  # New location is now current location
        self._board.set_cur_loc(new_loc)
        self._board.set_square(new_row, new_col, self._board.get_square(cur_row, cur_col)) # current position is 0
        self._board.set_square(cur_row, cur_col, 0)

        self._board.find_piece_available_moves(self._board.get_square(new_row, new_col))  # Recalculate moves
        self._board.set_all_possible_moves("B")
        self._board.set_all_possible_moves("R")

        #  ------------------------------------------
        #  Evaluate if a player is now in check or checkmate, and update turn
        #  ------------------------------------------

        check = self._board.check_move("CHECK")

        if check == "R":
            # If player is already in check, their next move must be to move out of check
            if self._red_check is True:
                return self.revert_game_board(cur_loc, new_loc)

            # If check is set during players own turn return false. Cannot move self into check
            if self._board.get_player_turn() == "R":
                return self.revert_game_board(cur_loc, new_loc)

            # If opposing general can be captured next turn, player is in check
            else:
                self._red_check = True

        # Mirrored logic for other player
        elif check == "B":
            if self._blue_check is True:
                return self.revert_game_board(cur_loc, new_loc)

            if self._board.get_player_turn() == "B":
                return self.revert_game_board(cur_loc, new_loc)

            else:
                self._blue_check = True

        # If player is not in check or has moved out of check
        else:
            self._red_check = False
            self._blue_check = False

        # See if a player is in check mate
        if self._board.get_player_turn() == "R":
            if self._board.check_mate("B") is True and self._blue_check is True:
                self._game_state = "RED_WON"
                return True

        elif self._board.get_player_turn() == "B":
            if self._board.check_mate("R") is True and self._red_check is True:
                self._game_state = "BLUE_WON"
                return True

        # Update player turn
        if self._board.get_player_turn() == "R":
            self._board.set_player_turn("B")
        elif self._board.get_player_turn() == "B":
            self._board.set_player_turn("R")

        return True

if __name__ == "__main__":
    game = JanggiGame()
    print(game.make_move("a7", "a6"))

    game._board.print_board()