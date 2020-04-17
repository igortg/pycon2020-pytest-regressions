import numpy as np
import matplotlib.pyplot as plt

def quadratic_bezier(p0, p1, p2, num_points=100):
    t = np.linspace(0, 1, num_points)
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y

if __name__ == '__main__':
    B = quadratic_bezier((1, 1), (0, 0), (1, 0))
    plt.plot(*B)
    x, y = zip((1,1), (0,0), (1,0))
    plt.plot(x, y, 'o')
    plt.xlim((0,1))
    plt.show()
