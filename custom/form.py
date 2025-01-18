from tkinter import *

root = Tk()

def register():
    name_info = name_value.get()
    phone_info = phone_value.get()
    gender_info = gender_value.get()
    email_info = email_value.get()

    file = open(name_info + ".txt", 'w')
    file.write(name_info + '\n')
    file.write(phone_info + '\n')
    file.write(gender_info + '\n')
    file.write(email_info + '\n')


root.title("Registration")
root.geometry("600x470")
root.resizable(False, False)

Label(root, text='python registration form', font='Arial 25').pack(pady=50)

Label(text='Name', font=23).place(x=100, y=150)
Label(text='Phone', font=23).place(x=100, y=200)
Label(text='Gender', font=23).place(x=100, y=250)
Label(text='Email', font=23).place(x=100, y=300)

name_value = StringVar()
phone_value = StringVar()
gender_value = StringVar()
email_value = StringVar()

name_entry = Entry(root, textvariable=name_value, width=30, bd=2, font=20)
phone_entry = Entry(root, textvariable=phone_value, width=30, bd=2, font=20)
gender_entry = Entry(root, textvariable=gender_value, width=30, bd=2, font=20)
email_entry = Entry(root, textvariable=email_value, width=30, bd=2, font=20)

name_entry.place(x=200, y=150)
phone_entry.place(x=200, y=200)
gender_entry.place(x=200, y=250)
email_entry.place(x=200, y=300)

check_value = IntVar
check_button = Checkbutton(text='remember me', variable=check_value).place(x=195, y=330)

Button(text='register', font=20, width=29, height=1, command=register).place(x=200, y=370)



root.mainloop()