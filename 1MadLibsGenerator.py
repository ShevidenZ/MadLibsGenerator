from tkinter import Button ,Tk , Label
root = Tk()
root.geometry('300x300')
root.title("Mad Libs Generator")
Label(root, text="MadLibsGenerator", font ="arial 20 bold").pack()
Label(root, text="Click Any One :", font= "arial 15 bold").place(x=40, y=80)

def madlib1():
    animals = input("enter a animal name: ")
    profession = input("enter a profession name: ")
    cloth = input("enter a piece of cloth name: ")
    things = input("enter a thing name: ")
    name = input("enter a name: ")
    place = input("enter a place name: ")
    verb = input("enter a verb in ing from: ")
    food = input("food name: ")
    print('say' + food +', the photographer said as the camera flashed! ' + name +' and i had gone to'+ place +'to get our pjotos take on my birthday. the first photo we realy wanted was picture of us dressed as '+ animals +'pretending to be a '+ profession +'.when we saw the second photo, it was exacly what i wanted. we both looked like '+ things +'wearing'+ cloth +'and '+ verb +'--exactly what i had to mind')

Button(root, text="Photographer", font="arial 15", command= madlib1, bg="ghost white").place(x=60, y=120)

root.mainloop()