users = ['Dave','John','Sara']

data = ['Dave', 42, True]

emptylist = []

# print("Dave" in data)
# print(users[0])
# print(users[-3])
# print(users.index('Sara'))
# print(users[0:2])
# print(users[0:])
# print(users[-3:])

users.append('Elsa')
# print(users)

users += ['Jason']
# print(users)

users.extend(['Robert','Jimmy'])
# print(users)
users.insert(0, 'Bob')
# print(users)

users[2:2] = ['Eddie','Alex']
# print(users)

users[1:3] = ['Robert', 'JPJ']
# print(users)

users.remove('Bob')
# print(users)

# print(users.pop())
# print(users)

del users[0]
# print(users)

# del data
data.clear()
# print(data)

users[1:2] = ['dave', 'Adam']
users.sort()
# print(users)

users.sort(key=str.lower)
# print(users)

nums = [4, 42, 78, 1, 5]
# nums.reverse()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# print(sorted(nums, reverse=True))

#Tuples
mytuple = tuple(('Dave',42,True))
anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))