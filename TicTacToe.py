from tkinter import *
import tttback


class app:
    def __init__(self, master):
            frame = Frame(master)
            frame.grid()
            self.init_game(frame)

    def init_game(self, frame):
            frame.grid()

            fa1=StringVar()
            fa1.set("    ")

            fa2=StringVar()
            fa2.set("    ")

            fa3=StringVar()
            fa3.set("    ")

            fb1=StringVar()
            fb1.set("    ")

            fb2=StringVar()
            fb2.set("    ")


            fb3=StringVar()
            fb3.set("    ")

            fc1=StringVar()
            fc1.set("    ")

            fc2=StringVar()
            fc2.set("    ")

            fc3=StringVar()
            fc3.set("    ")

            self.turn = 1

            self.a1 = Label(frame, textvariable=fa1, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.a2 = Label(frame, textvariable=fa2, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.a3 = Label(frame, textvariable=fa3, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.b1 = Label(frame, textvariable=fb1, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.b2 = Label(frame, textvariable=fb2, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.b3 = Label(frame, textvariable=fb3, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.c1 = Label(frame, textvariable=fc1, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.c2 = Label(frame, textvariable=fc2, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            self.c3 = Label(frame, textvariable=fc3, borderwidth=2, relief="ridge", height=10, width = 20, font=200)
            
            self.a1.grid(column=0, row=0)
            self.a2.grid(column=1, row=0)
            self.a3.grid(column=2, row=0)
            self.b1.grid(column=0, row=1)
            self.b2.grid(column=1, row=1)
            self.b3.grid(column=2, row=1)
            self.c1.grid(column=0, row=2)
            self.c2.grid(column=1, row=2)
            self.c3.grid(column=2, row=2)

            self.a1.bind('<Button-1>', lambda event: tttback.pa1(self, fa1))
            self.a2.bind('<Button-1>', lambda event: tttback.pa2(self, fa2))
            self.a3.bind('<Button-1>', lambda event: tttback.pa3(self, fa3))
            self.b1.bind('<Button-1>', lambda event: tttback.pb1(self, fb1))
            self.b2.bind('<Button-1>', lambda event: tttback.pb2(self, fb2))
            self.b3.bind('<Button-1>', lambda event: tttback.pb3(self, fb3))
            self.c1.bind('<Button-1>', lambda event: tttback.pc1(self, fc1))
            self.c2.bind('<Button-1>', lambda event: tttback.pc2(self, fc2))
            self.c3.bind('<Button-1>', lambda event: tttback.pc3(self, fc3))

	

root = Tk()
root.title("TicTacToe")
b = app(root)
root.mainloop()
