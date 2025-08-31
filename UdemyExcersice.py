from tkinter import *


def button_clicked():
    input_text = input.get()
    my_label.config(text= input_text)#Updating label if Button class is clicked and command executed
    print("I got clicked")

window = Tk()
window.title("Temperature Converter")
window.wm_minsize(width=500, height=300) #will auto adjust depending on what you have within the window - Default if starting
#can add padding to the whole, or in individual components
window.config(padx= 30) # Creating a padding/buffer between components

#Label
miles_label = Label(text="Miles", padx=50, pady=50, font=("Arial", 18, "bold")) #doesn't display automatically
is_equal_to_label = Label(text="is equal to", font=("Arial", 14, "italic"))
Km_label = Label(text="Km", font=("Arial", 18, "bold"))
# my_label.pack() #Automatically centers text on the screen, if you create a second Object, it will populate below this
miles_label.grid(column= 2, row= 0)
is_equal_to_label.grid(column= 0, row=1) #top left corner
Km_label.grid(column= 2, row = 1)
# miles_label.config(padx=50, pady=50) #adding space around widgets

#Can also create buttons
button = Button(text="Calculate", command=button_clicked) #don't need parenthesis at the end because we are not calling the function
button.grid(column= 1, row=2)
# button.pack()

# Entry Component (input)
miles_input = Entry(width=10)
miles_input.grid(column= 1, row=0)

#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
