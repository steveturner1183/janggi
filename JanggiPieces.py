class GamePiece:
    """
    Description: Parent class for all game pieces. Holds initial values and information needed to create a specific
    game piece, and list of possible moves a piece can do at any given game state
    """

    def __init__(self, player, location):
        """
        Initialize player, location, and variables
        """
        self._player = player
        self._move_list = {}
        self._pos_list = []
        self._let_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}
        self._num_to_let = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i"}

        if player == "R":  # Takes into account reverse actions depending on player/side of board
            self._mov = 1
        else:
            self._mov = -1

        self._cur_loc = location
        self._new_loc = None
        self._cur_col = self._let_to_num[self._cur_loc[0]]
        self._cur_row = int(self._cur_loc[1:3])
        self._new_col = None
        self._new_row = None
        self._type = None
        self._piece_possible_moves = []

    def clear_piece_possible_moves(self):
        """Clear possible moves for recalculating"""
        self._piece_possible_moves = []

    def get_piece_possible_moves(self):
        """Get method for piece's possible moves"""
        return self._piece_possible_moves

    def set_piece_possible_moves(self, val):
        """Adds a value to possible moves list"""
        self._piece_possible_moves.append(val)

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

    def get_cur_loc(self):
        """Get method for current location"""
        return self._cur_loc

    def get_player(self):
        """Get method for piece's player"""
        return self._player

    def format_node(self, row, col):
        """Converts row and column to represent user input"""
        return self._num_to_let[col] + str(row)

    def get_type(self):
        """Get method for a piece's type"""
        return self._type


class General(GamePiece):
    """
    Represents a General in Janggi, has a method for returning all the moves the general can make based on it's
    current location.
    """

    def __init__(self, player, location):
        """"""
        super().__init__(player, location)
        self._type = "General"

    def __repr__(self):
        return self._player + "Ge"

    def check_moves(self):
        """
        Given the current location, calculates all moves the general can make. General can only move one space
        within the caste.
        """
        self._move_list = {}

        # Directional variables used to calculate each possible move
        no = [self._cur_row + self._mov, self._cur_col]
        ne = [self._cur_row + self._mov, self._cur_col - self._mov]
        nw = [self._cur_row + self._mov, self._cur_col + self._mov]
        we = [self._cur_row, self._cur_col + self._mov]
        ea = [self._cur_row, self._cur_col - self._mov]
        so = [self._cur_row - self._mov, self._cur_col]
        se = [self._cur_row - self._mov, self._cur_col - self._mov]
        sw = [self._cur_row - self._mov, self._cur_col + self._mov]

        # Based on current position in the castle, generate list of moves in bounds

        # South east castle corner
        if self._cur_loc == "f3" or self._cur_loc == "d8":
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if se[0] in range(0, 11) and se[1] in range(0, 9):
                self._move_list[self.format_node(se[0], se[1])] = [[-self._mov, -self._mov]]
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]

        # East castle middle
        elif self._cur_loc == "f2" or self._cur_loc == "d9":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]

        # Northwest castle corner
        elif self._cur_loc == "f1" or self._cur_loc == "d10":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[self._mov, -self._mov]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]

        # Castle top center
        elif self._cur_loc == "e3" or self._cur_loc == "e8":
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]

        # Castle center
        elif self._cur_loc == "e9" or self._cur_loc == "e2":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[self._mov, -self._mov]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if se[0] in range(0, 11) and se[1] in range(0, 9):
                self._move_list[self.format_node(se[0], se[1])] = [[-self._mov, -self._mov]]
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]
            if sw[0] in range(0, 11) and sw[1] in range(0, 9):
                self._move_list[self.format_node(sw[0], sw[1])] = [[-self._mov, self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[self._mov, self._mov]]

        # Castle bottom center
        elif self._cur_loc == "e10" or self._cur_loc == "e1":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]

        # Castle top left corner
        elif self._cur_loc == "d3" or self._cur_loc == "f8":
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]
            if sw[0] in range(0, 11) and sw[1] in range(0, 9):
                self._move_list[self.format_node(sw[0], sw[1])] = [[-self._mov, self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]

        # Castle left center
        elif self._cur_loc == "d2" or self._cur_loc == "f9":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]
            if so[0] in range(0, 11) and so[1] in range(0, 9):
                self._move_list[self.format_node(so[0], so[1])] = [[-self._mov, 0]]

        # Castle bottom left center
        elif self._cur_loc == "d1" or self._cur_loc == "f10":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[self._mov, self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]

        return self._move_list


class Guard(General):
    """
    Represents a Guard in Janggi, has a method for returning all the moves the guard can make based on it's
    current location. Guard has all the same moves as general, so Guard inherits all moves.
    """
    def __init__(self, player, location):
        """"""
        super().__init__(player, location)
        self._type = None

    def __repr__(self):
        return self._player + "Gu"


