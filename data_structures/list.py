print("--------------LIST----------------")
games = ['Cricket', 'Football']
print('k' in games) # find an element in the list
games.append('chess')
games.extend([10, 1001]) # you can add multiple values
print(games.remove(10))
del games[0:2]
games.pop(1)
games.insert(1, 'kabaddi')
# games.clear() empty the list
print(games)
nos = [2,9,0,33]
nos.sort()
nos.reverse()
print(nos)
print(nos.index(33))
print(len(games))

print("--list slicing--")
numbers = list(range(10,100, 10))
print(numbers)
print(numbers[0:3])
print(numbers[:9])
# numbers[n:n+1:interval]
print("---List Comprehension---")
# x = []
# for i in range(11):
#     x.append(i**2)
# print(x)
# using list comprehension one line below
x =[i**2 for i in range(11) if i**2 %2 == 0]
print(x)