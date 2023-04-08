class counting:
    n=0
    def cnt(self):
       self.n+=1
       return self.n

c = counting()
print(c.cnt()) 
# Constructors and desctructors
class cd:
    def __init__(self):
        print('Constructed')
    def __del__(self):
        print('destructed')

c = cd()

# initialise values
class Car:
    def __init__(self, color, type):
        self.color = color
        self.type = type
    def __del__(self):
        pass
car1 = Car('red', 'swift')
print(car1.color)

# INHERITANCE
class baseClass:
    name = ''
    def __init__(self, z):
        self.name = z
        print (self.name)

a = baseClass(100)

class inheritedClass(baseClass):
    def test(self):
        print(self.name, " well done")
b = inheritedClass('Raju')

# SINGLE LEVEL INHERTANCE
class A:
    def func1(self):
         print('Func 1')

class B(A):
    def func2(self):
        print('Func 1')
objB = B()
objB.func1()
# MULTI LEVEL INHERITANCE
class C(B):
    def func3(self):
        print('C func3 method has been called')
c = C()
c.func3()

# multiple inheritance
class X:
    def x(self):
        print('X')
class Y:
    def y(self):
        print('y')
class multiple(X,Y):
    def z(self):
        print('X, Y inherited') 

# Operator overloading
class vegetables:
    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans

    def __add__(self, other):
        return self.carrot + other.carrot
v1 = vegetables(2,3)
v2 = vegetables(5,6)
print(v1+v2)

# DATA HIDING
class p:
    def __init__(self):
        self.value = 1
    def __display(self):
        print(self.value)
q = p()
# q.__display() wont work as display is hidden
print(dir(q)) # read all the methods
q._p__display()
