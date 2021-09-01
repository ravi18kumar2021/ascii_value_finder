from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('ASCII value finder')
root.geometry('300x300+600+90')
root.resizable(False,False)
root.config(bg = 'ivory3')

# variable
count = 0

def find_ascii():
    user = entry.get()
    if len(user) == 1:
        a = ord(user)
        label_2.pack(pady = 15)
        label_2.config(text = f"ASCII value of {user} is {a}")
    elif len(user) > 1:
        global count
        if count == 0:
            label_2.pack(pady = 15)
            label_2.config(text = "XXXXX Invalid XXXXX")
            count += 1
        elif count > 0:
            messagebox.showwarning('Warning','Enter only one character !!')

label_1 = Label(root, text = "Enter a character here :",
                font = ('arial',18),fg = 'red', bg = 'ivory3')
label_1.pack(pady = 20)

entry = Entry(root,
              width = 5,
              font = ('arial',18),
              justify = 'center'
              )
entry.pack(pady = 20)

button = Button(root,
                width = 12,
                text = 'CLICK',
                font = ('times new roman',12,'bold'),
                bg = 'blue2', fg = 'goldenrod1',
                command = find_ascii)
button.pack(pady = 10)

label_2 = Label(root, font = ('arial',14,'italic'), bg = 'ivory3', fg = 'magenta2')

root.mainloop()