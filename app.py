from tkinter import *
from cell import Cell
import settings
import utils
root = Tk()
# Override the settings of the windoww
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.configure(bg="black")
root.title('Minesweeper')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black", 
    width=settings.WIDTH,
    height=utils.height_perc(25),
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Mine Sweeper",
    font=(
        '', 36
    )
)

game_title.place(
    x=utils.width_perc(25), y=0
)

left_frame = Frame(
    root,
    bg="black",
    width=utils.width_perc(25),
    height=utils.height_perc(75),
)

left_frame.place(x=0, y=utils.height_perc(25))


center_frame = Frame(
    root,
    bg="black",
    width=utils.width_perc(75),
    height=utils.height_perc(75)
)

center_frame.place(
    x=utils.width_perc(25),
    y=utils.height_perc(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Call the labelform the cell class
Cell.create_cell_count_label(left_frame)

Cell.cell_count_label_object.place(
    x=0,y=0
    )

Cell.randomize_mines()
# print((Cell.all))
# Run the window
root.mainloop()