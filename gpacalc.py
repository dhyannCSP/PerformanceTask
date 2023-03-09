#GPA Calculator that takes in amount of courses and depending on that gives option to tell how many credits each course is and the grade letter for each
#Calculator also gives recomendations of colleges based on GPA calculated. 
#GPA Calculator uses 3 lists. Grade letters, colleges, credits. 

import tkinter as tk
from tkinter import *


def create_course_boxes(*args):
    global course_boxes
    
    # Create new course boxes
    num_courses = int(course_dropdown.get())
    course_boxes = []
    for i in range(num_courses):
        course_label = tk.Label(root, text=f"Course {i+1}:")
        course_label.grid(row=i+2, column=0)
        credits_box = tk.Entry(root)
        credits_box.grid(row=i+2, column=1)
        grade_box = tk.Entry(root)
        grade_box.grid(row=i+2, column=2)
        course_boxes.append((course_label, credits_box, grade_box))

root = tk.Tk()
root.title("GPA Calculator")
root.minsize(500,400)

tk.Label(root, text="Select number of courses:").grid(row=0, column=0)
course_options = list(range(1, 7))
course_dropdown = tk.StringVar(root)
course_dropdown.set(course_options[0])
course_dropdown.trace("w", create_course_boxes)  # Call create_course_boxes whenever the dropdown value changes
tk.OptionMenu(root, course_dropdown, *course_options).grid(row=0, column=1)

# Create initial course boxes
course_boxes = []
create_course_boxes()


root.mainloop()