
import matplotlib.pyplot as plt
import numpy as np


# np.random.seed(19680801)  # seed the random number generator.
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# fig, ax = plt.subplots(figsize=(7.5, 4.5), layout='constrained')
# ax.scatter('a', 'b', c='c', s='d', data=data)
# ax.set_xlabel('entry a')
# ax.set_ylabel('entry b')
# plt.show()

# ------------------------------------------------------------------------
#
x = np.linspace(0, 2, 100)  # Sample data.

plt.figure(figsize=(10, 5.4), layout='constrained')
plt.plot(x, x, label='linear')  # Plot some data on the (implicit) Axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.plot(x, x**4, label='quadro')
plt.plot(x, x**0.5, label='sqr')
plt.plot(x, 2*np.sin(x*4*3.14), label='sin')
plt.plot(x, 2*np.cos(x*4*3.14), label='cos')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# ------------------------------------------------------------------------
#
# mu, sigma = 175, 15
# x = mu + sigma * np.random.randn(10000)
# fig, ax = plt.subplots(figsize=(10, 5.4), layout='constrained')
# # the histogram of the data
# n, bins, patches = ax.hist(x, 50, density=True, facecolor='C0', alpha=0.75)
#
# ax.set_xlabel('Length [mm]')
# ax.set_ylabel('Probability')
# ax.set_title('Lizard lengths\n (not really)')
# ax.text(75, .025, r'$\mu=115,\ \sigma=15$')
# ax.axis([95, 275, 0, 0.03])
# ax.grid(True)
# plt.show()

# ------------------------------------------------------------------------

