import tkinter

window = tkinter.Tk()
window.title("My First GUID Program")
window.wm_minsize(width=500, height=300) #will auto adjust depending on what you have within the window - Default if starting

#componnent use
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold")) #doesn't display automatically
# create the label then specify how it is laid out on screen. Notice that parameters do now show within parenthesis
my_label.pack(side= "left") #Automatically centers text on the screen, if you create a second Object, it will populate below this




#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