class Horse(GamePiece):
    """
    Represents a Horse in Janggi, has a method for returning all the moves the horse can make based on it's
    current location. A horse can move one space straight, and one space diagonally.
    """

    def __repr__(self):
        return self._player + "Ho"

    def check_moves(self):
        """"""
        self._move_list = {}

        # Set each direction based on current location
        no_ea = [self._cur_row + self._mov * 2, self._cur_col - self._mov]
        ea_no = [self._cur_row + self._mov, self._cur_col - self._mov * 2]
        ea_so = [self._cur_row - self._mov, self._cur_col - self._mov * 2]
        so_ea = [self._cur_row - self._mov * 2, self._cur_col - self._mov]
        so_we = [self._cur_row - self._mov * 2, self._cur_col + self._mov]
        we_so = [self._cur_row - self._mov, self._cur_col + self._mov * 2]
        we_no = [self._cur_row + self._mov, self._cur_col + self._mov * 2]
        no_we = [self._cur_row + self._mov * 2, self._cur_col + self._mov]

        # One o'clock position
        if no_ea[0] in range(1, 11) and no_ea[1] in range(0, 9):
            self._move_list[self.format_node(no_ea[0], no_ea[1])] = [[self._mov, 0], [self._mov, -self._mov]]

        # Two o'clock position
        if ea_no[0] in range(1, 11) and ea_no[1] in range(0, 9):
            self._move_list[self.format_node(ea_no[0], ea_no[1])] = [[0, -self._mov], [self._mov, -self._mov]]

        # Four o'clock position
        if ea_so[0] in range(1, 11) and ea_so[1] in range(0, 9):
            self._move_list[self.format_node(ea_so[0], ea_so[1])] = [[0, -self._mov], [-self._mov, -self._mov]]

        # Five o'clock position
        if so_ea[0] in range(1, 11) and so_ea[1] in range(0, 9):
            self._move_list[self.format_node(so_ea[0], so_ea[1])] = [[-self._mov, 0], [-self._mov, -self._mov]]

        # Seven o'clock position
        if so_we[0] in range(1, 11) and so_we[1] in range(0, 9):
            self._move_list[self.format_node(so_we[0], so_we[1])] = [[-self._mov, 0], [-self._mov, self._mov]]

        # Eight o'clock position
        if we_so[0] in range(1, 11) and we_so[1] in range(0, 9):
            self._move_list[self.format_node(we_so[0], we_so[1])] = [[0, self._mov], [-self._mov, self._mov]]

        # Ten o'clock position
        if we_no[0] in range(1, 11) and we_no[1] in range(0, 9):
            self._move_list[self.format_node(we_no[0], we_no[1])] = [[0, self._mov], [self._mov, self._mov]]

        # Eleven o'clock position
        if no_we[0] in range(1, 11) and no_we[1] in range(0, 9):
            self._move_list[self.format_node(no_we[0], no_we[1])] = [[self._mov, 0], [self._mov, self._mov]]

        return self._move_list


