import pandas as pd

df = pd.read_csv('student.csv')
print("Student Data:")
print(df)

#It calculates the average score of the the class
average_marks =df["Marks"].mean()
print("Average Marks:", average_marks)

#It finds students who scored below average
below_average_students = df[df["Marks"] < average_marks]
print("Students with below average marks:")
print(below_average_students)

#It identifies the top scorers
top_scorer = df[df["Marks"] >= 90]
print("Top Scorer:", top_scorer)

#It adds a new column 'Performance' based on marks
def performance(marks):
    if marks < average_marks:
        return "Needs Improvement"
    elif marks < 90:
        return "Good"
    else:
        return "Excellent"

df["Performance"] = df["Marks"].apply(performance)

def attendance_status(attendance):
    if attendance < 75:
        return "Low Attendance"
    else:
        return "OK"

df["Attendance_Status"] = df["Attendance"].apply(attendance_status)
print("\nUpdated Student Report with Attendance Status:")
print(df)

print("\nFinal Student Report:")
print(df)
df.to_csv("final_student_report.csv", index=False)
print("\nFinal report saved as final_student_report.csv")

