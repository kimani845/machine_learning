# order of operation(PEDMAS)
# Paranthesis, Exponents, Multiplication, Addition, Subtraction
# Please Excuse My Dear Aunt Samantha
my_value = 2* (3 + 2 )**2/5-4
print(my_value) # Prints 6.0

# Variables
# Variables are named placeholders for unspecified numbers
x = int(input("Please Enter a number:\n"))
product = 3 * x
print(product) #Prints please enter a number


# FUNCTIONS
# these are expressions that define the relationships between two or more variables
# declaring a function in python
def f(x):
    return 2* x + 1
x_values = [0,1,2,3,4]
for x in x_values:
    y = f(x)
print(y)

# charting a linear function in python using sympy. sympy uses matplotlib
from sympy import *
x = symbols('x')
f = 2*x + 1
plot(f)

# charting of an exponential function
from sympy import *
x = symbols('x')
f = x**2 + 1 
plot(f) # prints a smooth symetrical curve called a parabola

# we can also have a funvtion that have multiple input variables f(x,y) = 2x + 3y
# ploting this kind of a function will result in a three dimensional to produce a plane rather than a line
from sympy import *
from sympy.plotting import plot3d
x, y = symbols('x, y')
f = 2*x + 3*y
plot3d(f)

# SUMMATIONS
# summation is usuallty expressed as sigma adds elements together
summation = sum (2*i for i in range(1,6))
print(summation)

# summation of elements in python
x = [1,2,3,4]
n = len (x)
summation = sum (10 * x [i] for i in range (0,n))
print (summation)

# sympy is usually used to map functions in python
from sympy import *
i,n = symbols('i,n')
# iterate each element i from 1 to n
# then multiply and sum
summation = Sum(2*i,(i,1,n)) # the Sum() operator performs the summation operation in sympy

# specify n as 5
# iterating the number 1 through 5
up_to_5 = summation.subs(n,5) # the subs function here is used to specify n as 5
print(up_to_5.doit()) #30

#  LOGARITHMS
# this is a math function that finds a power for a specific number and base
# in python 
from math import log
# 2 raised to what power gives 8
x = log (8, 2)
print (x) #prints 3.0

# in python 
from sympy import *
x = symbols('x')
expr = x**2 / x**5
print (expr) #prints x**(-3)


# in python
# Compoud interest  in python 
from math import exp
p=100
r=.20
t=2
n=12

a = p*(1 + (r/n))**(n*t)
print(a) #prints 148.69146179463576

# Compoud interest continuously in python using the Euler's number 
from math import exp
p= 100
r = .20
t = 2

a = p * exp (r*t)
print (a) # prints 149.18246976412703

# in python
from math import log
# e raised to what power gives 10
x = log(10)
print(x) #prints 2.302585092994046


# limits in python 
from sympy import *
x = symbols('x')
f = 1/x
result=limit(f,x,oo)
print (result)


# calculating the eulers number using limits in python
from sympy import *
n = symbols ('n')
f = (1+(1/n))**n
result = limit (f,n,oo)
print (result) #E
print(result.evalf()) #2.71828182845905 


# Derivatives 
# A derivative calculator in python
def derivative_x(f, x, step_size):
    m = (f(x+step_size)-f(x))/ ((x+step_size)-x)
    return m

def my_function(x):
    return x**2
slope_at_2 = derivative_x(my_function, 2, .00001)
print(slope_at_2) #prints 4.000010000000827


# calculation of derivatives using sympy in python
from sympy import *
# declare x to sympy
x=symbols('x')
# declaring the function using normal python syntax
f = x**2
# calculate the derivative of the function
dx_f=diff(f)
print(dx_f) #prints 2*x

# the diff() function canbe used to calculate the derivative in python

# derivative calculator
def f(x):
    return x**2
def dx_f (x):
    return 2*x
slope_at_2 = dx_f(2.0)
print(slope_at_2) #prints 4.0

# using sympy to find the slope
from sympy import *
x=symbols('x')
f=x**2
# derivative of the function
dx_f=diff(f)
# using substitution to calculate the slope at x=2
print(dx_f.subs(x,2)) #prints 4