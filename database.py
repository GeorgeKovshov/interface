from tkinter import *
#from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Main window")
root.geometry("400x400")#change window size

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# create a cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE adresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer)
""")


#Commit Changes
conn.commit()

#Close connection
conn.close()

mainloop()