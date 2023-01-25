# imports (* means import everything from the module (tkinter in this case))
from tkinter import *
import settings
import random
import ctypes
import sys


class Cell:  # Create a class named Cell

    all = []

    cell_count = settings.CELL_COUNT

    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(location, width=12, height=4)
        btn.bind("<Button-1>", self.left_click_actions)  # Left click
        btn.bind("<Button-3>", self.right_click_actions)  # Right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(location, bg="black", fg="white", text=f"Cells left : {Cell.cell_count - 12}", width=12, height=4, font=("", 35))
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):

        print(event)  # Prints event information
        print("Left Steve")

        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cell:
                    cell_obj.show_cell()
            self.show_cell()
            # if mines == cells left, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, "You win !", "Congrats !", 0)

        # Cancel left and right click events if cell is opened
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def right_click_actions(self, event):

        print(event)  # Prints event information
        print("Right Steve")

        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    def get_cell_by_axis(self, x, y):
        # return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cell(self):

        cells = [self.get_cell_by_axis(self.x - 1, self.y - 1),
                 self.get_cell_by_axis(self.x - 1, self.y),
                 self.get_cell_by_axis(self.x - 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y - 1),
                 self.get_cell_by_axis(self.x + 1, self.y),
                 self.get_cell_by_axis(self.x + 1, self.y + 1),
                 self.get_cell_by_axis(self.x, self.y + 1),
                 ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cell:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):

        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length, bg="lightblue")
            # Replace text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left : {Cell.cell_count - 12}")

            # if this was a mine candidate then for safety we should config the bg colour to SystemButtonFace
            self.cell_btn_object.configure(bg="SystemButtonFace")

        # Mark the cell as opened (use is as the last line of this method)
        self.is_opened = True

    def show_mine(self):
        # A logic to interrupt the game and display a game over message
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine", "Game Over", 0)
        # sys.exit()

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
