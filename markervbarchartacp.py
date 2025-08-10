import matplotlib.pyplot as plt
student_names = ["wow","Wowza","Kamza","kizaza","estanbulala","kirkza","soomath","kirosa"]
student_marks = [25,40,30,35,25,20,50,48]
marks_perc = []
for x in student_marks:
    res= (x/50)*100
    marks_perc.append(res)
print(marks_perc)
def mark_bar_chart():
    plt.bar(student_names,student_marks)
    plt.title("Student Marks Bar Chart")
    plt.xlabel(student_names)
    plt.ylabel(student_marks)
    plt.show()

mark_bar_chart()