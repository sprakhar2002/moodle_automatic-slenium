import tkinter
from moodle import moodle
root = tkinter.Tk()
root.geometry('400x400')
root.title('Moodle_login')
BlankLine=tkinter.Label(root, text="")
BlankLine.pack()
HeadingLabel=tkinter.Label(root, text="Login to moodle",fg = "black",bg = "white",font ="Helvetica 16 bold italic")
HeadingLabel.pack()
button=tkinter.Button(root, text="Login to moodle", fg="Blue" , command=moodle)
button.pack( expand=True)
root.mainloop()