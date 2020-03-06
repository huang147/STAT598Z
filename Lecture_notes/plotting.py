# Please see the excellent tutorial at 
# http://matplotlib.sourceforge.net/users/pyplot_tutorial.html
# Many examples below are from this tutorial 

# Also see 
# http://matplotlib.sourceforge.net/contents.html
# for detailed pylab documentation

# In order to use the plotting facilities of Python we need to first
# load pylab
import matplotlib.pyplot as plt
import numpy as np

# Create an array with numbers from 0 to 9
x=np.arange(10)

# Compute y = x^2 
y=x*x

# Plot x vs y
plt.plot(x, y)

# Note that at this point nothing appears on the screen. You need to use
# plt.show to make the plot appear on the screen
plt.show()

# The idea behind pylab is that you can write a series of commands which
# will affect the current plot and at the end you can show the results
# by using plt.show(). Here is an illustration.

# Plot x vs y
plt.plot(x, y)

# Let us give the plot a title
plt.title("x vs x^2")

# This plot now has a title 
plt.show()

# Now let us see a few other commands which can be used to modify the
# plot

plt.plot(x, y)

# Add a title
plt.title("x vs x^2")

# give the x axis a label
plt.xlabel("x")

# give the y axis a label
plt.ylabel("y=x^2")

# Add a grid to the plot
plt.grid(True)

# Control the x and y limits
plt.xlim(0, 12)
plt.ylim(0, 120)

plt.show()

# Hint for advanced users: If you know LaTeX then pyplot can use LaTeX
# strings for text. They are specified using r"$latex stuff$". For
# example

plt.plot(x, y)

# Add a title
plt.title(r"$x$ vs $x^2$")

# give the x axis a label
plt.xlabel(r"$x$")

# give the y axis a label
plt.ylabel(r"$y=x^2$")

# Add a grid to the plot
plt.grid(True)

plt.show()


# Now let us work on commands which can control the properties of the
# plot itself. For instance, things like color, markers etc. 
# This is done by passing a formatting string to the plt.plot function. 

# This changes the color of the plot to red 
plt.plot(x, y, "r")
plt.show()


# This changes the color to green and the line style to dashed
plt.plot(x, y, "--g")
plt.show()

# This changes the marker to be a circle
plt.plot(x, y, "o")
plt.show()

# You can of course combine format strings
# This plots using black + symbols
plt.plot(x, y, "k+--")
plt.show()

# You can change the linewidth used in plotting 
plt.plot(x, y, linewidth=4)
plt.show()

# Again this can be combined with other formatting options
plt.plot(x, y, "r", linewidth=2)
plt.show()

# For more information about the format strings see 
# http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.plot

# Suppose you want to plot two functions on the same plot. There are two
# options available to you.
yy=x*x*x

# Just give plot a series of x, f(x) values and it will do the plotting
# for you 
plt.plot(x, y, x, yy)
# To make things fancy I can add a legend 
plt.legend((r"$x^2$", r"$x^3$"))
plt.show()

# Alternatively, you can use a series of plt.plot commands
plt.plot(x, y)
plt.plot(x, yy)
plt.show()

# If you want to place more than one plot on the same figure then you
# need this

# First create a figure 
plt.figure(1)

# In that figure create a subplot
# Way to read the arguments is 
# numrows numcolumns subplot number 

# Here we are creating a figure with 1 row and 2 columns 
plt.subplot(121)
plt.plot(x, y)

plt.subplot(122)
plt.plot(x, yy)

plt.show()

# Another example. Now we create a figure with 2 rows and two columns 
plt.figure(1)

plt.subplot(221)
plt.plot(x, y)

plt.subplot(222)
plt.plot(x, yy)

plt.subplot(223)
plt.plot(x, y)

plt.subplot(224)
plt.plot(x, yy)
plt.xlabel(r"$x$")

plt.show()


# Now let us try other plots such as log-log plots, semi-log plots etc. 
plt.loglog(x, y)
plt.show()

plt.semilogx(x, y)
plt.show()

plt.semilogy(x, y)
plt.show()

plt.bar(x, y)
plt.show()

# Please see the documentation for hist box and other plot types

# If you want to save a figure to pdf just use plt.savefig instead of
# plt.show 
plt.bar(x, y)
plt.savefig("temp.pdf")
