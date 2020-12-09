import matplotlib.pylab as plt
from numpy import pi, linspace, sin, cos, append


def save_plt(plt, filename):
    fig = plt.gcf()
    fig_size = fig.get_size_inches()
    fig.set_size_inches(fig_size[0] * 2, fig_size[1] * 2)
    fig.savefig('{}.png'.format(filename), dpi=100)


def _motion_back(_x, _t):
    return _t/_x - 1/(2*pi)*1/_x*sin(2*pi*_t)


def _motion_front(_x, _t):
    return cos(2*pi*(_t-_x)) + 1/(2*pi)*(1/_x)*sin(2*pi*(_t-_x))-1/(2*pi)*1/_x*sin(2*pi*_t)


def motion(_x):
    _t = linspace(0, 2*_x, 2000)
    y = append(
        _motion_back(_x, _t[:500]), _motion_front(_x, _t[500:])
    )
    return _t, y


x = 2, 12
motion_12 = motion(12)
motion_2 = motion(2)


plt.figure(1)
plt.xlabel('t/T_n')
plt.ylabel('R_d')
plt.title('Problem 2 A')
plt.plot(motion_2[0], motion_2[1])

save_plt(plt, 'Problem_2_A')


plt.figure(2)
plt.xlabel('t/T_n')
plt.ylabel('R_d')
plt.title('Problem 2 B')
plt.plot(motion_12[0], motion_12[1])

save_plt(plt, 'Problem_2_B')