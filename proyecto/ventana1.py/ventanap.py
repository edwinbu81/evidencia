from tkinter import*
 
def miFuncion():
    print ("Este es un mensaje del botón")
ventana = Tk()  
ventana.geometry("400x200")
ventana.title("Hola Mundo")
 
 
 
label = Label(ventana, text="Este es un label")
label = Pack()
 
 
btn = Button (ventana, text="Presionar aqui", bg="blue", command = miFuncion)
btn.pack()
 
ventana.mainloop()