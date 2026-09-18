#Topic-1 — Comparison Operators
#1
a = 15
b = 20

print(a < b)   #True
print(a > b)   #False
print(a == b)  #False
print(a != b)  #True
print(a <= b)  #True
print(a >= b)  #False

#2
x = 10
y = 10

print(x == y)  #True
print(x != y)  #False
print(x < y)   #False
print(x <= y)  #True
print(x >= y)  #True

#3
a = 10
b = 5

print(a + b == 15)  #True
print(a * b > 40)   #True
print(a - b != 5)   #False
print(a // b == 2)  #True

#4
print("Python" == "Python")  #True
print("Python" == "python")  #False
print("Hello" != "hello")    #True

#Topic-2 — Assignment Operators
#5
x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x) #10

#6
marks = 50
marks+=10
marks-=5
marks*=2
print(marks)

#Topic-3 — Membership Operators with Strings
#7
text = "Python Programming"
print("Python" in text) #True
print("Java" in text)   #False
print("Python" not in text) #False

#8
word = "computer"
print("p" in word)
print("x" in word)
print("c" not in word)

#9
text = "Python"

print("P" in text)  #True
print("p" in text)  #False
print("Python" in text)  #True
print("python" in text)  #False
#Python is case-sensitive, meaning uppercase and lowercase letters are treated as different.

#10
text = input("Enter a word or sentence: ")

print("a" in text)

#11
email = input("Enter your email: ")
print("@" in email)

#12
print(ord("A"))
print(ord("a"))
print(ord("Z"))
print(ord("z"))
print(ord("0"))
print(ord("9"))
print(ord("@"))

#13
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(48))
print(chr(57))
print(chr(64))

#14
print(ord("A"))
print(ord("a"))
print(ord("B"))
print(ord("b"))
#Which is larger: ord("A") or ord("a")?
ord("a") > ord("A")
#What is the difference between them?
97 - 65 = 32
#Is the difference the same for B and b?
98 - 66 = 32

#15
char = input("Enter a character: ")
print(ord(char))

#16
char = input("Enter an uppercase letter: ")
next_char = chr(ord(char) + 1)
print(next_char)

#17
print("A" < "B")
print("a" < "b")
print("A" < "a")
print("0" < "9")

#18
print(chr(9731))
print(chr(9829))
print(chr(8377))
print(ord(chr(9731)))
print(ord(chr(9829)))
print(ord(chr(8377)))

#19
text = "PYTHON"
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])

#20
text = "COMPUTER"
print(text[0])
print(text[3])
print(text[-1])
print(text[-3])

#21
text = "PYTHON"

print(text[0]) #P
print(text[2]) #T
print(text[-1]) #N
print(text[-2]) #O

#22
word = input("Enter a word: ")
print(word[0])
print(word[-1])

#23
word = "PROGRAM"
word[0] #P
word[2] #O
word[-1] #M
word[-4] #G

#24
text = "PYTHON"
print(text[0:3]) #PYT
print(text[2:5]) #THO
print(text[1:6]) #YTHON

#25
text = "PROGRAMMING"
print(text[:4]) #PROG
print(text[4:]) #RAMMING
print(text[:])  #PROGRAMMING

#26
text = "COMPUTER"
print(text[-5:]) #PUTER
print(text[:-3]) #COMPU
print(text[-6:-2]) #MPUT

#27
text = "PYTHON"
print(text[::2]) #PTO
print(text[1::2]) #YHN
print(text[::-1]) #NOHTYP

#28
text = input("Enter a string: ")
print(text[::-1])

#29
text = input("Enter a string: ")
print(text[::2])

#30
text = input("Enter a string: ")
print(text[:3])
print(text[-3:])

#31
text = "ABCDEFGHIJ"
print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])

#32
text = "BTECH-CSE-2026"
print(text[:5])
print(text[6:9])
print(text[10:])

#33
text = "Python is easy"
print(text.split())
#.split() separates a string using whitespace by default.

#34
data = "apple,banana,mango"
print(data.split(","))
#split(",") separates the string wherever a comma appears.

#35
text = "Python is easy"
print(text.split(","))
#There is no comma , in the string, so Python does not split it.

#36
name = input("Enter full name: ")

words = name.split()
print(words[0])
print(words[1])
print(words[2])

#37
first_name, last_name = input().split()
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")

#38
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)

#39
name, age, course, city = input().split(",")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")
print(f"City: {city}")

#40
email = input()
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

#41
sentence = input()
words = sentence.split()
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Total words: {len(words)}")

#42
print("Hello\nWorld")

#43
print("Name:\tRahul")
print("Age:\t20")
print("City:\tAhmedabad")

#44
print("C:\\Python\\Programs")

#45
print('It\'s Python')

#46
print("He said \"Hello\"")

#47
print("Python\nProgramming")

#48
print("Student Details\n\nName:\tRahul\nAge:\t20\nCourse:\tB.Tech")

#49
print("2026", "09", "09", sep="-")

#50
print("Hello", end=" ")
print("Python")

#51
print(10, 20, 30, sep="-", end="\n")
print(40, 50, 60, sep="-")

#52
name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
course = input("Enter course: ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course: {course}")

#53
price = float(input())
print(f"{price:.2f}")

#54
age = int(input("Enter age: "))
print("Age after 5 years:", age + 5)

#55
print("It's Python")

#56
text = "Python"
print(text[1:4])

#57
a, b = input().split()
print(a)
print(b)

#58
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)

#59
print("C:\\new\\test")
#Use \\ when you want to print an actual backslash.

#60
name = input()
m1, m2, m3 = input().split()
m1 = int(m1)
m2 = int(m2)
m3 = int(m3)
total = m1 + m2 + m3
average = total / 3
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")

#61
student_id = input()
parts = student_id.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = student_id[-3:]
roll_number = int(roll_number)
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll_number}")

#62
full_name = input()
names = full_name.split()
first_name = names[0]
last_name = names[2]
username = first_name.lower() + "." + last_name.lower()
print(username)

#63
sentence = input()
words = sentence.split()
print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Number of words: {len(words)}")

#64
email = input()
print(f"@ Present: {'@' in email}")
username, domain = email.split("@")
print(f"Username: {username}")
print(f"Domain: {domain}")

#65
char = input()
code = ord(char)
print(f"Character: {char}")
print(f"Code: {code}")
print(f"Previous: {chr(code - 1)}")
print(f"Next: {chr(code + 1)}")

#66
product_name = input()
price = float(input())
quantity = int(input())
discount_percentage = float(input())
subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount
print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")

#67
date = input()
day, month, year = date.split("-")
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(date[-4:])

#68
text = input()
words = text.split()
first_word = words[0]
second_word = words[1]
print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")
print(f"First Word Reversed: {first_word[::-1]}")
print(f"Second Word Reversed: {second_word[::-1]}")

#69
student_code = input()
parts = student_code.split("-")
degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = student_code[-3:]
print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {degree}/{branch}/{roll}")

#70
full_name = input()
names = full_name.split()
first_name = names[0]
last_name = names[-1]
first_upper_part = first_name[:3].upper()
last_lower_part = last_name[1:4].lower()
reversed_name = full_name[::-1]
print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper_part}")
print(f"Last Name (Lower Part): {last_lower_part}")
print(f"Full Name Reversed: {reversed_name}"