class Elephant(GamePiece):
    """
    Represents an Elephant in Janggi, has a method for returning all the moves the elephant can make based on it's
    current location. A elephant can move one space straight, and two spaces diagonally.
    """

    def __repr__(self):
        return self._player + "El"

    def check_moves(self):
        """"""
        self._move_list = {}

        # Set directional values based on current move
        no_ea = [self._cur_row + self._mov * 3, self._cur_col - self._mov * 2]
        ea_no = [self._cur_row + self._mov * 2, self._cur_col - self._mov * 3]
        ea_so = [self._cur_row - self._mov * 2, self._cur_col - self._mov * 3]
        so_ea = [self._cur_row - self._mov * 3, self._cur_col - self._mov * 2]
        so_we = [self._cur_row - self._mov * 3, self._cur_col + self._mov * 2]
        we_so = [self._cur_row - self._mov * 2, self._cur_col + self._mov * 3]
        we_no = [self._cur_row + self._mov * 2, self._cur_col + self._mov * 3]
        no_we = [self._cur_row + self._mov * 3, self._cur_col + self._mov * 2]

        # One o'clock position
        if no_ea[0] in range(1, 11) and no_ea[1] in range(0, 9):
            self._move_list[self.format_node(no_ea[0], no_ea[1])] = [[self._mov, 0], [self._mov, -self._mov],
                                                                     [self._mov, -self._mov]]
        # Two o'clock position
        if ea_no[0] in range(1, 11) and ea_no[1] in range(0, 9):
            self._move_list[self.format_node(ea_no[0], ea_no[1])] = [[0, -self._mov], [self._mov, -self._mov],
                                                                     [self._mov, -self._mov]]
        # Four o'clock position
        if ea_so[0] in range(1, 11) and ea_so[1] in range(0, 9):
            self._move_list[self.format_node(ea_so[0], ea_so[1])] = [[0, -self._mov], [-self._mov, -self._mov],
                                                                     [-self._mov, -self._mov]]
        # Five o'clock position
        if so_ea[0] in range(1, 11) and so_ea[1] in range(0, 9):
            self._move_list[self.format_node(so_ea[0], so_ea[1])] = [[-self._mov, 0], [-self._mov, -self._mov],
                                                                     [-self._mov, -self._mov]]
        # Six o'clock position
        if so_we[0] in range(1, 11) and so_we[1] in range(0, 9):
            self._move_list[self.format_node(so_we[0], so_we[1])] = [[-self._mov, 0], [-self._mov, self._mov],
                                                                     [-self._mov, self._mov]]
        # Eight o'clock position
        if we_so[0] in range(1, 11) and we_so[1] in range(0, 9):
            self._move_list[self.format_node(we_so[0], we_so[1])] = [[0, self._mov], [-self._mov, self._mov],
                                                                     [-self._mov, self._mov]]
        # Ten o'clock position
        if we_no[0] in range(1, 11) and we_no[1] in range(0, 9):
            self._move_list[self.format_node(we_no[0], we_no[1])] = [[0, self._mov], [self._mov, self._mov],
                                                                     [self._mov, self._mov]]
        # Eleven o'clock position
        if no_we[0] in range(1, 11) and no_we[1] in range(0, 9):
            self._move_list[self.format_node(no_we[0], no_we[1])] = [[self._mov, 0], [self._mov, self._mov],
                                                                     [self._mov, self._mov]]
        return self._move_list


class Chariot(GamePiece):
    """
    Represents a Chariot in Janggi, has a method for returning all the moves the chariot can make based on it's
    current location. A Chariot can move unlimited spaces in cardinal directions, and can move diagonally within
    the castle
    """

    def __repr__(self):
        return self._player + "Ch"

    def check_moves(self):
        """"""
        self._move_list = {}

        # West direction
        temp_row = self._cur_row
        temp_col = self._cur_col + self._mov
        temp_list = []

        while temp_col in range(0, 9) and temp_row in range(1, 11):  # Add each move until bounds is reached
            temp_list.append([0, self._mov])
            temp_list_2 = tuple(temp_list)
            self._move_list[self.format_node(temp_row, temp_col)] = temp_list_2
            temp_row += 0
            temp_col += self._mov

        # East direction
        temp_row = self._cur_row
        temp_col = self._cur_col - self._mov
        temp_list = []
        while temp_col in range(0, 9) and temp_row in range(1, 11):
            temp_list.append([0, -self._mov])
            temp_list_2 = tuple(temp_list)
            self._move_list[self.format_node(temp_row, temp_col)] = temp_list_2
            temp_row += 0
            temp_col -= self._mov

        # South direction
        temp_row = self._cur_row - self._mov
        temp_col = self._cur_col
        temp_list = []
        while temp_col in range(0, 9) and temp_row in range(1, 11):
            temp_list.append([-self._mov, 0])
            temp_list_2 = tuple(temp_list)
            self._move_list[self.format_node(temp_row, temp_col)] = temp_list_2
            temp_row -= self._mov
            temp_col += 0

        # North direction
        temp_row = self._cur_row + self._mov
        temp_col = self._cur_col
        temp_list = []
        while temp_col in range(0, 9) and temp_row in range(1, 11):
            temp_list.append([self._mov, 0])
            temp_list_2 = tuple(temp_list)
            self._move_list[self.format_node(temp_row, temp_col)] = temp_list_2
            temp_row += self._mov
            temp_col += 0

        # Set directions for castle movement
        ne = [self._cur_row - 1, self._cur_col + 1]
        nw = [self._cur_row - 1, self._cur_col - 1]
        se = [self._cur_row + 1, self._cur_col + 1]
        sw = [self._cur_row + 1, self._cur_col - 1]
        ne2 = [self._cur_row - 2, self._cur_col + 2]
        nw2 = [self._cur_row - 2, self._cur_col - 2]
        se2 = [self._cur_row + 2, self._cur_col + 2]
        sw2 = [self._cur_row + 2, self._cur_col - 2]

        # Northwest castle corner
        if self._cur_loc == "d8" or self._cur_loc == "d1":
            if se[0] in range(0, 11) and se[1] in range(0, 9):
                self._move_list[self.format_node(se[0], se[1])] = [[1, 1]]
            if se2[0] in range(0, 11) and se2[1] in range(0, 9):
                self._move_list[self.format_node(se2[0], se2[1])] = [[1, 1], [1, 1]]

        # Southwest castle corner
        elif self._cur_loc == "d10" or self._cur_loc == "d3":
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[-1, 1]]
            if ne2[0] in range(0, 11) and ne2[1] in range(0, 9):
                self._move_list[self.format_node(ne2[0], ne2[1])] = [[-1, 1], [-1, 1]]

        # Castle center
        elif self._cur_loc == "e9" or self._cur_loc == "e2":
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[-1, 1]]
            if ne2[0] in range(0, 11) and ne2[1] in range(0, 9):
                self._move_list[self.format_node(ne2[0], ne2[1])] = [[-1, 1], [-1, 1]]
            if se[0] in range(0, 11) and se[1] in range(0, 9):
                self._move_list[self.format_node(se[0], se[1])] = [[1, 1]]
            if se2[0] in range(0, 11) and se2[1] in range(0, 9):
                self._move_list[self.format_node(se2[0], se2[1])] = [[1, 1], [1, 1]]
            if sw[0] in range(0, 11) and sw[1] in range(0, 9):
                self._move_list[self.format_node(sw[0], sw[1])] = [[1, -1]]
            if sw2[0] in range(0, 11) and sw2[1] in range(0, 9):
                self._move_list[self.format_node(sw2[0], sw2[1])] = [[1, -1], [1, -1]]
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[-1, -1]]
            if nw2[0] in range(0, 11) and nw2[1] in range(0, 9):
                self._move_list[self.format_node(nw2[0], nw2[1])] = [[-1, -1], [-1, -1]]

        # South east caste corner
        elif self._cur_loc == "f8" or self._cur_loc == "f1":
            if sw[0] in range(0, 11) and sw[1] in range(0, 9):
                self._move_list[self.format_node(sw[0], sw[1])] = [[1, -1]]
            if sw2[0] in range(0, 11) and sw2[1] in range(0, 9):
                self._move_list[self.format_node(sw2[0], sw2[1])] = [[1, -1], [1, -1]]

        # Noth east castle corner
        elif self._cur_loc == "f10" or self._cur_loc == "f3":
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[-1, -1]]
            if nw2[0] in range(0, 11) and nw2[1] in range(0, 9):
                self._move_list[self.format_node(nw2[0], nw2[1])] = [[-1, -1], [-1, -1]]

        return self._move_list


