from tkinter import *
from tkinter import messagebox
import os
import platform

main = Tk()
main.geometry('1366x768')
main.title('KKK Super Market')

def employee():
	main.withdraw()
	if platform.system() == 'Linux':
		os.system('python3 employee.py')
	else:
		os.system('python employee.py')
	main.deiconify()

def admin():
	main.withdraw()
	if platform.system() == 'Linux':
		os.system('python3 admin.py')
	else:
		os.system('python admin.py')
	main.deiconify()

def Exit():
	exit = messagebox.askyesno("Exit",'Are you sure you want to exit?', parent=main)
	if exit == True:
		main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)

label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img0 = PhotoImage(file='./images/main/front-page.png')
label1.configure(image=img0)

button1 = Button(main)
button1.place(relx=0.75, rely=0.4, width=100, height=100)
button1.configure(relief='flat')
button1.configure(overrelief='flat')
button1.configure(activebackground="#8BF5FA")
button1.configure(cursor='hand2')
button1.configure(foreground='#8BF5FA')
button1.configure(background='#8BF5FA')
button1.configure(borderwidth='0')
img1 = PhotoImage(file='./images/main/employees.png')
button1.configure(image=img1)
button1.configure(command=employee)

button2 = Button(main)
button2.place(relx=0.85, rely=0.4, width=100, height=100)
button2.configure(relief='flat')
button2.configure(overrelief='flat')
button2.configure(activebackground='#8BF5FA')
button2.configure(cursor='hand2')
button2.configure(foreground='#8BF5FA')
button2.configure(background='#8BF5FA')
button2.configure(borderwidth='0')
img2 = PhotoImage(file='./images/main/admin.png')
button2.configure(image=img2)
button2.configure(command=admin)

main.mainloop()