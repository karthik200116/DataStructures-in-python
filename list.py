from tokenize import Double


#Declaration.
l = list()

#Using map and Lambda function to mmake changes.
num = [10,20,30]
Double_num = list(map(lambda x: 2*x, num))
print(Double_num)

#.join() method on list.
s = ['Hello', ' World!']
string = ''.join(s)
print(string)

#Comphrension of list
nums = list(range(10))
even = [x for x in nums if x%2 == 0]
print(even)
#newlist = [expression for item in iterable if condition == True]
#The condition is like a filter that only accepts the items that valuate to True.

#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]

# Sorting.
l = [1,10,9,5,7]
# Ascending sort.
l.sort()
print(l)
# Descending sort.
l.sort(reverse=True)
print(l)

# Customize sort function.
'''You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first).
'''
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

#Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


