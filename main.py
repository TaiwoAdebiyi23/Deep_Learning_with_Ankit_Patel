# Getting started
# Simple use of Matplotlib
import numpy as np
import matplotlib.pyplot as plt


def f_objective(x):                                               # define function for xSinx
    return x * np.sin(x)


X_r = np.linspace(-15, 15, 400)  # input values of x-axis
Y_r = f_objective(X_r)           # f(x)

# Plot xSin(x)
plt.style.use('fivethirtyeight')                                 # plotting style
plt.figure(figsize=(10, 6))                                      # set figure dimension
plt.plot(X_r, Y_r, label=r'$y = x \sin(x)$', linewidth=2.0)      # line plot
plt.title(r'Plot of $y = x \sin(x)$')                            # set title
plt.xlabel('x')                                                  # set x label
plt.ylabel('y')  # set y label
plt.show()


#