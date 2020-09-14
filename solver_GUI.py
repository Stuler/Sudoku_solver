from tkinter import *

window=Tk()

window.wm_title("Sudoku Solver")

# Row 1
sud_number_1=StringVar()
e1=Entry(window, textvariable=sud_number_1,width=2)
e1.grid(row=0,column=0)

sud_number_2=StringVar()
e2=Entry(window, textvariable=sud_number_2,width=2)
e2.grid(row=0,column=1)

sud_number_3=StringVar()
e3=Entry(window, textvariable=sud_number_3,width=2)
e3.grid(row=0,column=2)

sud_number_4=StringVar()
e4=Entry(window, textvariable=sud_number_4,width=2)
e4.grid(row=0,column=3)

sud_number_5=StringVar()
e5=Entry(window, textvariable=sud_number_5,width=2)
e5.grid(row=0,column=4)

sud_number_6=StringVar()
e6=Entry(window, textvariable=sud_number_6,width=2)
e6.grid(row=0,column=5)

sud_number_7=StringVar()
e7=Entry(window, textvariable=sud_number_7,width=2)
e7.grid(row=0,column=6)

sud_number_8=StringVar()
e8=Entry(window, textvariable=sud_number_8,width=2)
e8.grid(row=0,column=7)

sud_number_9=StringVar()
e9=Entry(window, textvariable=sud_number_9,width=2)
e9.grid(row=0,column=8)

# Row 2
sud_number_10=StringVar()
e10=Entry(window, textvariable=sud_number_10,width=2)
e10.grid(row=1,column=0)

sud_number_11=StringVar()
e11=Entry(window, textvariable=sud_number_11,width=2)
e11.grid(row=1,column=1)

sud_number_12=StringVar()
e12=Entry(window, textvariable=sud_number_12,width=2)
e12.grid(row=1,column=2)

sud_number_13=StringVar()
e13=Entry(window, textvariable=sud_number_13,width=2)
e13.grid(row=1,column=3)

sud_number_14=StringVar()
e14=Entry(window, textvariable=sud_number_14,width=2)
e14.grid(row=1,column=4)

sud_number_15=StringVar()
e15=Entry(window, textvariable=sud_number_15,width=2)
e15.grid(row=1,column=5)

sud_number_16=StringVar()
e16=Entry(window, textvariable=sud_number_16,width=2)
e16.grid(row=1,column=6)

sud_number_17=StringVar()
e17=Entry(window, textvariable=sud_number_17,width=2)
e17.grid(row=1,column=7)

sud_number_18=StringVar()
e18=Entry(window, textvariable=sud_number_18,width=2)
e18.grid(row=1,column=8)

# Row 3
sud_number_19=StringVar()
e19=Entry(window, textvariable=sud_number_19,width=2)
e19.grid(row=2,column=0)

sud_number_20=StringVar()
e20=Entry(window, textvariable=sud_number_20,width=2)
e20.grid(row=2,column=1)

sud_number_21=StringVar()
e21=Entry(window, textvariable=sud_number_21,width=2)
e21.grid(row=2,column=2)

sud_number_22=StringVar()
e22=Entry(window, textvariable=sud_number_22,width=2)
e22.grid(row=2,column=3)

sud_number_23=StringVar()
e23=Entry(window, textvariable=sud_number_23,width=2)
e23.grid(row=2,column=4)

sud_number_24=StringVar()
e24=Entry(window, textvariable=sud_number_24,width=2)
e24.grid(row=2,column=5)

sud_number_25=StringVar()
e25=Entry(window, textvariable=sud_number_25,width=2)
e25.grid(row=2,column=6)

sud_number_26=StringVar()
e26=Entry(window, textvariable=sud_number_26,width=2)
e26.grid(row=2,column=7)

sud_number_27=StringVar()
e27=Entry(window, textvariable=sud_number_27,width=2)
e27.grid(row=2,column=8)

