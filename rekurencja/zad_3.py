from tkinter import *


window = Tk()
window.title("Rekurencja, witraż")
window.geometry("1000x450+100+60")
paramN, paramLg, parX, ParY = 6, 250, 15, 15

NapisN = Label(window, text=" N=")
NapisN.grid(column=0, row=1, padx=5, pady=5)
editN = Entry()
editN.insert(END, '6')
editN.grid(column=1, row=1)

NapisLg = Label(window, text=" Lg=")
NapisLg.grid(column=0, row=2)
editLg = Entry()
editLg.insert(END, '240')
editLg.grid(column=1, row=2, padx=5, pady=5)

NapisX = Label(window, text=" X=")
NapisX.grid(column=3, row=1)
editX = Entry()
editX.insert(END, '15')
editX.grid(column=4, row=1, padx=5, pady=5)

NapisY = Label(window, text=" Y=")
NapisY.grid(column=3, row=2)
editY = Entry()
editY.insert(END, '6')
editY.grid(column=4, row=2, padx=5, pady=5)

canvas = Canvas(bg="white", width=300, height=300)
def clickedClear():
    editN.delete(END, 0)
    editLg.delete(END, 0)
    editX.delete(END, 0)
    editY.delete(END, 0)
    canvas.delete("all")


clearButton = Button(window, text="clear", command=clickedClear)
clearButton.grid(column=1, row=0, padx=5, pady=5)

def draw_square(n, Lg, x, y):
    if n>0:
        canvas.create_line(x, y, x+Lg, y)
        canvas.create_line(x+Lg, y, x+Lg, y+Lg)
        canvas.create_line(x+Lg, y+Lg, x, y+Lg)
        canvas.create_line(x, y+Lg, x, y+Lg/2)
        canvas.create_line(x, y+Lg/2, x+Lg/2, y+Lg)
        canvas.create_line(x+Lg/2, y+Lg, x+Lg, y+Lg/2)
        canvas.create_line(x+Lg, y+Lg/2, x+Lg/2, y)
        canvas.create_line(x+Lg/2, y, x+Lg/4, y+Lg/4)
        draw_square(n-1, Lg/2, x+Lg/4, y+Lg/4)
        canvas.create_line(x+Lg/4, y+Lg/4, x, y+Lg/2)
        canvas.create_line(x, y+Lg, x, y)
    canvas.grid(column=5, row=3, padx=1, pady=1)

def clicked_draw():
    canvas.delete("all")
    paramN = int(editN.get())
    paramLg = int(editLg.get())
    paramX = int(editX.get())
    paramY = int(editY.get())

    print(paramN, paramLg, paramX, paramY)
    draw_square(paramN, paramLg, paramX, paramY )

drawButton = Button(window,text= " Rysuj ", command=clicked_draw)
drawButton.grid(column=0, row=0)

window.mainloop()