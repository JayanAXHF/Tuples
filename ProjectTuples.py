
month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

profits = (22245, 45446, 12683, 5485656, 784545, 456789, 5485656, 784545, 5485656, 456872, 155445, 4843454)
from tkinter import *


root = Tk()

label = Label(root)
label2 = Label(root)
label3 = Label(root)
label4 = Label(root)


mpindex = profits.index(max(profits))

print(mpindex)

print(profits[mpindex])

mpm = month[mpindex]

print(mpm)


minpindex = profits.index(min(profits))

label["text"] = "Months :" + str(month)
label2["text"] = "Profit : " + str(profits)
label3["text"] = "max Profit : " + str(profits[mpindex] )+ " in Month " + str(month[mpindex])
label4["text"] = "Min Profit : " + str(profits[minpindex] )+ " in Month " + str(month[minpindex])

root.title("Fibonacci")

root.geometry("1920x1080")

label.place(relx = 0.5 , rely = 0.5 , anchor =  CENTER)


label2.place(relx = 0.5 , rely = 0.6 , anchor =  CENTER)

label3.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

label4.place(relx = 0.5 , rely = 0.8 , anchor=CENTER)
root.mainloop()