# Row 4
sud_number_28=StringVar()
e28=Entry(window, textvariable=sud_number_28,width=2)
e28.grid(row=3,column=0)

sud_number_29=StringVar()
e29=Entry(window, textvariable=sud_number_29,width=2)
e29.grid(row=3,column=1)

sud_number_30=StringVar()
e30=Entry(window, textvariable=sud_number_30,width=2)
e30.grid(row=3,column=2)

sud_number_31=StringVar()
e31=Entry(window, textvariable=sud_number_31,width=2)
e31.grid(row=3,column=3)

sud_number_32=StringVar()
e32=Entry(window, textvariable=sud_number_32,width=2)
e32.grid(row=3,column=4)

sud_number_33=StringVar()
e33=Entry(window, textvariable=sud_number_33,width=2)
e33.grid(row=3,column=5)

sud_number_34=StringVar()
e34=Entry(window, textvariable=sud_number_34,width=2)
e34.grid(row=3,column=6)

sud_number_35=StringVar()
e35=Entry(window, textvariable=sud_number_35,width=2)
e35.grid(row=3,column=7)

sud_number_36=StringVar()
e36=Entry(window, textvariable=sud_number_36,width=2)
e36.grid(row=3,column=8)

# Row 5
sud_number_29=StringVar()
e29=Entry(window, textvariable=sud_number_29,width=2)
e29.grid(row=4,column=0)

sud_number_30=StringVar()
e30=Entry(window, textvariable=sud_number_30,width=2)
e30.grid(row=4,column=1)

sud_number_31=StringVar()
e31=Entry(window, textvariable=sud_number_31,width=2)
e31.grid(row=4,column=2)

sud_number_32=StringVar()
e32=Entry(window, textvariable=sud_number_32,width=2)
e32.grid(row=4,column=3)

sud_number_33=StringVar()
e33=Entry(window, textvariable=sud_number_33,width=2)
e33.grid(row=4,column=4)

sud_number_34=StringVar()
e34=Entry(window, textvariable=sud_number_34,width=2)
e34.grid(row=4,column=5)

sud_number_35=StringVar()
e35=Entry(window, textvariable=sud_number_35,width=2)
e35.grid(row=4,column=6)

sud_number_36=StringVar()
e36=Entry(window, textvariable=sud_number_36,width=2)
e36.grid(row=4,column=7)

sud_number_37=StringVar()
e37=Entry(window, textvariable=sud_number_37,width=2)
e37.grid(row=4,column=8)

# Row 6
sud_number_38=StringVar()
e38=Entry(window, textvariable=sud_number_38,width=2)
e38.grid(row=5,column=0)

sud_number_39=StringVar()
e39=Entry(window, textvariable=sud_number_39,width=2)
e39.grid(row=5,column=1)

sud_number_40=StringVar()
e40=Entry(window, textvariable=sud_number_40,width=2)
e40.grid(row=5,column=2)

sud_number_41=StringVar()
e41=Entry(window, textvariable=sud_number_41,width=2)
e41.grid(row=5,column=3)

sud_number_42=StringVar()
e42=Entry(window, textvariable=sud_number_42,width=2)
e42.grid(row=5,column=4)

sud_number_43=StringVar()
e43=Entry(window, textvariable=sud_number_43,width=2)
e43.grid(row=5,column=5)

sud_number_44=StringVar()
e44=Entry(window, textvariable=sud_number_44,width=2)
e44.grid(row=5,column=6)

sud_number_45=StringVar()
e45=Entry(window, textvariable=sud_number_45,width=2)
e45.grid(row=5,column=7)

sud_number_46=StringVar()
e46=Entry(window, textvariable=sud_number_46,width=2)
e46.grid(row=5,column=8)

# Row 7
sud_number_47=StringVar()
e47=Entry(window, textvariable=sud_number_47,width=2)
e47.grid(row=6,column=0)

