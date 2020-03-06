from numpy	import *
from scipy	import *
from scipy import optimize
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import pylab

def f(x):
	return x
	
def g(x):
	return x**2
	
def p(x):
	return x**3
	
def q(x):
	return x**4	
	
x = arange(-10,10,0.1)
new_position = array( [0.0,0.0,0.0,0.0] )

subplot1 = pylab.subplot(2,2,1)
new_position[0] = 0.15
new_position[1] = 0.6
new_position[2] = 0.3
new_position[3] = 0.3
subplot1.set_position(new_position)
subplot1.set_title('Linear')
pylab.xlabel('x')
pylab.ylabel('f(x)')
pylab.plot(x, f(x))

subplot2 = pylab.subplot(2,2,2)
new_position[0] = 0.65
new_position[1] = 0.6
new_position[2] = 0.3
new_position[3] = 0.3
subplot2.set_position(new_position)
subplot2.set_title('Quadratic')
pylab.xlabel('x')
pylab.ylabel('g(x)')
pylab.plot(x, g(x))

subplot3 = pylab.subplot(2,2,3)
new_position[0] = 0.15
new_position[1] = 0.1
new_position[2] = 0.3
new_position[3] = 0.3
subplot3.set_position(new_position)
subplot3.set_title('Cubic')
pylab.xlabel('x')
pylab.ylabel('p(x)')
pylab.plot(x, p(x))

subplot4 = pylab.subplot(2,2,4)
new_position[0] = 0.65
new_position[1] = 0.1
new_position[2] = 0.3
new_position[3] = 0.3
subplot4.set_position(new_position)
subplot4.set_title('Quartic')
pylab.xlabel('x')
pylab.ylabel('q(x)')
pylab.plot(x, q(x))

fig = file('foo.png', 'wb')
pylab.savefig(fig, format='png')
fig.close()