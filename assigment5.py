#assigment5
#1
2
5
8
11
14

#2
15
12
9
6
3

#3
4
9
14
19
24
29

#4
for i in range(3, 19, 3):
    print(i)

#5
for i in range(5, 11):
    print(i, 20 - i)


#6
for i in range(1, 7):
    print(i, i**2, i**3)

#7
start, end = map(int, input().split())
total = 0

for i in range(start, end + 1):
    total += i

print(total)


#8
n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print(count)

#9
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 4 == 0:
        total += i

print(total)

#10
n = int(input())
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print(count)

#11
n = int(input())
total = 0

for i in range(1, n + 1):
    if i % 3 != 0:
        total += i

print(total)

#12
n = int(input())
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even, "Odd =", odd)

#13
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i
    print(total)

#14
n = int(input())
product = 1

for i in range(1, n + 1):
    product *= i
    print(product)

#15
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)


#16
n = int(input())
fact = 1

for i in range(1, n + 1):
    fact *= i
    print(i, "! =", fact)

#17
n = int(input())
product = 1

for i in range(2, n + 1, 2):
    product *= i

print(product)

#18
n = int(input())
product = 1

for i in range(1, n + 1, 2):
    product *= i

print(product)

#19
n = int(input())
product = 1

for i in range(n, 0, -2):
    product *= i

print(product)

#20
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i**2

print(total)

#21
n = int(input())
total = 0

for i in range(1, n + 1):
    total += i**3

print(total)

#22
n = int(input())
fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i
    total += fact

print(total)

#23
n = int(input())
count = 0

for i in range(1000): 
    if n > 0:
        count += 1
        n //= 10
    else:
        break

print(count)

#24
n = int(input())
total = 0

for i in range(1000):
    if n > 0:
        total += n % 10
        n //= 10
    else:
        break

print(total)

#25
n = int(input())
product = 1

for i in range(1000):
    if n > 0:
        product *= n % 10
        n //= 10
    else:
        break

print(product)


#26
n = int(input())
count = 0

for i in range(1000):
    if n > 0:
        digit = n % 10
        if digit % 2 == 0:
            count += 1
        n //= 10
    else:
        break

print(count)


#27
n = int(input())
total = 0

for i in range(1000):
    if n > 0:
        digit = n % 10
        if digit % 2 == 0:
            total += digit
        n //= 10
    else:
        break

print(total)

#28
n = int(input())
largest = 0

for i in range(1000):
    if n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n //= 10
    else:
        break

print(largest)


#29
n = int(input())
smallest = 9

for i in range(1000):
    if n > 0:
        digit = n % 10
        if digit < smallest:
            smallest = digit
        n //= 10
    else:
        break

print(smallest)


#30
n = int(input())
rev = 0

for i in range(1000):
    if n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    else:
        break

print(rev)

#31
n = int(input())
original = n
rev = 0

for i in range(1000):
    if n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    else:
        break

if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


#32
n, target = map(int, input().split())
count = 0

for i in range(1000):
    if n > 0:
        if n % 10 == target:
            count += 1
        n //= 10
    else:
        break

print(count)



#33
n = int(input())

for i in range(1000):
    if n >= 10:
        n //= 10
    else:
        break

print(n)
#34
n = int(input())
largest = 0
smallest = 9

for i in range(1000):
    if n > 0:
        digit = n % 10

        if digit > largest:
            largest = digit
        if digit < smallest:
            smallest = digit

        n //= 10
    else:
        break

print(largest - smallest)

#35
n = int(input())
position = 1

for i in range(1000):
    if n > 0:
        print(n % 10, position)
        n //= 10
        position += 1
    else:
        break

#36
n = int(input())
original = n
total = 0

for i in range(3):
    digit = n % 10
    total += digit**3
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
#37
s = input()

for i in range(len(s)):
    print(i, s[i])

#38
s = input()
count = 0

for ch in s:
    count += 1

print(count)
#39
s = input().lower()
vowels = 0
consonants = 0

for ch in s:
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Vowels =", vowels, "Consonants =", consonants)
#40
s = input()
target = input()
count = 0

for ch in s:
    if ch == target:
        count += 1

print(count)

#41
s = input()
target = input()
pos = -1

for i in range(len(s)):
    if s[i] == target and pos == -1:
        pos = i

if pos == -1:
    print("Not Found")
else:
    print(pos)
#42
s = input()
upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase =", upper, "Lowercase =", lower)
#43
s = input()

for ch in s:
    print(ch, ord(ch))
#44
s = input()

for ch in s:
    if ch.lower() not in "aeiou":
        print(ch, end="")
