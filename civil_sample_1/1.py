import matplotlib.pylab as plt
from numpy import pi, exp, linspace, sin, cos

x = [0.01, 0.1, 1.0]


def _motion(_x, _t):

	return _x*sin(2*pi*_t)-cos(2*pi*_t) + exp(-1*_x/(2*pi))


def motion(_x, _t):

	return 1/(1+_x**2)*_motion(_x, _t)


t = linspace(0, 4, 1000)

plt.plot(t, motion(x[0], t), label='a/w=0.01')
plt.plot(t, motion(x[1], t), label='a/w=0.1')
plt.plot(t, motion(x[2], t), label='a/w=1')

# Add a title
plt.title('Problem 1')

# Add X and y Label
plt.xlabel('t/t_n')
plt.ylabel('u/u_st')

# Add a grid
plt.grid(alpha=.4, linestyle='--')
# Add a Legend
plt.legend()


# save plt
fig = plt.gcf()
fig_size = fig.get_size_inches()
fig.set_size_inches(fig_size[0]*2, fig_size[1]*2)
fig.savefig('Problem-1.jpg', dpi=100)

# Show the plot
plt.show()
