import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=400)


# label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
# my_label["text"] = 'new text'
my_label.config(text="new text")
my_label.place(x=0, y=0)
# my_label.pack()
# my_label.grid(column=0, row=2)


# Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="click me", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=10)
input.pack()

# replace : repalcement of pack for complex locations


window.mainloop()

