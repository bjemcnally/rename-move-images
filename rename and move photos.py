# Goal: to open images from source (ex. camera), rename them, and then move them to appropriate long term locations
# sources of inspiration so far:
# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
# https://stackoverflow.com/questions/23901168/how-do-i-insert-a-jpeg-image-into-a-python-tkinter-window
import tkinter as tk
from tkinter.ttk import *
import os
from PIL import ImageTk, Image

#get list of cities
city_list = os.listdir("Cities")

#This creates the main window of an application
window = tk.Tk()
window.title("Let's Rename Appraisal Photos!")
window.geometry("900x900")
window.configure(background='white')

# two test images
path = "house.jpg"
path2 = "house2.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))
img2 = ImageTk.PhotoImage(Image.open(path2))

#get list of streets from chosen city directory
street_list = []
def get_streets(*args):
    """This sets the values of combo_streets based upon the selection in combo_cities"""
    sel = combo_cities.get()
    path_to_streets = "Cities/" + sel
    street_list = os.listdir(path_to_streets)
    combo_streets.config(values=street_list)

#set address for file naming and final location based upon users selections
full_address = ""
def clicked():
    """This will save the property address info"""
    subject_city = combo_cities.get()
    subject_street = combo_streets.get()
    subject_address = txt.get()
    full_address = subject_address + " " + subject_street + ", " + subject_city
    property_address.configure(text=full_address)

#First row selects and sets city, street, and house #
instructions = tk.Label(window, text="Select City and Street and set the house number in this first row")
instructions.grid(column=0, row=0)

combo_cities = Combobox(window, state="readonly")
combo_cities.bind("<<ComboboxSelected>>",get_streets)
combo_cities['values']= (city_list)
combo_cities.current(0) #set the selected item
combo_cities.grid(column=1, row=0)

combo_streets = Combobox(window, state="readonly") #remove readonly here? (later)
combo_streets['values']= (street_list)
combo_streets.grid(column=2, row=0)

txt = Entry(window, width=20)
txt.grid(column=3, row=0)

btn = Button(window, text="Set Address", command=clicked)
btn.grid(column=4, row=0)

#Subsequent rows show pictures and allows them to be renamed
property_address = tk.Label(window, text="Address will appear here")
property_address.grid(column=0, row=1)

#everything below here is still under construction/brainstorming phase
lbl_type_address = tk.Label(window, text="Type Address")
lbl_type_address.grid(column=1, row=1)
lbl_select_city = tk.Label(window, text="Select City")
lbl_select_city.grid(column=2, row=1)

display_img = tk.Label(window, image = img)
display_img.grid(column=0, row=2)
txt1 = tk.Entry(window, width=20)
txt1.grid(column=1, row=2)
combo = Combobox(window)
combo['values']= (city_list)
combo.current(0) #set the selected item
combo.grid(column=2, row=2)


display_img2 = tk.Label(window, image = img2)
display_img2.grid(column=0, row=3)

#Start the GUI
window.mainloop()