# import tkinter
#Alternatively, you could do the below to import all classes - Don't need the tkinter. when initializing anymore
from tkinter import *

window = Tk()
window.title("My First GUID Program")
window.wm_minsize(width=500, height=300) #will auto adjust depending on what you have within the window - Default if starting

#componnent use
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold")) #doesn't display automatically
# create the label then specify how it is laid out on screen. Notice that parameters do now show within parenthesis
my_label.pack(side= "left") #Automatically centers text on the screen, if you create a second Object, it will populate below this

#How we configure or change the properties of a particular component that we have created
my_label["text"] = "New Text"
my_label.configure(text="New Text")

#Can also create buttons
button = Button



#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
