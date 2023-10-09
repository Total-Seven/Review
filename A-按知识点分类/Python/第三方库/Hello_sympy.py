from sympy import Symbol, Derivative
from sympy.plotting import plot

x = Symbol('x')
y = x*x + 2*x + 3
d = Derivative(y, x)
print(d.doit())

d.doit().subs({x: 10})

plot(y, (x, -10, 10))
