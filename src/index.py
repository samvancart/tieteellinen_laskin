from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Tieteellinen laskin")
    window.configure(background='#D9D9D9')
    window.resizable(False, False)

    view = UI(window)
    view.start()

    window.mainloop()

if __name__ == "__main__":
    main()
