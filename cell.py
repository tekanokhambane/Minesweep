import sys
from tkinter import Button, Label, messagebox
import random
import settings
import ctypes
import platform


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self,x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_mine_candidate = False
        self.is_opened = False
        self.x = x
        self.y = y
        #Append the object to the Cell.all_list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=6,
            height=2,
            
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="black",
            fg="white",
            text=f"Cells Left:{Cell.cell_count}",
            font=("", 24)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # if Mines count is equal to cells left count, then player won
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showinfo('Game over!','Congratulations, You won')
                sys.exit()

        # Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')


    def get_cell_by_axis(self, x,y):
        # Return a cell object based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x , self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of ceell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                    )
            # if this was a mine candidate, then for safety, we should
            #reset the backgroud color of the button
            if platform.uname()[0] == "Linux":

                self.cell_btn_object.configure(
                    bg='gray85'
                )
            elif platform.uname()[0] == "Windows":
                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )
            else:
                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )
        # mark the cell as opened (Use the last line of this method)
        self.is_opened = True


    def show_mine(self):
        self.cell_btn_object.configure(bg='blue',)
        messagebox.showwarning('Game over!','You clicked on a mine')
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange',
            )
            self.is_mine_candidate = True
        else:
            if platform.uname()[0] == "Linux":

                self.cell_btn_object.configure(
                    bg='gray85'
                )
            elif platform.uname()[0] == "Windows":
                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )
            else:
                self.cell_btn_object.configure(
                    bg='SystemButtonFace'
                )

            self.is_mine_candidate = False
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self) -> str:
        return f"Cell({self.x},{self.y})"