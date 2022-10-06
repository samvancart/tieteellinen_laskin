import tkinter as tk
from tkinter import Tk, ttk, END

from services.calculator import Calculator
from services.rpn import Rpn
from services.variable_handler import VariableHandler


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
        self.var_clicked = False
        self.var_handler = VariableHandler()

    def button_click(self, value, entry):
        if value == 'var':
            self.var_clicked = True
        if value == '=' and not self.var_clicked:
            self.handle_equals(entry)
            return
        if value == '=' and self.var_clicked:
            self.handle_var(entry)
            return
        if value == 'AC':
            self.clear_entry(entry)
            self.handle_var_clicked()
            return
        current = entry.get()
        new = current + value
        if value in self.rpn.get_functions():
            new = current + value + '('
        if value == 'var':
            new = current + value + '='
        entry.delete(0, END)
        entry.insert(0, new)

    def handle_var(self, entry):
        self.var_handler.create_variable(entry.get())
        self.clear_entry(entry)
        self.handle_var_clicked()
        # print(self.var_handler.get_variables_as_dict())
        # print(self.var_clicked)
        return

    def handle_equals(self, entry):
        if entry.get() == '':
            return
        str_input = entry.get()
        result = self.calculator.calculate(str_input)
        self.clear_entry(entry)
        entry.insert(0, result)

    def handle_var_clicked(self):
        if self.var_clicked:
            self.var_clicked = False

    def clear_entry(self, entry):
        entry.delete(0, END)

    def start(self):
        frame_bottom = ttk.Frame(master=self._root, borderwidth=5, padding=10)
        frame_top = ttk.Frame(master=self._root, borderwidth=5, padding=10)
        frame_top.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=tk.W)
        frame_bottom.grid(column=0, row=2, columnspan=4,
                          rowspan=4, sticky=tk.W)

        entry = ttk.Entry(master=frame_top, width=25, font=('Helvetica', 30))
        entry.grid(padx=10, pady=10)
        entry.bind("<Key>", lambda event: 'break')

        self.buttons_to_grid(entry, frame_bottom)

    def get_buttons_list(self):
        return [['7', '8', '9', 'AC', '^', 'pi'], ['4', '5', '6', '/', '(', 'sqrt'],
                ['1', '2', '3', '*', ')', 'sin'], ['0', '.', '-', '+', '=', 'var']]

    def buttons_to_grid(self, entry, frame):
        style = ttk.Style()
        for row_index, row in enumerate(self.get_buttons_list()):
            for cell_index, cell in enumerate(row):
                buttons = ttk.Button(
                    frame,
                    text=cell,
                    style='grid.TButton',
                    padding=30,
                    command=lambda value=cell, entry=entry:
                    self.button_click(value, entry)
                )
                style.configure('grid.TButton', font=('Helvetica', 14))
                buttons.grid(row=row_index+3, column=cell_index)