sud_number_48=StringVar()
e48=Entry(window, textvariable=sud_number_48,width=2)
e48.grid(row=6,column=1)

sud_number_49=StringVar()
e49=Entry(window, textvariable=sud_number_49,width=2)
e49.grid(row=6,column=2)

sud_number_50=StringVar()
e50=Entry(window, textvariable=sud_number_50,width=2)
e50.grid(row=6,column=3)

sud_number_51=StringVar()
e51=Entry(window, textvariable=sud_number_51,width=2)
e51.grid(row=6,column=4)

sud_number_52=StringVar()
e52=Entry(window, textvariable=sud_number_52,width=2)
e52.grid(row=6,column=5)

sud_number_53=StringVar()
e53=Entry(window, textvariable=sud_number_53,width=2)
e53.grid(row=6,column=6)

sud_number_54=StringVar()
e54=Entry(window, textvariable=sud_number_54,width=2)
e54.grid(row=6,column=7)

sud_number_55=StringVar()
e55=Entry(window, textvariable=sud_number_55,width=2)
e55.grid(row=6,column=8)

# Row 8
sud_number_56=StringVar()
e56=Entry(window, textvariable=sud_number_56,width=2)
e56.grid(row=7,column=0)

sud_number_57=StringVar()
e57=Entry(window, textvariable=sud_number_57,width=2)
e57.grid(row=7,column=1)

sud_number_58=StringVar()
e58=Entry(window, textvariable=sud_number_58,width=2)
e58.grid(row=7,column=2)

sud_number_59=StringVar()
e59=Entry(window, textvariable=sud_number_59,width=2)
e59.grid(row=7,column=3)

sud_number_60=StringVar()
e60=Entry(window, textvariable=sud_number_60,width=2)
e60.grid(row=7,column=4)

sud_number_61=StringVar()
e61=Entry(window, textvariable=sud_number_61,width=2)
e61.grid(row=7,column=5)

sud_number_62=StringVar()
e62=Entry(window, textvariable=sud_number_62,width=2)
e62.grid(row=7,column=6)

sud_number_63=StringVar()
e63=Entry(window, textvariable=sud_number_63,width=2)
e63.grid(row=7,column=7)

sud_number_64=StringVar()
e64=Entry(window, textvariable=sud_number_64,width=2)
e64.grid(row=7,column=8)

# Row 9
sud_number_65=StringVar()
e65=Entry(window, textvariable=sud_number_65,width=2)
e65.grid(row=8,column=0)

sud_number_66=StringVar()
e66=Entry(window, textvariable=sud_number_66,width=2)
e66.grid(row=8,column=1)

sud_number_67=StringVar()
e67=Entry(window, textvariable=sud_number_67,width=2)
e67.grid(row=8,column=2)

sud_number_68=StringVar()
e68=Entry(window, textvariable=sud_number_68,width=2)
e68.grid(row=8,column=3)

sud_number_69=StringVar()
e69=Entry(window, textvariable=sud_number_69,width=2)
e69.grid(row=8,column=4)

sud_number_70=StringVar()
e70=Entry(window, textvariable=sud_number_70,width=2)
e70.grid(row=8,column=5)

sud_number_71=StringVar()
e71=Entry(window, textvariable=sud_number_71,width=2)
e71.grid(row=8,column=6)

sud_number_72=StringVar()
e72=Entry(window, textvariable=sud_number_72,width=2)
e72.grid(row=8,column=7)

sud_number_73=StringVar()
e73=Entry(window, textvariable=sud_number_73,width=2)
e73.grid(row=8,column=8)

b1=Button(window,text="Solve")
b1.grid(row=10, column=0, columnspan=3)

b2=Button(window,text="New")
b2.grid(row=10, column=3, columnspan=3)

b3=Button(window,text="Quit")
b3.grid(row=10, column=6, columnspan=3)

window.mainloop()