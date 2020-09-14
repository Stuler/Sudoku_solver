from tkinter import *

numbers = [x for x in range(1,10)]
window=Tk()

window.wm_title("Sudoku Solver")

sud_number=StringVar()
e1=Entry(window, textvariable=sud_number,width=2)
e1.grid(row=0,column=0)

e2=Entry(window, textvariable=sud_number,width=2)
e2.grid(row=0,column=1)

e3=Entry(window, textvariable=sud_number,width=2)
e3.grid(row=0,column=2)

e4=Entry(window, textvariable=sud_number,width=2)
e4.grid(row=0,column=3)

e5=Entry(window, textvariable=sud_number,width=2)
e5.grid(row=0,column=4)

e6=Entry(window, textvariable=sud_number,width=2)
e6.grid(row=0,column=5)

e7=Entry(window, textvariable=sud_number,width=2)
e7.grid(row=0,column=6)

e8=Entry(window, textvariable=sud_number,width=2)
e8.grid(row=0,column=7)

e9=Entry(window, textvariable=sud_number,width=2)
e9.grid(row=0,column=8)

e10=Entry(window, textvariable=sud_number,width=2)
e10.grid(row=0,column=9)
window.mainloop()