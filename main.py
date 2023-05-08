import string
import random
import tkinter as tk

def Generate_password():
	password=""
	length=10
	for i in range(length):
		if i%2==0:
			password=password+random.choice(string.ascii_letters)
		else:
			password=password+random.choice(string.digits)
	password_label.config(text="Random Password Generator:"+password)

#Tkinter window creaton
window=tk.Tk()
window.title("Password_Generator")
window.geometry("500x300")
window.configure(bg="Purple")
window.resizable(False,False)

#Button creation For Password Generator
generate_button=tk.Button(window,text="Generate Password",command=Generate_password,bg="light yellow",font=("bold",10))
generate_button.pack()

#Label creation
password_label=tk.Label(window,text="",bg="White",font=("bold,5"))
password_label.pack()
#Run on Window
window.mainloop()


