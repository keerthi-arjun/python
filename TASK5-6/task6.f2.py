students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']

student_subject_dict = {student: subject for student, subject in zip(students, subjects)}

print("Using a dictionary comprehension:")
print(student_subject_dict)
