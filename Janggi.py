import tkinter as tk
from JanggiMain import JanggiGame
from PIL import ImageTk, Image


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.grid_coordinates = {"a": [[]]*10, "b": [[]]*10, "c": [[]]*10, "d": [[]]*10, "e": [[]]*10,
                                 "f": [[]]*10, "g": [[]]*10, "h": [[]]*10, "i": [[]]*10}
        self.game = JanggiGame()
        self.start_location = None
        self.start_piece = None
        self.finish_location = None
        self.finish_piece = None
        self.turn_display = None
        self.moves_list = None
        self.red_display = None
        self.blue_display = None
        self.piece_loc = "pieces/"

        # Create game pieces to store associated images and initial starting locations
        # Janggi Piece images taken from http://www.janggi.pl/janggi-figures/
        self.b_ge = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_general.png")), ["e", 9])
        self.b_ca = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_cannon.png")), ["b", 8])
        self.b_ca2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_cannon.png")), ["h", 8])
        self.b_so1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_soldier.png")), ["a", 7])
        self.b_so2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_soldier.png")), ["c", 7])
        self.b_so3 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_soldier.png")), ["e", 7])
        self.b_so4 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_soldier.png")), ["g", 7])
        self.b_so5 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_soldier.png")), ["i", 7])
        self.b_ch1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_chariot.png")), ["a", 10])
        self.b_ch2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_chariot.png")), ["i", 10])
        self.b_ho1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_horse.png")), ["c", 10])
        self.b_ho2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_horse.png")), ["g", 10])
        self.b_gu1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_guardian.png")), ["d", 10])
        self.b_gu2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_guardian.png")), ["f", 10])
        self.b_el1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_elephant.png")), ["b", 10])
        self.b_el2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "blue_elephant.png")), ["h", 10])

        self.r_ge = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_general.png")), ["e", 2])
        self.r_ca = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_cannon.png")), ["b", 3])
        self.r_ca2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_cannon.png")), ["h", 3])
        self.r_so1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_soldier.png")), ["a", 4])
        self.r_so2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_soldier.png")), ["c", 4])
        self.r_so3 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_soldier.png")), ["e", 4])
        self.r_so4 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_soldier.png")), ["g", 4])
        self.r_so5 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_soldier.png")), ["i", 4])
        self.r_ch1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_chariot.png")), ["a", 1])
        self.r_ch2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_chariot.png")), ["i", 1])
        self.r_ho1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_horse.png")), ["c", 1])
        self.r_ho2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_horse.png")), ["g", 1])
        self.r_gu1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_guardian.png")), ["d", 1])
        self.r_gu2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_guardian.png")), ["f", 1])
        self.r_el1 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_elephant.png")), ["b", 1])
        self.r_el2 = Piece(ImageTk.PhotoImage(Image.open(self.piece_loc + "red_elephant.png")), ["h", 1])

        # Create roster to add initial pieces to board
        self.pieces = [self.b_ge, self.b_ca, self.b_ca2, self.b_so1, self.b_so2, self.b_so3, self.b_so4, self.b_so5,
                       self.b_ch1, self.b_ch2, self.b_ho1, self.b_ho2, self.b_gu1, self.b_gu2, self.b_el1, self.b_el2,
                       self.r_ge, self.r_ca, self.r_ca2, self.r_so1, self.r_so2, self.r_so3, self.r_so4, self.r_so5,
                       self.r_ch1, self.r_ch2, self.r_ho1, self.r_ho2, self.r_gu1, self.r_gu2, self.r_el1, self.r_el2
                       ]

        self.create_widgets()

    def create_widgets(self):
        """
        Add widgets to application
        """
        self.create_board()  # draw board

        # Side panel display
        frame = tk.Frame(self, padx=100, borderwidth=5, height=500)

        title = tk.Label(frame, text="Janggi")
        title.config(font=30)
        title.pack()


        # Red player
        self.red_display = tk.Label(frame, text="Red Player" + "\n" + " ", pady=100)
        self.red_display.pack(side="top")

        # Moves made
        self.moves_list = tk.Listbox(frame, listvariable=self.moves_list, height=20, bg="white", width="20")
        self.moves_list.pack()

        # Blue player
        self.blue_display = tk.Label(frame, text="Your Move" + "\n" + "Blue Player", pady=100)
        self.blue_display.pack()

        frame.pack(side="right")

        # Add display for current player turn

    def create_board(self):
        """
        Creates a canvas and then draws the game board. Pieces are then added, and a grid system is created so that
        the piece locations can be referenced later in the application
        """
        square = 80
        margin = 40
        height = square*9
        width = square*8

        canvas = tk.Canvas(self, height=height+margin*2, width=width+margin*2, background="DarkOrange")

        # Draw the game board
        self.draw_board(canvas, height, width, margin, square)

        # Create gridlines
        self.generate_gridlines(margin, square)

        # Place pieces in starting locations
        for pieces in self.pieces:
            self.place_piece(pieces)  # Place piece and record button object for later moves

        canvas.bind("<Button-1>", self.mouse_click)
        canvas.pack(side="left")

    def draw_board(self, canvas, height, width, margin, square):
        """
        Draw board on canvas given height, width, margin, and square size
        """
        # Create main Grid
        for y_cord in range(margin, height + square, square):
            canvas.create_line(margin, y_cord, width + margin, y_cord)
        for x_cord in range(margin, width + square, square):
            canvas.create_line(x_cord, margin, x_cord, height + margin)

        # Create Fortress
        canvas.create_line(margin + width / 2 - square, margin, margin + width / 2, margin + square)
        canvas.create_line(margin + width / 2 + square, margin, margin + width / 2, margin + square)
        canvas.create_line(margin + width / 2, margin + square, margin + width / 2 - square, margin + square * 2)
        canvas.create_line(margin + width / 2, margin + square, margin + width / 2 + square, margin + square * 2)

        canvas.create_line(margin + width / 2 - square, margin + height, margin + width / 2, margin + height - square)
        canvas.create_line(margin + width / 2 + square, margin + height, margin + width / 2, margin + height - square)
        canvas.create_line(margin + width / 2, margin + height - square, margin + width / 2 - square, margin + height - square * 2)
        canvas.create_line(margin + width / 2, margin + height - square, margin + width / 2 + square, margin + height - square * 2)

    def generate_gridlines(self, margin, square):
        """
        Generate a dictionary containing coordinates for each possible location on game board
        """
        # Create grid coordinates for pieces
        vert_line = margin
        for row in self.grid_coordinates:
            for num in range(0, 10):
                self.grid_coordinates[row][num] = [vert_line, margin+square*num]
            vert_line += square

    def turn_box(self, player_turn):
        """
        Display the current player turn
        """
        if player_turn == "Blue Player":
            self.blue_display["text"] = "Your Move" + "\n" + "Blue Player"
            self.red_display["text"] = "Red Player" + "\n" + " "
        elif player_turn == "Red Player ":
            self.red_display["text"] = "Red Player" + "\n" + "Your Move"
            self.blue_display["text"] = "Blue Player" + "\n" + " "
            self.blue_display.config(font=20)

    def place_piece(self, piece):
        grid = self.grid_coordinates
        image = piece.get_image()
        col = piece.get_location()[0]
        row = piece.get_location()[1]

        button = tk.Button(self, image=image, border="0")
        button["command"] = lambda : self.button_select(row, col, piece)
        button.place(x=grid[col][row-1][0], y=grid[col][row-1][1], anchor="center")
        piece.set_button(button)
        return button

    def mouse_click(self, event):
        print("clicked at", event.x, event.y)

        coord = self.grid_conversion(event.x, event.y)
        self.finish_location = coord[1] + str(coord[0])

        if coord[0] is not None and coord[1] is not None:
            if self.start_location is not None:
                self.make_move()

    def button_select(self, row, col, piece):
        if self.start_location is None:
            self.start_location = col + str(row)
            self.start_piece = piece
            print(self.start_location)
        else:
            self.finish_location = col + str(row)
            self.finish_piece = piece
            print(self.start_location)
            print(self.finish_location)
            self.make_move()

    def make_move(self):
        if self.game.make_move(self.start_location, self.finish_location) is True:
            self.start_piece.set_location([self.finish_location[0], int(self.finish_location[1])])
            self.start_piece.get_button().destroy()
            if self.finish_piece is not None:
                self.finish_piece.get_button().destroy()
            self.place_piece(self.start_piece)

            self.moves_list.insert("end", self.start_location + ", " + self.finish_location)

            self.turn_box(self.game.display_player_turn())

            self.clear_data()

        else:
            print("false move")
            self.clear_data()

    def clear_data(self):
        self.start_location = None
        self.finish_location = None
        self.start_piece = None
        self.finish_piece = None

    def grid_conversion(self, x, y):
        row = None
        col = None

        if 20 < x < 60:
            col = "a"
        elif 100 < x < 140:
            col = "b"
        elif 180 < x < 220:
            col = "c"
        elif 260 < x < 300:
            col = "d"
        elif 340 < x < 380:
            col = "e"
        elif 420 < x < 460:
            col = "f"
        elif 500 < x < 540:
            col = "g"
        elif 580 < x < 620:
            col = "h"
        elif 620 < x < 700:
            col = "i"

        if 20 < y < 60:
            row = 1
        elif 100 < y < 140:
            row = 2
        elif 180 < y < 220:
            row = 3
        elif 260 < y < 300:
            row = 4
        elif 340 < y < 380:
            row = 5
        elif 420 < y < 460:
            row = 6
        elif 500 < y < 540:
            row = 7
        elif 580 < y < 620:
            row = 8
        elif 660 < y < 700:
            row = 9
        elif 740 < y < 780:
            row = 10

        return [row, col]


class Piece:
    def __init__(self, image, location):
        self.image = image
        self.location = location
        self.button = None

    def set_location(self, location):
        self.location = location

    def get_image(self):
        return self.image

    def get_location(self):
        return self.location

    def set_button(self, button):
        self.button = button

    def get_button(self):
        return self.button

root = tk.Tk()
root.geometry = "720x1200"
root.title = "Janggi Game"
app = Application(master=root)


app.mainloop()
