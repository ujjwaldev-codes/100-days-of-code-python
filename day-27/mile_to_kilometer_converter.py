FONT =("Arial", 12, "bold")
import tkinter
windows =tkinter.Tk()
windows.minsize(width =150,height= 100)
windows.config(padx=10, pady=20)
windows.title("Mile to Km Converter")
textinput = tkinter.Entry(width=20) # highlightthickness=20 --> doubt
textinput.grid(row=0, column=1)
label_1=tkinter.Label(text="Miles", font=FONT)
label_1.grid(row=0, column=2)
label_2=tkinter.Label(text="is equal to", font=FONT)
label_2.grid(row=1, column=0)
label_4=tkinter.Label(text="Km", font=FONT)
label_4.grid(row=1, column=2)
label_3=tkinter.Label(text="0", font=FONT)
label_3.grid(row=1, column=1)
def calc():
    label_3["text"]=1.5 * int(textinput.get())
button= tkinter.Button(text="Calculate", command=calc) # Can Implement font = FONT also in button ...
button.grid(row= 2, column=1)
windows.mainloop()
