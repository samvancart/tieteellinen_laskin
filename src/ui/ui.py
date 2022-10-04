from tkinter import Tk, ttk, END
from services.calculator import Calculator
from services.rpn import Rpn


class UI:
    """Class to handle graphical user interface."""

    def __init__(self, root):
        """Class constructor. Creates new instance of class.

        Args:
            root: Tkinter-element to hold ui.
        """
        self._root = root
        self.calculator = Calculator()
        self.rpn = Rpn()

    def button_click(self, value, entry):

        if value == '=':
            self.handle_equals(entry)
            return
        if value == 'AC':
            self.clear_entry(entry)
            return
        current = entry.get()
        new = current + value
        if value in self.rpn.get_functions():
            new = current + value + '('
        entry.delete(0, END)
        entry.insert(0, new)

    def handle_equals(self, entry):
        if entry.get() == '':
            return
        str_input = entry.get()
        result = self.calculator.calculate(str_input)
        self.clear_entry(entry)
        entry.insert(0, result)

    def clear_entry(self, entry):
        entry.delete(0, END)

    def start(self):
        frame_bottom = ttk.Frame(master=self._root, borderwidth=5, padding=10)
        frame_top = ttk.Frame(master=self._root, borderwidth=5, padding=10)
        frame_top.grid(column=0, row=0, columnspan=3, rowspan=1)
        frame_bottom.grid(column=0, row=2, columnspan=4, rowspan=4)

        entry = ttk.Entry(master=frame_top, width=30, font=('default', 30))
        entry.grid(padx=10, pady=10)
        entry.bind("<Key>", lambda event: 'break')

        self.buttons_to_grid(entry, frame_bottom)

    def get_buttons_list(self):
        return [['7', '8', '9', 'AC', '^', 'pi'], ['4', '5', '6', '/', '(', 'sqrt'],
                ['1', '2', '3', '*', ')', 'sin'], ['0', '.', '-', '+', '=']]

    def buttons_to_grid(self, entry, frame):
        style = ttk.Style()
        for row_index, row in enumerate(self.get_buttons_list()):
            for cell_index, cell in enumerate(row):
                buttons = ttk.Button(
                    frame,
                    text=cell,
                    style='grid.TButton',
                    padding=40,
                    command=lambda value=cell, entry=entry:
                    self.button_click(value, entry)
                )
                style.configure('grid.TButton', font=('Helvetica', 14))
                buttons.grid(row=row_index+3, column=cell_index)
