"""
Program takes number of students, their names and grades and return dictionary where the keys are the names and the values are lists with grades.
-------------------------------------------------------
"""
#Enter the number of members: 2
#Name?:John
#Please enter the grades (separeted by comma):3,4,5
#Name?:MIA
#Please enter the grades (separeted by comma):5,5,5
#{'John': ['3', '4', '5'], 'Mia': ['5', '5', '5']}

n = int(input("Enter the number of members: "))
names = []
grades = []

for item in range(n):
    names.append(input("Name?:").title())
    grades.append(list(input("Please enter the grades (separeted by comma):").split(",")))
    
total = dict(zip(names, grades))
print(total)
