from itertools import count


numbers = list(map(int,input('Enter the array of nmbers:').split()))
tuple_numbers = []
for i in numbers:
    string = bin(i)
    count = string.count('1')
    tuple_numbers.append((i,count))
tuple_numbers.sort(key = lambda x: x[1], reverse = False)
print(tuple_numbers)