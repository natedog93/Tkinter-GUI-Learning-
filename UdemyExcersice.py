from tkinter import *

# def miles_to_km():
#     miles = float(user_input.get())
#     miles_to_km = miles * 1.60934
#     pass


def calculate_clicked():
    input_int = float(user_input.get()) #converting str to float
    miles_to_km = round((input_int * 1.60934), 2)
    farenheight_conversion_label.config(text= miles_to_km)#Updating label if Button class is clicked and command executed
    # print("I got clicked")

window = Tk()
window.title("Temperature Converter")
window.wm_minsize(width=300, height=150) #will auto adjust depending on what you have within the window - Default if starting
#can add padding to the whole, or in individual components
window.config(padx= 20, pady= 20) # Creating a padding/buffer between components

#Label
miles_label = Label(text="Miles", font=("Arial", 18, "bold")) #doesn't display automatically
is_equal_to_label = Label(text="is equal to", font=("Arial", 16, "italic"))
Km_label = Label(text="Km", font=("Arial", 18, "bold"))
farenheight_conversion_label = Label(text="0", font=("Arial", 14, "bold"))
# assigning grids for all labels
miles_label.grid(column= 2, row= 0, sticky = "w")
is_equal_to_label.grid(column= 0, row=1, sticky = "e") #top left corner
Km_label.grid(column= 2, row = 1, padx= 2, sticky = "w")
farenheight_conversion_label.grid(column = 1, row = 1, sticky = "e")

#calculate Button
calculate = Button(text="Calculate", command = calculate_clicked) #don't need parenthesis at the end because we are not calling the function
calculate.grid(column= 1, row=2)

# Miles Input
user_input = Entry(width=10, justify="right", takefocus=1) #Creating a str by default, need to change to float when calculating
user_input.grid(column= 1, row=0)
user_input.focus() #places curser in Entry once the program is run and so that the user does not have to click

#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
