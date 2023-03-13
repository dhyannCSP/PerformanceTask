import tkinter as tk
from tkinter import *


def create_course_boxes(*args):
    global course_boxes, calculate_button
    
    # Remove previous course boxes and Calculate GPA button
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Entry, tk.Button)):
            widget.destroy()
    
    # Create new course boxes
    num_courses = int(course_dropdown.get())
    course_boxes = []
    for i in range(num_courses):
        course_label = tk.Label(root, text=f"Course {i+1}:")
        course_label.grid(row=i+2, column=0)
        credits_box = tk.Entry(root)
        credits_box.grid(row=i+2, column=1)
        grade_box = tk.Entry(root, validate="key")
        grade_box.config(validatecommand=(grade_box.register(lambda char: char.isalpha()), '%S'))
        grade_box.grid(row=i+2, column=2)
        course_boxes.append((course_label, credits_box, grade_box))
    
    # Create Calculate GPA button
    calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
    calculate_button.grid(row=num_courses+2, column=1)


def calculate_gpa():
    total_credits = 0
    total_grade_points = 0
    for course_box in course_boxes:
        credits = float(course_box[1].get())
        grade = course_box[2].get().upper()
        if grade == 'A':
            grade_points = 4.0
        elif grade == 'B':
            grade_points = 3.0
        elif grade == 'C':
            grade_points = 2.0
        elif grade == 'D':
            grade_points = 1.0
        else:
            grade_points = 0.0
        total_credits += credits
        total_grade_points += credits * grade_points
    gpa = total_grade_points / total_credits
    gpa_label = tk.Label(root, text=f"GPA: {gpa:.2f}")
    gpa_label.grid(row=len(course_boxes)+3, column=1)


root = tk.Tk()
root.title("GPA Calculator")
root.minsize(500,400)

tk.Label(root, text="Select number of courses:").grid(row=0, column=0)
course_options = list(range(1, 7))
course_dropdown = tk.StringVar(root)
course_dropdown.set(course_options[0])
course_dropdown.trace("w", create_course_boxes)  # Call create_course_boxes whenever the dropdown value changes
tk.OptionMenu(root, course_dropdown, *course_options).grid(row=0, column=1)

# Create initial course boxes and Calculate GPA button
course_boxes = []
calculate_button = tk.Button(root, text="Calculate GPA", command=calculate_gpa)
calculate_button.grid(row=2, column=1)
course_boxes.append((None, tk.Entry(root), tk.Entry(root, validate="key")))

root.mainloop()
