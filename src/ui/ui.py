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
        self.frame_bottom = self.create_frame()
        self.frame_top_left = self.create_frame()
        self.frame_top_right = self.create_frame()
        self.entry = self.create_entry(self.frame_top_left)

        self.calculator = Calculator()
        self.rpn = Rpn()
        self.variable_handler = VariableHandler()
        self.var_clicked = False

    def default_button_click(self, value, entry):
        # Handle default button click event
        if value == 'var':
            self.var_clicked = True
        if value == '=' and not self.var_clicked:
            self.handle_equals(entry)
            return
        if value == '=' and self.var_clicked:
            self.handle_variable(entry)
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

    def variable_button_click(self, value, entry):
        # Handle variable button click event
        str_input = value
        result = self.calculator.calculate(str_input)
        current = entry.get()
        new = current + result
        entry.delete(0, END)
        entry.insert(0, new)

    def handle_variable(self, entry):
        # Create a new variable and add variable button to grid 
        result = self.variable_handler.create_variable(entry.get())
        self.clear_entry(entry)
        if result == 'error':
            entry.insert(0, 'error')
            return
        self.handle_var_clicked()
        self.variable_frame_to_grid()
        self.variable_buttons_to_grid(
            self.entry,
            self.frame_top_right,
            self.get_variable_buttons_list(),
        )
        return

    def handle_equals(self, entry):
        # Handle event when equals button is clicked
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
        # Create start layout
        self.frame_top_left.grid(
            column=0, row=0, columnspan=2, rowspan=2, sticky=tk.W)
        self.frame_top_right.grid(column=2, row=0, columnspan=2, rowspan=2)
        self.frame_bottom.grid(column=0, row=2, columnspan=4,
                               rowspan=4, sticky=tk.W)

        self.default_buttons_to_grid(self.entry, self.frame_bottom,
                             self.get_default_buttons_list())

    def get_default_buttons_list(self):
        return [['7', '8', '9', 'AC', '^', 'pi', 'tan'], ['4', '5', '6', '/', '(', 'sqrt'],
                ['1', '2', '3', '*', ')', 'sin'], ['0', '.', '-', '+', '=', 'var']]

    def get_variable_buttons_list(self):
        return self.variable_handler.get_variable_buttons_list()

    def variable_frame_to_grid(self):
        self.frame_top_right.grid(column=2, row=0, columnspan=2, rowspan=2)

    def create_frame(self):
        frame = ttk.Frame(master=self._root, borderwidth=5, padding=10)
        return frame

    def create_entry(self, frame):
        entry = ttk.Entry(master=frame, width=25, font=('Helvetica', 30))
        entry.grid(padx=10, pady=10)
        entry.bind("<Key>", lambda event: 'break')
        return entry

    def default_buttons_to_grid(self, entry, frame, buttons):
        style = ttk.Style()
        for row_index, row in enumerate(buttons):
            for cell_index, cell in enumerate(row):
                buttons = ttk.Button(
                    frame,
                    text=cell,
                    style='default.TButton',
                    padding=30,
                    command=lambda value=cell, entry=entry:
                    self.default_button_click(value, entry)
                )
                style.configure('default.TButton', font=('Helvetica', 14))
                buttons.grid(row=row_index+3, column=cell_index)

    def variable_buttons_to_grid(self, entry, frame, buttons):
        style = ttk.Style()
        for row_index, row in enumerate(buttons):
            for cell_index, cell in enumerate(row):
                buttons = ttk.Button(
                    frame,
                    text=cell['name'] + '=' + cell['value'],
                    style='var.TButton',
                    padding=10,
                    command=lambda value=cell['value'], entry=entry:
                    self.variable_button_click(value, entry)
                )
                style.configure('var.TButton', font=('Helvetica', 14))
                buttons.grid(row=row_index+3, column=cell_index)
