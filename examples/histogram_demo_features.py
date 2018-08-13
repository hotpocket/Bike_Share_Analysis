"""
Demo of the histogram (hist) function with a few features.

In addition to the basic histogram, this demo shows a few optional features:

    * Setting the number of data bins
    * The ``normed`` flag, which normalizes bin heights so that the integral of
      the histogram is 1. The resulting histogram is a probability density.
    * Setting the face color of the bars
    * Setting the opacity (alpha value).

"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


# example data
mu = 100 # mu = mean of distribution
sigma = 15 # sigma = standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

print(len(x))
print(max(x))
print(min(x))

bins = [i for i in range(40, 161, 5)]
# the histogram of the data
n, bins, patches = plt.hist(x, bins, normed=True, facecolor='green', alpha=0.5)
# add a 'best fit' line
print(bins)
y = mlab.normpdf(bins, mu, sigma)
print(y)
plt.plot(bins, y, 'r--')
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

# Tweak spacing to prevent clipping of ylabel (push plot to the left .15 to give more space on the left)
plt.subplots_adjust(left=.15)
plt.show()
