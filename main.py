import tkinter

window = tkinter.Tk()
window.title("My First GUID Program")
window.wm_minsize(width=500, height=300) #will auto adjust depending on what you have within the window - Default if starting

#componnent use
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold")) #doesn't display automatically
# create the label then specify how it is laid out on screen. Notice that parameters do now show within parenthesis
my_label.pack(side= "left") #Automatically centers text on the screen, if you create a second Object, it will populate below this

# How come arguments are not being listed in properties, but can be used by typping them in
#Advanced Arguments
 #Keyword Arguments
    #Solve by creating arugments that have default values - Chagne function declaration
    # def my_function(a=1, b=2, c=3):
        #do this with a
        #then do this with b
    #my_function() - does not require keyword arguments if you are going to change declaration above "Prime" the function
    # What if I want to modify b?
        #my_function(b = 5)







#Always has to be at the end of the program
window.mainloop() # Keeps window on screen and listens for waht user will do to interact with
