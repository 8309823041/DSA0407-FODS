
import numpy as np

# Marks of 4 students in 4 subjects
# Columns: Math, Science, English, History
student_scores = np.array([
    [85, 90, 78, 88],
    [92, 85, 80, 75],
    [78, 95, 85, 82],
    [88, 80, 90, 86]
])

subjects = ["Math", "Science", "English", "History"]

# Calculate average marks for each subject
average_scores = np.mean(student_scores, axis=0)

print("Average marks for each subject:")

for subject, average in zip(subjects, average_scores):
    print(f"{subject}: {average:.2f}")

# Find the subject with the highest average
highest_index = np.argmax(average_scores)

print("\nSubject with the highest average:",
      subjects[highest_index])
print("Highest average score:",
      average_scores[highest_index])
