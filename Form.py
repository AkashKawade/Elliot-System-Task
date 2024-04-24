import re
from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry("1000x600")
root.resizable(False,False)
root.title(" Employee Form ")
root.configure(bg="white")
root.iconbitmap("form.ico")

def save_info():
    username = username_entry.get()
    email = email_entry.get()
    designation = designation_entry.get()
    depat = depat_entry.get()


    # Create a dictionary to store the data
    data = {
        "User Name": username,
        "Email ID": email,
        "Designation": designation,
        "Department": depat,
    }
    x=0
    for key, value in data.items():
        show_win = Label(root,text=f"{key}: {value}", font=("Arial", 16), bg="white")
        show_win.place(x=600,y=100+x)
        x+=30
    print("Successfully Submitted")

    # Check if any field is left empty
    if not all([username, email, designation, depat]):
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not re.match("^[A-Za-z]+$", username):
        messagebox.showerror("Error", "Please fill valid Username")
        return

    if not re.findall("@gmail.com\Z", email):
        messagebox.showerror("Error", "Please fill valid Email Id")
        return

    if not re.match("^[A-Za-z]+$", designation):
        messagebox.showerror("Error", "Please fill valid Designation")
        return

    if not re.match("^[A-Za-z]+$", depat):
        messagebox.showerror("Error", "Please fill valid Department")
        return

    # Clear the entry widgets after submission
    username_entry.delete(0, END)
    email_entry.delete(0, END)
    designation_entry.delete(0, END)
    depat_entry.delete(0, END)


# Title Name
head_title = Label(text=" Employee Form",font=("Times", "30", "bold"),fg="red",bg="yellow")
head_title.place(x=100,y=25)

#labels abd entry
username = (Label(root,text="User Name",width=9,height=1,font=("times","20"),fg="blue"))
username.place(x=10,y=150)

username_entry = (Entry(root, fg="black",font=("arial 20 "),bd=5))
username_entry.place(x=200,y=150)

email = Label(root,text="Email ID",width=9,font=("times 20"),fg="blue")
email.place(x=10,y=220)

email_entry =Entry(root,fg="black",font=("arial 20"),bd=5)
email_entry.place(x=200,y=220)

designation = Label(root,text="Designation",width=9,font=("times 20"),fg="blue")
designation.place(x=10,y=290)

designation_entry =Entry(root,fg="black",font=("arial 20"),bd=5)
designation_entry.place(x=200,y=290)

depat = Label(root,text="Department",width=9,font=("times 20"),fg="blue")
depat.place(x=10,y=360)

depat_entry =Entry(root,fg="black",font=("arial 20"),bd=5)
depat_entry.place(x=200,y=360)

#Submit Button
submit = Button(root,text="SUBMIT",fg="blue",font=("times 20"),width=10,command=save_info)
submit.place(x=150,y=450)

root.mainloop()