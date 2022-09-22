from tkinter import Tk,ttk,END

class UI:
    def __init__(self, root):
        self._root = root

    def button_click(self, value, entry):
        if value=='AC':
            self.clear_entry(entry)
            return
        current = entry.get()
        new = current + value
        entry.delete(0,END)
        entry.insert(0,new)

    def clear_entry(self, entry):
        entry.delete(0,END)

    def start(self):
        frame_bottom = ttk.Frame(master=self._root, borderwidth=5,padding=10)
        frame_top = ttk.Frame(master=self._root, borderwidth=5,padding=10)
        frame_top.grid(column=0, row=0, columnspan=3, rowspan=1)
        frame_bottom.grid(column=0, row=2, columnspan=4, rowspan=4)

        entry = ttk.Entry(master=frame_top, width=30, font=('default',30))
        entry.grid(padx=10, pady=10)
        entry.bind("<Key>", lambda event: 'break')

        self.buttons_to_grid(entry,frame_bottom)

    def get_buttons_list(self):
        return [['7', '8', '9', 'AC'], ['4', '5', '6', '/'],
                ['1', '2', '3', '*', ], ['0', '.', '-', '+']]

    def buttons_to_grid(self,entry,frame):
        for row_index, row in enumerate(self.get_buttons_list()):
            for cell_index, cell in enumerate(row):
                buttons = ttk.Button(
                frame,
                text=cell,
                padding=40,
                command=lambda value=cell,entry=entry:
                self.button_click(value,entry)
            )
                buttons.grid(row=row_index+3, column=cell_index)

window = Tk()
window.title("Tieteellinen laskin")
# window.geometry("800x800")
# window.resizable(0,0)


ui = UI(window)
ui.start()

window.mainloop()
