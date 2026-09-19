# Part 5: Dictionaries
# 8. Student Profile

students = {
    "Name": "Yeukai Marashe",
    "Age": 33,
    "Course": "Computer Science",
    "Level": "Junior",
    "Skills": ["Python", "mySQL", "Firebase"]
}
print(students)
print(students["Name"])
students["Email"] = "yeukaimarashe@gmail.com"
students.update({"Level": "Senior"})
students.pop("Age")
print(students)
