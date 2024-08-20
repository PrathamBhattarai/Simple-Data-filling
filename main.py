import tkinter
from tkinter import ttk

def enter_data():
    #User info
    firstname = first_name_entry.get()
    lastname = last_name_entry.get()
    title = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()

    #course info
    isregistered = reg_status_var.get()
    CompletedCourses = completedcourse_spinbox.get()
    Semester = semester_spinbox.get()

    #Terms and Conditions
    is_TermsandCondition_Accepted = Termsandcondtion_status.get()


    print("First Name: ", firstname, "Last Name: ", lastname)
    print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
    print("# courses: ", CompletedCourses, "# Semesters: ",  Semester)
    print(" Is Registered? ", isregistered, "Is Terms and Condtions accepted? ", is_TermsandCondition_Accepted)
    print("---------------------------------------")


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# saving User Info
user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 0, column =0, padx = 20, pady = 10)

first_name_label = tkinter.Label(user_info_frame, text = "First Name")
first_name_label.grid(row =0, column = 0)
last_name_label = tkinter.Label(user_info_frame, text = "Last Name")
last_name_label.grid( row = 0, column = 1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row = 1, column = 0)
last_name_entry.grid(row = 1, column = 1)

title_label = tkinter.Label(user_info_frame, text = "Title")
title_combobox = ttk.Combobox(user_info_frame, values = ["", "Mr.", "Mrs.", "Dr."])
title_label.grid(row= 0, column = 2)
title_combobox.grid(row=1, column= 2)

age_label =tkinter.Label(user_info_frame, text = "Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 18, to = 110 )
age_label.grid(row = 2, column = 0)
age_spinbox.grid(row = 3, column = 0)

nationality_label = tkinter.Label(user_info_frame, text = "Nationality" )
nationality_combobox = ttk.Combobox(user_info_frame, values = ["Africa", "Antartica", "Europe", "South America", "North America", "Asia", "Oceania"])
nationality_label.grid(row = 2, column =1)
nationality_combobox.grid(row = 3, column = 1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady= 5)

# Saving course info
course_info_frame = tkinter.LabelFrame(frame, text = "Course Information")
course_info_frame.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)

registration_label = tkinter.Label(course_info_frame, text = "Ragistration Status")

reg_status_var = tkinter.StringVar()
registration_checkbutton = tkinter.Checkbutton(course_info_frame, text = "Currently Registered", variable = reg_status_var, onvalue= "Resgistered", offvalue = "Not Registered")


registration_label.grid(row = 0, column = 0)
registration_checkbutton.grid(row = 1, column = 0)

completedcourse_label = tkinter.Label(course_info_frame, text = "#Completed Courses")
completedcourse_spinbox = tkinter.Spinbox(course_info_frame, from_= 1, to =4 )
completedcourse_label.grid(row = 0, column = 1)
completedcourse_spinbox.grid(row = 1, column= 1)

semester_label = tkinter.Label(course_info_frame, text = "#Semesters")
semester_spinbox = tkinter.Spinbox(course_info_frame, from_= 1, to = 8)
semester_label.grid(row = 0, column=2 )
semester_spinbox.grid(row =1, column = 2)

for widget in course_info_frame.winfo_children():
    widget.grid_configure(padx = 10,  pady = 5)


# Accepting terms and conditions
termsandcondition_label = tkinter.LabelFrame(frame, text = "Terms And Conditions", padx = 20, pady = 20)
termsandcondition_label.grid(row = 2, column = 0, sticky = "news", padx = 20, pady = 10)

Termsandcondtion_status = tkinter.StringVar()
termsandcondition_checkbutton = tkinter.Checkbutton(termsandcondition_label, text = "I accept the terms and conditions", variable = Termsandcondtion_status, onvalue = "Aceepted", offvalue= "Not Accepted")


termsandcondition_checkbutton.grid(row = 0, column = 1)

for widget in termsandcondition_label.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)

button = tkinter.Button(frame, text = "Enter Data", command = enter_data)
button.grid(row = 3, column=0, sticky = "news", padx = 20, pady = 10)


window.mainloop()