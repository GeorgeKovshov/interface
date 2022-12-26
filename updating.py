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

# Function to delete a record
def delete():
    # you have to connect inside the function too
    conn = sqlite3.connect('address_book.db')
    # and make a cursor
    cursor = conn.cursor()

    cursor.execute(("DELETE from adresses WHERE oid= " + delete_box.get()))

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Create Edit Function
def update():
    # you have to connect inside the function too
    conn = sqlite3.connect('address_book.db')
    # and make a cursor
    cursor = conn.cursor()

    record_id = delete_box.get()
    cursor.execute(""" UPDATE adresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        WHERE oid = :oid""",
                   {
                       'first': f_name_editor.get(),
                       'last': l_name_editor.get(),
                       'address': address_editor.get(),
                       'city': city_editor.get(),
                       'state': state_editor.get(),
                       'zipcode':zipcode_editor.get(),

                       'oid': record_id
                   }
                   )

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

    editor.destroy()
    '''
    f_name_editor.delete(0, END)
    l_name_editor.delete(0, END)
    address_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zipcode_editor.delete(0, END)
    '''

def edit():
    global editor
    editor = Tk()
    editor.title("Update a Record")
    editor.geometry("400x400")

    # you have to connect inside the function too
    conn = sqlite3.connect('address_book.db')
    # and make a cursor
    cursor = conn.cursor()


    record_id = delete_box.get()
    # query the database
    cursor.execute("SELECT * FROM adresses WHERE oid= " + record_id)  # oid is the primary key (sqlite3 also makes unique ids for you)
    records = cursor.fetchall()  # fetchmany(50)

    #create global variable
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor



    # Creating text boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))  # padding in tuple - specify one side and the other
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)
    # Create text box labels
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="city")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="state")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="zipcode")
    zipcode_label.grid(row=5, column=0)

    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # Create an Save Button
    edit_btn = Button(editor, text="Save Record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()


# Create Submit Function for database
def submit():
    # you have to connect inside the function too
    conn = sqlite3.connect('address_book.db')
    # and make a cursor
    cursor = conn.cursor()

    #Insert Into Table
    cursor.execute("INSERT INTO adresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
                   {
                       'first_name': f_name.get(),
                       'last_name': l_name.get(),
                       'address': address.get(),
                       'city': city.get(),
                       'state': state.get(),
                       'zipcode': zipcode.get()
                   })

    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

# Create Query Function
def query():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # create a cursor
    cursor = conn.cursor()

    #query the database
    cursor.execute("SELECT *, oid FROM adresses") # oid is the primary key (sqlite3 also makes unique ids for you)
    records = cursor.fetchall() #fetchmany(50)
    #print(records)
    print_records = ''
    #for record in records[0]:
    for record in records:
        print_records += str(record) + '\n'

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()


#Creating text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0)) # padding in tuple - specify one side and the other

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

#Create text box labels

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column= 0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column= 0)

address_label = Label(root, text="address")
address_label.grid(row=2, column= 0)

city_label = Label(root, text="city")
city_label.grid(row=3, column= 0)

state_label = Label(root, text="state")
state_label.grid(row=4, column= 0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column= 0)

#Create submit button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)
delete_box_label = Label(root, text="ID Number")
delete_box_label.grid(row=9, column=0)

#cREATE a delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Commit Changes
conn.commit()

#Close connection
conn.close()

mainloop()