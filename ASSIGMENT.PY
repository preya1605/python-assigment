#21
name = "Riya"
age = 20
marks = 85.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#22
name = "Riya"
age = 20
marks = 85.5

print("Name:", name)
print("Age:", age)
print("Marks:", marks)

print("Name Type:", type(name))
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#23
age = "18"
marks = 85.5

print("Age:", age)
print("Marks:", marks)
print("Age Type:", type(age))
print("Marks Type:", type(marks))

#24
age = 18
marks = "85.5"

print("Age:", age)
print("Marks:", marks)

print("Age Type:", type(age))
print("Marks Type:", type(marks))

#25
name = "Ravi"
age = 18
marks = 90.5
passed = True

print("Name:", name)
print("Age:", a…
### 18.
What will type() identify for the following?

python
x = 25
print(type(x))

answer:<class 'int'>
### 19.
What will type() identify for:

python
price = 99.50
print(type(price))

Answer:<class 'float'>
### 20.
What will type() identify for:

python
name = "Python"
print(type(name))

Answer: <class 'str'>

### 21.
What will type() identify for:

python
is_active = True
print(type(is_active))

Answer: <class 'bool'>

### 22.
What will type() identify for:

python
data = None
print(type(data))

Answer: <class 'None'>
##23
# Creating variables of five basic Python types

student_name = "Diya"       # String
student_age = 15            # Integer
student_height = 5.4        # Float
is_active = True             # Boolean
student_data = [1, 2, 3]    # List

print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(is_active))
print(type(student_data))

#D. Practicle Problems
##24
student_name = "Diya"
student_age = 15
student_height = 5.4
is_student = True
student_result = None

# Identifying the type of each variable
print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(is_student))
print(type(student_result))

##25
a=50
b=50.0
c="50"
print(type(a))
print(type(b))
print(type(c))

##26
a=True
b="True"
print(t…
3.1_data_types_practice_problems.md
2.1_variables_practice_problems.md
### 18.
What values will the following variables refer to?

python
name = "Rahul"
age = 18
city = "Patna"


Write your answer in this form:

text
Answer: name = "Rahul"  -> value is Rahul
age = 18  -> value is 18
city = "Patna" -> value is Patna

### 19.
What is the final value of `age`?

python
age = 18
age = 19


Explain why.
Answer:The final value of age is 19.
Python runs the code from top to bottom:
age = 18 → age is set to 18.
age = 19 → the previous value is replaced with 19.

### 20.
What is the final value of `name`?

python
name = "Rahul"
name = "Amit"
name = "Riya"

Answer: the final value of name is Riya.
### 21.
Explain what happens in this program:

python
student_name = "Rahul"
student_age = 18

student_age = 19

Answer:student_name = "Rahul"
…
##24.
student_name="Diya Yadav"
student_age=17
student_citys="Kalol"
##25.
student_name = "Rahul"
student_roll_number = 101
student_branch = "Computer Science"
#These use Python's recommended snake_case naming convention, where words are separated by underscores.
##26.
marks = 75
print("Before reassignment:", marks)
marks = 90
print("After reassignment:", marks)
#Explanation:
#At first, marks has the value 75.
#Then marks = 90 reassigns the variable, replacing 75 with 90.
#So the final value of marks is 90.
##27.
name, age, city = "Rahul", 18, "Patna"
##28.
x = y = z = 0
##29.
student_name = "Rahul"
student_full_name = "Rahul"
student_class = "B.Tech"
##30.
# This program stores a student's information and updates their age.
student_name = "Rahul"
student_ag…
1.1_introduction_to_python_practice_problems.md
21.
Identify the comment in the following code:

# Display a message
print("Hello")
Answer: #Display a message is a comment.It explains what the next line of code does.

22.
What is the purpose of the following comment?

# Store the student's name
student_name = "Rahul"
Answer:it explains that the next line stores the student's name in the student_name variable.

23.
Which of the following names is easier to understand for storing a student's name?

x
student_name
a
Answer:It is easier to understand because it clearly tells us that the variable stores a student's name.a does not describe what the data represents.

Explain your answer.

24.
Identify which names are written in snake_case:

student_name
StudentNam…