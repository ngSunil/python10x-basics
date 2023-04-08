def add(a,b):
    return a+b
def callback(a,b):
    return add(a,b)
def pas(i,j,fn):
    return fn(i,j)
a = add(1,2)
print(a)
print(callback(2,3))
print(pas(10,20,add))

# LAMBDA FUNCTION
'''equivalent to 
def func(a):
    return a+1
    '''
func = lambda a, b:a+b

print(f'Lambda function: {func(100, 200)}')


# filter
print("FILTER>>>>>>>>>>>>>>>>>")
def even(a):
    return a%2 == 0
numbers = [1,2,3,4,5]
ans = list(filter(even, numbers))
print(ans)
print(list(filter(lambda a: a%2==0, [2,5,7,10])))

# Map
def square(a):
    return a**2
numbers = [1,2,3]
result = list(map(square, numbers))
print(result)
print(list(map(lambda a:a%2==0, range(10))))

# ITERATION
iteration = iter([1,2,3,4])
print(next(iteration))
print(next(iteration))
print('--GENERATOR---')
# GENERATOR
def fn():
    yield 1
    yield 2
    yield 3
    yield 4
values = fn()
print(values.__next__())
print(values.__next__())
for i in values:
    print(i)
print(*values, sep='\n')
print(list(map(lambda a: a**2, range(5))))
# GENERATOR TO PRINT SQUARES
def squares():
    n=1
    while n<=5:
        square = n**2
        yield square
        n+=1
values = squares()
print(*values)