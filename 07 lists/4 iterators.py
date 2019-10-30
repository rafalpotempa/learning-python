string = "1234567890"

# myIter = iter(string)
# print(myIter)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# for char in string:
#     print(char)
# for char in iter(string):
#     print(char)

numbers = list(range(0,10,2))
print(numbers)

myIter = iter(numbers)
for number in range(0, len(numbers)):
    nextItem = next(myIter)
    print(nextItem)