class Cannon(Chariot):
    """
    Represents a Cannon in Janggi, has a method for returning all the moves the cannon can make based on it's
    current location. A cannon has the same move set as a castle, so it inherits from castle class. The special
    condition that a cannon must 'jump' over a piece is handled when validating moves
    """

    def __init__(self, player, location):
        """"""
        super().__init__(player, location)
        self._type = "Cannon"

    def __repr__(self):
        return self._player + "Ca"


class Soldier(GamePiece):
    """
    Represents a Soldier in Janggi, has a method for returning all the moves the soldier can make based on it's
    current location. A soldier can move forward or sideways, and diagonally inside the castle
    """

    def __repr__(self):
        """"""
        return self._player + "So"

    def check_moves(self):
        """"""
        self._move_list = {}

        # Set directions for movement
        no = [self._cur_row + self._mov, self._cur_col]
        ne = [self._cur_row + self._mov, self._cur_col - self._mov]
        nw = [self._cur_row + self._mov, self._cur_col + self._mov]
        we = [self._cur_row, self._cur_col + self._mov]
        ea = [self._cur_row, self._cur_col - self._mov]

        # Southwest castle corner
        if self._cur_loc == "d3" or self._cur_loc == "f8":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[self._mov, -self._mov]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]

        # Castle center
        elif self._cur_loc == "e9" or self._cur_loc == "e2":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ne[0], ne[1])] = [[self._mov, -self._mov]]
            if ea[0] in range(0, 11) and ea[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[self._mov, self._mov]]

        # Southeast castle corner
        elif self._cur_loc == "d8" or self._cur_loc == "f3":
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if nw[0] in range(0, 11) and nw[1] in range(0, 9):
                self._move_list[self.format_node(nw[0], nw[1])] = [[self._mov, self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]

        # All other locations
        else:
            if no[0] in range(0, 11) and no[1] in range(0, 9):
                self._move_list[self.format_node(no[0], no[1])] = [[self._mov, 0]]
            if ne[0] in range(0, 11) and ne[1] in range(0, 9):
                self._move_list[self.format_node(ea[0], ea[1])] = [[0, -self._mov]]
            if we[0] in range(0, 11) and we[1] in range(0, 9):
                self._move_list[self.format_node(we[0], we[1])] = [[0, self._mov]]

        return self._move_list