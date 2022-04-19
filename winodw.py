from tkinter import*


class LBS:
    def __init__(self, root):
        self.root = root
        self.root.title("Mysql")
        self.root.geometry('1200x600')


if __name__ == "__main__":
    root = Tk()
    obj = LBS(root)
    root.mainloop()