#45
s = input()
print(s[len(s) // 2])

#46
s = input()
mid = len(s) // 2

print("First Half:", s[:mid])
print("Second Half:", s[mid:])
#47
s = input()
n = len(s)
first = ""
second = ""
middle = ""

for i in range(n):
    if i < n // 2:
        first += s[i]
    elif n % 2 == 1 and i == n // 2:
        middle = s[i]
    else:
        second += s[i]

print("First Half:", first)
if n % 2 == 1:
    print("Middle:", middle)
print("Second Half:", second)

#48
s = input()
n = len(s)
same = True

for i in range(n // 2):
    if s[i] != s[i + n // 2]:
        same = False

if same:
    print("Equal Halves")
else:
    print("Different Halves")

#49
s = input()
same = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        same = False

if same:
    print("Symmetric")
else:
    print("Not Symmetric")

#50
s = input()

for i in range(0, len(s), 2):
    print(s[i], end="")

#51
s = input()
even = 0
odd = 0

for i in range(len(s)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Index =", even, "Odd Index =", odd)
#52
s = input()
result = ""

for i in range(0, len(s), 2):
    result += s[i + 1] + s[i]

print(result)

#53
n = int(input())
largest = -1
second = -1

for i in range(1000):
    if n > 0:
        d = n % 10

        if d > largest:
            second = largest
            largest = d
        elif d < largest and d > second:
            second = d

        n //= 10
    else:
        break

print(second)
#54
s = input()
current = 0
best = 0
previous = ""

for ch in s:
    if ch == previous:
        current += 1
    else:
        current = 1

    if current > best:
        best = current

    previous = ch

print(best)
#55
s = input()
target = input()
count = 0

for ch in s:
    if ch == target:
        count += 1

frequency = count / len(s) * 100
print("Count =", count, "Frequency =", round(frequency, 2), "%")
#56
n = int(input())
total = 0

for i in range(1000):
    if n > 0:
        total += n % 10
        print(total)
        n //= 10
    else:
        break
#57
n = int(input())
even = 0
odd = 0

for i in range(1000):
    if n > 0:
        d = n % 10

        if d % 2 == 0:
            even += 1
        else:
            odd += 1

        n //= 10
    else:
        break

if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")
#58
n = int(input())
total = 0
sign = 1

for i in range(1000):
    if n > 0:
        total += sign * (n % 10)
        sign *= -1
        n //= 10
    else:
        break

print(total)
#59
total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)
#60
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count)
#output
5
#61

total = 0

for i in range(1, 6):
    total = total + i

print(total)

#62

n = int(input())
total = 0
highest = 0
lowest = float('inf')

for i in range(n):
    expense = int(input())
    total += expense

    if expense > highest:
        highest = expense
    if expense < lowest:
        lowest = expense

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)

#63

n = int(input())
total = 0
highest = 0
lowest = 100

for i in range(n):
    marks = int(input())
    total += marks

    if marks > highest:
        highest = marks
    if marks < lowest:
        lowest = marks

print("Total:", total)
print("Average:", total / n)
print("Highest:", highest)
print("Lowest:", lowest)

#64

n = int(input())
present = 0
absent = 0

for i in range(n):
    status = input().upper()

    if status == "P":
        present += 1
    elif status == "A":
        absent += 1

percentage = present / n * 100

print("Present:", present)
print("Absent:", absent)
print("Attendance:", round(percentage, 2), "%")

#65

n = int(input())
total = 0
days = 0

for i in range(n):
    units = int(input())
    total += units

    if units > 10:
        days += 1

print("Total Units:", total)
print("Days Above 10:", days)

#66

n = int(input())
total = 0
count = 0

for i in range(n):
    price = int(input())
    total += price

    if price > 1000:
        count += 1

print("Total Bill:", total)
print("Products Above 1000:", count)

#67

n = int(input())
successful = 0
failed = 0

for i in range(n):
    status = input().lower()

    if status == "success":
        successful += 1
    elif status == "failed":
        failed += 1

rate = successful / n * 100

print("Successful:", successful)
print("Failed:", failed)
print("Success Rate:", rate, "%")


#68

n = int(input())
digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0

for i in range(1000):
    if n > 0:
        d = n % 10
        digits += 1
        total += d

        if d > largest:
            largest = d
        if d < smallest:
            smallest = d

        if d % 2 == 0:
            even += 1
        else:
            odd += 1

        n //= 10

print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)

#69

s = input()
total = 0
vowels = 0
consonants = 0
upper = 0
lower = 0
even_index = 0

for i in range(len(s)):
    ch = s[i]
    total += 1

    if i % 2 == 0:
        even_index += 1

    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1

print("Total Characters:", total)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Even Index Characters:", even_index)
