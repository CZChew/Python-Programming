total = 0
count = 1

while count <= 5:
    num = int(input('Enter a number: '))
    if num % 2 != 0:
        total = total + num
    count = count + 1
print(total)
