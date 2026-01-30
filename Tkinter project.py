#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *

# ---------------- WINDOW SETUP ----------------
root = Tk()
root.title("Sharma Sweets Order Form")
root.geometry("644x344")

# ---------------- FUNCTIONS ----------------
def getvals():
    name = namevalue.get()
    phone = phonevalue.get()
    gender = gendervalue.get()
    emergency = emergencyvalue.get()
    payment = paymentmodevalue.get()
    food_service = foodservicevalue.get()

    print("Submitting form")
    print(name, phone, gender, emergency, payment, food_service)

    with open("records.txt", "a") as f:
        f.write(
            f"Name: {name}, Phone: {phone}, Gender: {gender}, "
            f"Emergency: {emergency}, Payment: {payment}, "
            f"Prebook Meal: {food_service}\n"
        )

# ---------------- HEADING ----------------
Label(
    root,
    text="Welcome to Sharma Sweets",
    font="comicsansms 13 bold",
    pady=15
).grid(row=0, column=3)

# ---------------- FORM LABELS ----------------
Label(root, text="Name").grid(row=1, column=2)
Label(root, text="Phone").grid(row=2, column=2)
Label(root, text="Gender").grid(row=3, column=2)
Label(root, text="Emergency Contact").grid(row=4, column=2)
Label(root, text="Payment Mode").grid(row=5, column=2)

# ---------------- VARIABLES ----------------
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# ---------------- ENTRY FIELDS ----------------
Entry(root, textvariable=namevalue).grid(row=1, column=3)
Entry(root, textvariable=phonevalue).grid(row=2, column=3)
Entry(root, textvariable=gendervalue).grid(row=3, column=3)
Entry(root, textvariable=emergencyvalue).grid(row=4, column=3)
Entry(root, textvariable=paymentmodevalue).grid(row=5, column=3)

# ---------------- CHECKBOX ----------------
Checkbutton(
    root,
    text="Want to prebook your meals?",
    variable=foodservicevalue
).grid(row=6, column=3)

# ---------------- SUBMIT BUTTON ----------------
Button(
    root,
    text="Submit to Sharma Sweets",
    command=getvals
).grid(row=7, column=3)

root.mainloop()


# In[ ]:





# In[ ]:




