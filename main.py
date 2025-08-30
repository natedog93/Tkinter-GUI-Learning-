# import tkinter
#Alternatively, you could do the below to import all classes - Don't need the tkinter. when initializing anymore
from tkinter import *


def button_clicked():
    input_text = input.get()
    my_label.config(text= input_text)#Updating label if Button class is clicked and command executed
    print("I got clicked")

window = Tk()
window.title("My First GUID Program")
window.wm_minsize(width=500, height=300) #will auto adjust depending on what you have within the window - Default if starting
#can add padding to the whole, or in individual components
window.config(padx= 50, pady= 20) # Creating a padding/buffer between components

#Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold")) #doesn't display automatically
# create the label then specify how it is laid out on screen. Notice that parameters do now show within parenthesis
#How we configure or change the properties of a particular component that we have created
# my_label["text"] = "New Text"
my_label.configure(text="New Text")
# my_label.pack() #Automatically centers text on the screen, if you create a second Object, it will populate below this
my_label.grid(column= 0, row=0) #top left corner
my_label.config(padx=50, pady=50) #adding space around widgets
# my_label.pack()

#Can also create buttons
button = Button(text="Click Me", command=button_clicked) #don't need parenthesis at the end because we are not calling the function
button.grid(column= 1, row=1)
# button.pack()

#Entry Component (input)
input = Entry(width=10)
print(input.get())
input.grid(column= 2, row=0)
# input.pack()

#Text
text = Text(height=1, width=1)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "New multi-line text entry for coding challenge.")
#Get's current value in textbox at line 1, character 0
text.grid(column= 3, row= 2)

# Defining the layouts and positioning of widgets
#Pack, Place, Grid
    #Pack - is next to each other in a defaulted format from top to bottom - can  use parameter of side="left", right,bottom
    #Place - uses coordinate system - have to be very specific, just like turtle graphics.
        #What if you have 50 widgets?
    #Grid - Entire program is a grid divided into columns and rows
        #can't use pack with this
#How to add padding aruond components







#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
