
from JanggiPieces import Soldier
from JanggiPieces import Horse
from JanggiPieces import Elephant
from JanggiPieces import Chariot
from JanggiPieces import Cannon
from JanggiPieces import Guard
from JanggiPieces import General


class GameBoard:
    """
    Represents the game board Janggi will be played on. Gameboard housed all the methods used in validating make_move's
    conditions on the game board. The actual game board is composed of piece objects than can be moved, and called on
    to get a move set that is representative of Janggi rules.
    """

    def __init__(self):
        """
        Initialize each piece as an object, the game board representation, each player's piece roster, and all
        required variables for methods
        """

        # Initialize all pieces. Each piece has a two parameters: player and initial location

        # Red pieces
        self._r_ch_1 = Chariot("R", "a1")
        self._r_el_1 = Elephant("R", "b1")
        self._r_ho_1 = Horse("R", "c1")
        self._r_gu_1 = Guard("R", "d1")
        self._r_gu_2 = Guard("R", "f1")
        self._r_el_2 = Elephant("R", "g1")
        self._r_ho_2 = Horse("R", "h1")
        self._r_ch_2 = Chariot("R", "i1")
        self._r_ge = General("R", "e2")
        self._r_ca_1 = Cannon("R", "b3")
        self._r_ca_2 = Cannon("R", "h3")
        self._r_so_1 = Soldier("R", "a4")
        self._r_so_2 = Soldier("R", "c4")
        self._r_so_3 = Soldier("R", "e4")
        self._r_so_4 = Soldier("R", "g4")
        self._r_so_5 = Soldier("R", "i4")

        # Blue pieces
        self._b_ch_1 = Chariot("B", "a10")
        self._b_el_1 = Elephant("B", "b10")
        self._b_ho_1 = Horse("B", "c10")
        self._b_gu_1 = Guard("B", "d10")
        self._b_gu_2 = Guard("B", "f10")
        self._b_el_2 = Elephant("B", "g10")
        self._b_ho_2 = Horse("B", "h10")
        self._b_ch_2 = Chariot("B", "i10")
        self._b_ge = General("B", "e9")
        self._b_ca_1 = Cannon("B", "b8")
        self._b_ca_2 = Cannon("B", "h8")
        self._b_so_1 = Soldier("B", "a7")
        self._b_so_2 = Soldier("B", "c7")
        self._b_so_3 = Soldier("B", "e7")
        self._b_so_4 = Soldier("B", "g7")
        self._b_so_5 = Soldier("B", "i7")

        # Set up rosters for each player that will be altered when a piece is captured
        self._red_player = [self._r_ch_1, self._r_el_1, self._r_ho_1, self._r_gu_1, self._r_gu_2, self._r_el_2,
                            self._r_ho_2, self._r_ch_2, self._r_ca_1, self._r_ca_2, self._r_so_1, self._r_so_2,
                            self._r_so_3, self._r_so_4, self._r_so_5, self._r_ge]

        self._blue_player = [self._b_ch_1, self._b_el_1, self._b_ho_1, self._b_gu_1, self._b_gu_2, self._b_el_2,
                             self._b_ho_2, self._b_ch_2, self._b_ca_1, self._b_ca_2, self._b_so_1, self._b_so_2,
                             self._b_so_3, self._b_so_4, self._b_so_5, self._b_ge]

        # Set up game board with pieces and 0 to represent empty location
        self._game_board = {
            1: [self._r_ch_1, self._r_el_1, self._r_ho_1, self._r_gu_1, 0, self._r_gu_2, self._r_el_2, self._r_ho_2, self._r_ch_2],
            2: [0, 0, 0, 0, self._r_ge, 0, 0, 0, 0],
            3: [0, self._r_ca_1, 0, 0, 0, 0, 0, self._r_ca_2, 0],
            4: [self._r_so_1, 0, self._r_so_2, 0, self._r_so_3, 0, self._r_so_4, 0, self._r_so_5],
            5: [0] * 9,
            6: [0] * 9,
            7: [self._b_so_1, 0, self._b_so_2, 0, self._b_so_3, 0, self._b_so_4, 0, self._b_so_5],
            8: [0, self._b_ca_1, 0, 0, 0, 0, 0, self._b_ca_2, 0],
            9: [0, 0, 0, 0, self._b_ge, 0, 0, 0, 0],
            10: [self._b_ch_1, self._b_el_1, self._b_ho_1, self._b_gu_1, 0, self._b_gu_2, self._b_el_2, self._b_ho_2, self._b_ch_2]
        }

        # Initialize variables and conversion tables
        self._cur_loc = None
        self._new_loc = None
        self._cur_col = None
        self._cur_row = None
        self._new_col = None
        self._new_row = None
        self._let_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j":9}
        self._num_to_let = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9:"j"}
        self._player_turn = "B"
        self._move_path = []
        self._all_possible_moves_blue = []
        self._all_possible_moves_red = []

        # Initialize move lists
        for piece in self._red_player:
            self.find_piece_available_moves(piece)

        for piece in self._blue_player:
            self.find_piece_available_moves(piece)

        self.set_all_possible_moves("B")
        self.set_all_possible_moves("R")

    def print_board(self):
        print("     a   b   c   d   e   f   g   h   i")
        print("     ----------------------------------")
        for row in self._game_board:
            if row < 10:
                display = str(row) + "  | "
            else:
                display = str(row) + " | "
            for col in self._game_board[row]:
                if col != 0:
                    display += str(col) + " "
                else:
                    display += " " + str(col) + "  "

            print(display)

    def add_piece_to_player(self, player, piece):
        """Reverts a captured piece if move is found to be false after board is altered"""
        if player == "R":
            self._red_player.append(piece)
        elif player == "B":
            self._blue_player.append(piece)

    def del_piece_from_player(self, player, piece):
        """Used for capturing a piece"""
        if player == "R":
            self._red_player.remove(piece)
        elif player == "B":
            self._blue_player.remove(piece)

    def set_all_possible_moves(self, player):
        """Calls a function that will return all possible moves for a given player"""
        if player == "B":
            self._all_possible_moves_blue = self.find_all_possible_moves("B")
        elif player == "R":
            self._all_possible_moves_red = self.find_all_possible_moves("R")

    def format_node(self, row, col):
        """Converts a row and column into user input format"""
        return self._num_to_let[col] + str(row)

    def get_player_turn(self):
        """Returns player turn"""
        return self._player_turn

    def set_player_turn(self, turn):
        """Changes player turn"""
        self._player_turn = turn

    def set_cur_loc(self, val):
        """Receives input from make_move method to set current location"""
        self._cur_loc = val
        self._cur_col = self._let_to_num[self._cur_loc[0]]
        self._cur_row = int(self._cur_loc[1:3])

    def set_new_loc(self, val):
        """Receives input from make_move method to set new location"""
        self._new_loc = val
        self._new_col = self._let_to_num[self._new_loc[0]]
        self._new_row = int(self._new_loc[1:3])

    def set_square(self, row, col, new_val):
        """Changes the value at given location when a move is made"""
        self._game_board[row][col] = new_val

    def get_square(self, row, col):
        """Returns the value that is at a requested location on the board"""
        return self._game_board[row][col]

    def find_all_possible_moves(self, player):  # Need to initialize each move?
        """Searches for all possible moves a player can make and returns them in set form"""

        if player == "R":
            self._all_possible_moves_red = []

            for piece in self._red_player:  # Every piece that is in player's roster
                self._cur_loc = piece.get_cur_loc()
                piece.clear_piece_possible_moves()
                self.find_piece_available_moves(piece)

                for move in piece.get_piece_possible_moves():  # Every move each piece can make
                    self._all_possible_moves_red.append(move)

            return self._all_possible_moves_red

        elif player == "B":  # Mirror actions for other player
            self._all_possible_moves_blue = []

            for piece in self._blue_player:
                self._cur_loc = piece.get_cur_loc()
                piece.clear_piece_possible_moves()
                self.find_piece_available_moves(piece)

                for move in piece.get_piece_possible_moves():
                    self._all_possible_moves_blue.append(move)

            return self._all_possible_moves_blue

    def check_mate(self, player):
        """Checks current game state to see if a player is in check mate"""

        if player == "R":
            self.find_piece_available_moves(self._r_ge)
            if len(self._r_ge.get_piece_possible_moves()) == 0:  # General cannot move anywhere

                if self._new_loc not in self._all_possible_moves_red:  # Attacking piece cannot be captured

                    for space in self._move_path:
                        if space in self._all_possible_moves_red:  # Attacking piece cannot be blocked
                            return
                    return True

        elif player == "B":  # Mirror actions for other player
            self.find_piece_available_moves(self._b_ge)
            if len(self._b_ge.get_piece_possible_moves()) == 0:

                if self._new_loc not in self._all_possible_moves_blue:

                    for space in self._move_path:
                        if space in self._all_possible_moves_blue:
                            return
                    return True

    def find_piece_available_moves(self, piece):
        """Caclulates all available moves for a given piece"""

        move_list = piece.check_moves()  # List of every move a piece can make without going out of bounds
        piece.clear_piece_possible_moves()

        if piece.get_type() == "General":
            for key in move_list:
                if self.validate_move(piece, move_list[key]) is not False:  # Accounts for pieces blocking path

                    # King cannot move into check
                    if piece.get_player() == "R":
                        if key not in self._all_possible_moves_blue:
                            piece.set_piece_possible_moves(self.validate_move(piece, move_list[key]))
                    if piece.get_player() == "B":
                        if key not in self._all_possible_moves_red:
                            piece.set_piece_possible_moves(self.validate_move(piece, move_list[key]))

        else:
            for key in move_list:
                if self.validate_move(piece, move_list[key]) is not False:
                    piece.set_piece_possible_moves(self.validate_move(piece, move_list[key]))

    def check_move(self, condition):
        """Receives a path to accomplish current move, and checks if that move is legal"""

        cur_piece = self._game_board[self._cur_row][self._cur_col]
        self.find_piece_available_moves(cur_piece)

        if condition == "MOVE":  # Checks if new move is in list of piece's valid moves
            if self._new_loc not in cur_piece.get_piece_possible_moves():
                return False

        # Simulate next turn to see if general can be captured (check)
        if condition == "CHECK":

            # Check resulting from current player putting opposing player into check
            if self._player_turn == "B":
                if self._r_ge.get_cur_loc() in cur_piece.get_piece_possible_moves():

                    # Store move path to use in checkmate validation, i.e. if path can be blocked
                    self._move_path = []
                    row = self._cur_row
                    col = self._cur_col
                    for location in cur_piece.check_moves()[self._r_ge.get_cur_loc()]:
                        row += location[0]
                        col += location[1]
                        self._move_path.append(self.format_node(row, col))
                    return "R"

                # Check resulting from a player moving themselves into check (illegal)
                elif self._b_ge.get_cur_loc() in self._all_possible_moves_red:
                    return "B"

            elif self._player_turn == "R":  # Mirror actions for other player
                if self._b_ge.get_cur_loc() in cur_piece.get_piece_possible_moves():

                    self._move_path = []
                    row = self._cur_row
                    col = self._cur_col
                    for location in cur_piece.check_moves()[self._b_ge.get_cur_loc()]:
                        row += location[0]
                        col += location[1]
                        self._move_path.append(self.format_node(row, col))

                    return "B"

                elif self._r_ge.get_cur_loc() in self._all_possible_moves_blue:
                    return "R"

    def validate_move(self, piece, list_moves):
        """
        Where the magic happens. Given a piece and the piece's move set, returns valid moves within that
        set. Cannons and chariots will record each valid move until they reach a block. All other pieces will
        only record the last move
        """

        loc = piece.get_cur_loc()
        row_mov = int(loc[1:3])
        col_mov = self._let_to_num[loc[0]]

        # Check every move in the list of possible moves to see if they are valid
        move = 0
        while move < len(list_moves):
            row_mov += list_moves[move][0]
            col_mov += list_moves[move][1]

            # Cannon must jump over another piece to move CANT MOVE OVER OTHER CANNON
            if piece.get_type() == "Cannon" and move == 0:
                if self._game_board[row_mov][col_mov] == 0:

                    # Continue searching for a piece to jump over
                    while self._game_board[row_mov][col_mov] == 0:
                        if move == len(list_moves) - 1:  # False if no pieces are found
                            return False
                        row_mov += list_moves[move][0]
                        col_mov += list_moves[move][1]
                        move += 1

                    if move == len(list_moves) - 1:  # False if no pieces are found
                        return False

                    # Cannons cannot jump over themselves
                    if self._game_board[row_mov][col_mov] != 0:
                        if self._game_board[row_mov][col_mov].get_type() == "Cannon":
                            return False

                    # Jump over piece
                    row_mov += list_moves[move][0]
                    col_mov += list_moves[move][1]
                    move += 1
                else:
                    # No pieces found
                    if move == len(list_moves) - 1:
                        return False
                    # Jump over piece
                    else:
                        row_mov += list_moves[move][0]
                        col_mov += list_moves[move][1]
                        move += 1

            # Stop when move is blocked
            if self._game_board[row_mov][col_mov] != 0 and move != len(list_moves) - 1:
                return False

            # Evaluate last space
            if move == len(list_moves) - 1:
                new_location = self._game_board[row_mov][col_mov]

                if new_location == 0 or new_location.get_player() != piece.get_player():
                    return self._num_to_let[col_mov] + str(row_mov)
                else:
                    return False
            move += 1
        return False
