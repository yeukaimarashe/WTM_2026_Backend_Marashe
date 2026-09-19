# Student Information Manager

student_name = "Yeukai Marashe"
student_age = 33
student_height = 1.55
is_currently_enrolled = True
student_subjects = ["Python", "HTML", "CSS", "JavaScript", "SQL"]

print(f"First Subject: {student_subjects[0]}")
student_subjects.append("Django")
student_subjects.remove("CSS")
print(f"Student Subjects: {student_subjects}")

favourite_numbers = (7, 10, 25)
print(f"Favourite Number: {favourite_numbers[1]}")

student_hobbies = {"Reading", "Gaming", "Football", "Reading"}
print(f"Student Hobbies: {student_hobbies}")
# Note: The set will only contain unique values, so "Reading" will only appear once in the output.
student_hobbies.add("Cooking")


student_info = {
    "Name": student_name,
    "Age": student_age,
    "Height": student_height,
    "Enrolled": is_currently_enrolled,
    "Subjects": student_subjects,
    "Favourite Numbers": favourite_numbers,
    "Hobbies": student_hobbies,
}
print(f"Student Name: {student_info['Name']}")
print(f"Skills: {student_info['Subjects']}")

student_info["Country"] = "Uganda"
student_info.update({"Age": 34})

print(f"Updated Student Info: {student_info}")




