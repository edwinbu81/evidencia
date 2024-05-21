from tkinter import Tk, Label, Button, Entry

vent = Tk()

vent.title("Ejemplo de Suma con label")
vent.geometry("400x200")

def fnSuma():
    n1 = float(txt1.get())
    n2 = float(txt2.get())
    r = n1 + n2
    txt3.delete(0, 'end')
    txt3.insert(0,r)

lbl1 = Label(vent, text="Primer número", bg="yellow")
lbl1.place(x=10, y=10, width=100, height=30)

txt1 = Entry(vent, bg="Pink")
txt1.place(x=120, y=10, width=100, height=30)

lbl2 = Label(vent, text="Segundo número", bg="yellow")
lbl2.place(x=10, y=50, width=100, height=30)

txt2 = Entry(vent, bg="Pink")
txt2.place(x=120, y=50, width=100, height=30)

btnSuma = Button(vent, text="Sumar", command=fnSuma)
btnSuma.place(x=10, y=90, width=100, height=30)

lbl3 = Label(vent, text="Resultado", bg="yellow")
lbl3.place(x=10, y=130, width=100, height=30)

txt3 = Entry(vent, bg="Pink")
txt3.place(x=120, y=130, width=100, height=30)

vent.mainloop()