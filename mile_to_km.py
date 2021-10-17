import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

label1 = tkinter.Label(text="is equal to", font=("Arial", 18))
label1.grid(column=0, row=1)
label1.config(padx=20, pady=20)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

label2 = tkinter.Label(text="Miles", font=("Arial", 18))
label2.grid(column=2, row=0)
label2.config(padx=20, pady=20)

label3 = tkinter.Label(text="0", font=("Arial", 18))
label3.grid(column=1, row=1)
label3.config(padx=20, pady=20)

label4 = tkinter.Label(text="Km", font=("Arial", 18))
label4.grid(column=2, row=1)
label4.config(padx=20, pady=20)


def button_clicked():
    something = float(input.get())
    label3["text"] = round(something*(1.609))


button = tkinter.Button(text="Calculate", command = button_clicked)
button.grid(column=1, row=2)

window.mainloop()