from numpy import arange, array, ones, linalg
from pylab import plot, show

# create array of x values
x = arange(0, 9)

# create numpy array
numpy_array = array([x, ones(9)])

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]

# obtain the least squares parameters
linear_least_squares = linalg.lstsq(numpy_array.T, y)[0]

# create regression line
line = linear_least_squares[0]*x+linear_least_squares[1]

# plot the line
plot(x, line, 'r-', x, y, 'o')
show()
