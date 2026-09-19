# Student Grade Evaluator & Class Performance Tracker

count = int(input("How many student entries do you want to create? "))
student_records = {}
print("\n")
for i in range(count):
    print(f"--- Entry {i + 1} ---")
    name = input(f"Enter student name {i + 1}: ")
    Score = float(input(f"Enter score (0-100): {name}: "))
    student_records[name] = Score

# Track student pass/fail metrics
total_passed = 0
total_failed = 0

print("\n")
print("=" * 40)
print("EVALUATION RESULTS")
print("=" * 40)


# Calculate student grades.
for name, Score in student_records.items():
    if Score >= 70:
        print(f"- {name}: Score: {Score:.2f} | Grade A | Passed with Distinction")
        total_passed += 1
    elif Score >= 50:
        print(f"- {name}: Score: {Score:.2f} | Grade B | Passed")
        total_passed += 1
    else:
        print(f"- {name}: Score: {Score:.2f} | Grade C | Needs Improvement")
        total_failed += 1
print("\n")

# Calculate class average.
total_score = sum(student_records.values())
average_score = total_score / count

print("=" * 40)
print("CLASS PERFORMANCE")
print("=" * 40)
print(f"\nClass Average: {average_score:.2f}")
print(f"Total Passed: {total_passed}")
print(f"Total Failed: {total_failed}")
