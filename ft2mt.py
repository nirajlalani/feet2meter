from tkinter import Tk,DoubleVar,Label,Entry,Button

window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="lightgreen")
window.geometry("320*320")
window.resizable(width=False,height=False)

ft_lbl = Label(window,text="Feet",bg="purple",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)