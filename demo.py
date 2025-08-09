import matplotlib.pyplot as plt
student_names = ["Aria","Karan","Kiraan","Jmaila","Gini","kissam","Ginia","Tomas"]
student_marks = [40,50,35,43,26,36,25,40]
marks_perc = []
for x in student_marks:
    res = (x/50)*100
marks_perc.append(res)
print(marks_perc)
def mark_line_chart():
    plt.plot(student_names,student_marks)
    plt.title("Student Graph Chart! ")
    plt.xlabel(student_names)
    plt.ylabel(student_marks)
    plt.show()

mark_line_chart()