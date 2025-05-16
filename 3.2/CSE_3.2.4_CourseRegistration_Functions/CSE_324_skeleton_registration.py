from CSE_324_course import Course
from CSE_324_skeleton_student import Student

math = ("Algebra I")
language = ("Spanish I")
science = ("Earth Science")
history = ("U.S. History I")
phys_ed = ("Physical Education I")

# Add two more courses of your choosing
student_list = []

computer_science = ("Computer Science I")
engineering = ("Engineering Essentials")

test_student = ("Jill", "Sample")
student_list.append(math)
student_list.append(language)
student_list.append(science)
student_list.append(history)

student_list2 = []
test_student2 = ("Bill", "Sample")
student_list2.append(math)
student_list2.append(phys_ed)
student_list2.append(science)
student_list2.append(history)

#TODO Add a third test student and assign them four classes

student_list3 = []
test_student3 = ("Harsha", "Malipeddi")
student_list3.append(math)
student_list3.append(language)
student_list3.append(science)
student_list3.append(history)
student_list3.append(computer_science)
student_list3.append(engineering)


#TODO Add all the test students to a list of your own creation
all_students = [test_student, test_student2, test_student3]
all_courses = [student_list, student_list2, student_list3]

#TODO print student_list
print(all_students[0], all_courses[0], "\n", all_students[1], all_courses[1], "\n", all_students[2], all_courses[2])

#TODO iterate over each of the students in the list and print their names and course schedules.
    #Each iteration should:
        #print the student
for student in all_students:
    print(student)
'''for this part you may need to review the other skeleton code to:
        - see how to get items from a list
        - see if there is code (like a function) in that file you can call in this file
        - verify that running this file gets you the correct output with information from that file
    Also, review syntax of pulling items from a list from other activities'''