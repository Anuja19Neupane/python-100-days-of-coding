from tkinter import *
from tkinter import messagebox
import random

 # ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*',
            '(', ')', '_', '+', '|', '}', '{', ':', ';'',', '<', '>', '?', '.', ]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    nr_letters=random.randint(8,10)
    nr_symbols=random.randint(2,4)
    nr_numbers=random.randint(2,4)




    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_letters)]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    # terminal ma print hunxa simpy print garyo vaney bur we want to print it in password box


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
# to fetch current entry text,use the get method:
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="OPPS!!",message="please make sure not to leave any field empty.")

    is_ok=messagebox.askokcancel(title=website,message=f"Email: {email}"f"\nPassword:{password} \nIs it ok to save?")
    if is_ok:
        with open("day_29/data.txt","a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            # "a" and "w " le file xaina vaney panii create garxa
            # a vaneko append ho
            website_entry.delete(0,END) 
            password_entry.delete(0,END)
            # ek palta varera add gareypaxi data haru delete hunxa so you can enter again

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(height=200,width=200)
# canvas vankeo screen vaney jasto ho
#"""Canvas widget to display graphical elements like lines or text."""
#  we can place graphics, text, widgets or frames on a Canvas.
logo_img=PhotoImage(file="day_29/logo.png")
canvas.create_image(100,100,image=logo_img)
# x-position=100
# y-position=100
#logo_img vaneko image ko name deko
canvas.grid(row=0,column=1)


# label
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label=Label(text="password:")
password_label.grid(row=3,column=0)


# entry

website_entry=Entry(width=40)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
# focus le cursor rakhxa
# columnspan vaneko katiikolamo, 2 vannu ko matlab column 2 samma yei huu vaneko
email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anujaneupane20@gmail.com")
#0 position ma vaneko
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

# buttons
generate_password_button=Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)






window.mainloop()