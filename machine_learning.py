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


# PARTIAL DERIVATIVES
from sympy import *
from sympy.plotting import plot3d
# declare the two functions
x,y = symbols('x y')
# python syntax to declare the function
f = 2*x**3 + 3*x**3
# finding the partial derivatives for both x and y
dx_f = diff(f, x)
dy_f = diff(f, y)
print(dx_f) #prints 6*x**2
print(dy_f) #prints 9*y**2]
# plot the function
plot3d(f)


# limits in partial derivatives using sympy
from sympy import *
# x and step size x
x, s = symbols ('x, s')
# decrare the function
f = x**2
# the slope between the two points with gap s
# substitute into raise-over-run formula
slope_f = (f.subs(x, x+s)-f)/ ((x+s)-x)
# substitute x for 2
slope_2 = slope_f.subs(x, 2)
# calculate the slope at x=2
# infinatelly approach step size __s__ to zero
result = limit(slope_2, s, 0)
print(result) #prints 4


# calculating derivatives in python using limits
from sympy import *
# 'x' and step size 's'
x,s=symbols('x s ')
# declaring the function
f = x**2
# slope between the two points with the gap s
# substitute into raise-over-run formula
slope_f = (f.subs(x, x+s)-f)/((x+s)-x)
# calculate the derivative function
# infinately approach the step size +s+ to 0
result = limit (slope_f,s,0)
print(result) #2*x

# CALCULATING USING CHAIN RULE
from sympy import *
z = (x**2 + 1)**3
dz_dx = diff(z,x)
print(dz_dx)

# calculating derivative of dz/dx with and without the chain rule but still getting the same result
# first function. underscore y to avoid variable crash
from sympy import *
x,y = symbols('x y')
_y = x**2 +1
dy_dx= diff(_y)
# the second function
z=y**3 + 2
dz_dy = diff(z)
# calculating the derivative with and without the chain rule
# substitute y function
dz_dx_chain = (dy_dx*dz_dy).subs(y,_y)
dz_dx_no_chain = diff(z.subs(y,_y))
# proving the chain rule by showing equal results
print(dz_dx_chain) #prints 6*x*(x**2 + 1)**2
print(dz_dx_no_chain) #prints 6*x*(x**2 + 1)**2

# INTERGRALS IN PYTHON
# Intergrals tend to find an area under the curve.
# this can be done in python by first having a function that approximates an intergral by calling this function.

def approximate _integral (a,b,n,f):
    delta_x = (b-a)/n 
    total sum = 0 
    for i in range (1,n+1):
        midpoint = 0.5 * (2 * a delta_x * (2 * i - 1))
        total_sum + = f(midpint)
    return total_sum * delta_x

def my_function (x):
    return x**2 + 1
area = approximate_intergral (a=0, b=1, n=5, f=my_function)
print (area) # prints 1.33

# so if we use 1000 rectangles for the examples above we get 
area = approximate_intergral(a=0, b=1, n=1000, f=my_function)
print (area) # prints an area of 1.333333250000001
# what about if we use a million triangles 
area = approximate_integral(a=0, b=1, n=1_000_000, f=my_function) 
# print (area)  #prints an area of 1.3333333333332733
# we are now getting a dininishing return here
#  so as we increase the number of triangles, the approximations starts to reach its limit at a smaller and smaller decimals

# we can now use sympy which supports rational numbers
from sympy import *
# Declare 'x' to sympy
x = symbols ('x')
# Now just using python syntax to declare a function 
f = x **2 + 1
#  Calculate the intergral of the function  with respect to x
#  for the area between x=0 and 1
area = intergrate (f, (x,0,1))
print (area) #prints 4/3

# The idea of intergrals is that we can pack some small triangles to find an area under a curve. These rectangles get smaller as we approach 
# but then the length of the triangles and also the width cannot get to 0 but closer. This will make them infinately smaller. This will lead us to use of limits

# CALCULATING INTEGRALS USING LIMITS
from sympy inport *
# Declaring variables 
f = x**2 + 1
lower, upper = 0,1
#  calculate the width and each triangle height at index "i"
delta_x = ((upper - lower )/n )
x_i = (lower + delta_x *i )
fx_i = f.subs(x, x_i)

# Iterate all the "n" triangles and sum their areas
n_rectangles = Sum (delta_x * fx_i, (i, n, 1 )).doit()

# Calculate the area by approaching the number of 
# rectangles "n" to infinity
area = limit(n_rectangles, n, oo)
print (area) #prints 4/3























