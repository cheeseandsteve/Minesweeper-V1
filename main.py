# imports (* means import everything from the module (tkinter in this case))
from tkinter import *
from cell import Cell
import settings
import utils

# Make window
root = Tk()  # Creates window
root.configure(bg="black")  # Background colour
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")  # Window size
root.title("Minesweeper")  # Window title
root.resizable()  # Doesn't allow the window to be resized by the user

top_frame = Frame(root, bg="black", highlightbackground="white", highlightthickness=5, width=utils.width_prct(100),
                  height=utils.height_prct(25))  # Create the top frame
top_frame.place(x=0, y=0)  # Place the frame at the specified coordinates

game_title = Label(top_frame, bg="black", fg="white", text="Minesweeper", font=("", 48))
game_title.place(x=utils.width_prct(36), y=utils.height_prct(2))

left_frame = Frame(root, bg="black", highlightbackground="white", highlightthickness=5, width=utils.width_prct(25),
                   height=utils.height_prct(75))  # Create the left frame
left_frame.place(x=0, y=utils.height_prct(25))  # Place the frame at the specified coordinates

center_frame = Frame(root, bg="black", width=utils.width_prct(75),
                     height=utils.height_prct(75))  # Create the left frame
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))  # Place the frame at the specified coordinates

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Call the label the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

# Run the window
root.mainloop()  # The window won't open without this
