import tkinter as tk

def create_course_boxes():
    global course_boxes
    
    # Clear existing course boxes
    for box in course_boxes:
        box.destroy()
    
    # Create new course boxes
    num_courses = int(course_dropdown.get())
    course_boxes = []
    for i in range(num_courses):
        course_label = tk.Label(root, text=f"Course {i+1}:")
        course_label.grid(row=i+2, column=0, padx=5, pady=5)
        credits_label = tk.Label(root, text="Credits:")
        credits_label.grid(row=i+2, column=1, padx=5, pady=5)
        credits_box = tk.Entry(root)
        credits_box.grid(row=i+2, column=2, padx=5, pady=5)
        grade_label = tk.Label(root, text="Grade:")
        grade_label.grid(row=i+2, column=3, padx=5, pady=5)
        grade_box = tk.Entry(root)
        grade_box.grid(row=i+2, column=4, padx=5, pady=5)
        course_boxes.append((course_label, credits_box, grade_box))

root = tk.Tk()
root.title("Course Information")

# Course selection dropdown
course_label = tk.Label(root, text="Select number of courses:")
course_label.grid(row=0, column=0, padx=5, pady=5)
course_options = list(range(1, 11))
course_dropdown = tk.StringVar(root)
course_dropdown.set(course_options[0])
course_dropdown_menu = tk.OptionMenu(root, course_dropdown, *course_options, command=create_course_boxes)
course_dropdown_menu.grid(row=0, column=1, padx=5, pady=5)

# Create initial course boxes
course_boxes = []
create_course_boxes()

root.mainloop()

