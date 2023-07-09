with open('file1.txt') as num_file:
    num = num_file.readlines()

with open('file2.txt') as num_file2:
    num2 = num_file2.readlines()

result = [int(num) for num in num if num in num2]

print(result)


