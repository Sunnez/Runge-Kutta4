# -*- coding: utf-8 -*-

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


class firstorder():
    """
    Implementation of the method fourth order Runge Kutta, to obtain the value
    of a differential equation given its initial conditions.

    The function receives equations of the form dy / dt = f(t,y)
    ...

    Attributes
    ----------
    function : def
        function of the differential equation to solve

    Methods
    -------
    solve(ti, yi, done, h):
        Solve the ODE using RK4 and its initial values.

    graph(*args, **kwargs):
        Solution graph of each iteration.

    graphvalues():
        Return (t, y) values of each iteration.

    Example
    -------
        from RungeKutta.RK4 import firstorder

        def f(t, y):
            return 2*t -3*y + 1
        y = firstorder(f)

        To get the solution given the initial condition
        ti = 1
        yi = 5
        done = 1.5
        h = 0.1
        r = y.solve(ti, yi, done, h)
        print("dy/dt =", r)

        To obtain the graph
        y.graph('r--', label = "Function y")
    """

    def __init__(self, function):
        """
        Constructor

        Parameters
        ----------
        function : Function to solve
        """

        self.ts = []
        self.ys = []
        self.f = function

    def solve(self, ti, yi, done, h):
        """
        Solution of the first-order ordinary differential equation

        Parameters
        ----------
        ti : Value of the initial t
        yi : Value of the initial y
        done : Value that you want to evaluate in the equation
        h : Integration step

        Return
        ------
        yi : Value of the equation
        """

        st = np.arange(ti, done, h)

        for _ in st:
            K1 = self.f(ti, yi)
            K2 = self.f(ti + h / 2, yi + K1 * h / 2)
            K3 = self.f(ti + h / 2, yi + K2 * h / 2)
            K4 = self.f(ti + h, yi + K3 * h)

            yi += (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
            self.ys.append(yi)

            ti += h
            self.ts.append(ti)
        return yi

    def graph(self, *args, **kwargs):
        """
        Graph the function with the values obtained from each iteration.
        """

        plt.title("Graph of the function")
        plt.plot(self.ts, self.ys, *args, **kwargs)
        plt.legend()
        plt.grid()
        plt.xlabel("$ t $")
        plt.ylabel("$ y(t) $")
        plt.show()

    # def table(self):
    #     """
    #     Show the obtained table of the values of each iteration.
    #     """
    #     data = []
    #     for i in range(len(self.ts)):
    #         data.append([self.ts[i], self.ys[i]])
    #
    #     color = plt.cm.GnBu(np.linspace(1, len(data)))
    #     colLab = ('t', 'y')
    #     plt.table(cellText=data, cellColours=None,
    #               cellLoc='center', colWidths=None,
    #               rowLabels=None, rowColours=None, rowLoc='center',
    #               colLabels=colLab, colColours=color, colLoc='center',
    #               loc='center', bbox=None)
    #
    #     ax = plt.gca()
    #     ax.xaxis.set_visible(False)
    #     ax.yaxis.set_visible(False)
    #     plt.title("Value table")
    #     plt.show()

    def graphvalues(self):
        """
        Obtain the solution values of each iteration.
        """

        return self.ts, self.ys

    def emptyvalues(self):
        """
        Clear all values of each iteration.
        """

        self.ts = []
        self.ys = []

class secondorder():
    """
    Implementation of the method fourth order Runge Kutta, to obtain the value of a 2nd order differential
    equation, given its initial conditions, obtain its graph.
    The function receives equations converted into a system of equations of the form:
    y = u
    du/dx = v
    dv/dx = y"

    du/dx = f(v)
    dv/dx = g(v, u, t)

    Example
    -------
        from RungeKutta.RK4 import secondorder
        from math import e

        def f(v):
            return v

        def g(v, u, t):
            return 4*v + 6*e**(3*t) - 3*e**(-t)

        rk = secondorder(f, g)
        ► To get the solution given the initial conditions
        ui = 1
        vi = -1
        ti = 0
        h = 0.1
        done = 1.5
        r = rk.solve(ti, ui, vi, done, h)
        print("u =", r[0])
        print("v =", r[1])
        ► To obtain the graph
        rk.graph()
        """

    def __init__(self, function1, function2):
        """
        Constructor

        Parameters
        ----------
        function1 : Function that depends on v (f(v))
        function2 : Function that depends on v, u, t (g(v, u, t))
        """

        self.f = function1
        self.g = function2
        self.ts = []
        self.us = []
        self.vs = []

    def solve(self, ti, ui, vi, done, h):
        """
        Solution of the second-order ordinary differential equation

        Parameters
        ----------
        ti : Value of the initial t
        ui : Value of the initial y
        vi : Value of the initial y'
        done : Values that you want to evaluate in the diff system
        h : Integration step

        Returns
        -------
        ui : Value of u
        vi : Value of v
        """

        st = np.arange(ti, done, h)

        for _ in st:
            K1 = self.f(vi)
            m1 = self.g(vi, ui, ti)

            K2 = self.f(vi + m1 * h / 2)
            m2 = self.g(vi + m1 * h / 2, ui + K1 * h / 2, ti + h / 2)

            K3 = self.f(vi + m2 * h / 2)
            m3 = self.g(vi + m2 * h / 2, ui + K2 * h / 2, ti + h / 2)

            K4 = self.f(vi + m3 * h)
            m4 = self.g(vi + m3 * h, ui + K3 * h, ti + h)

            ui += (h / 6) * (K1 + 2 * K2 + 2 * K3 + K4)
            self.us.append(ui)

            vi += (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
            self.vs.append(vi)

            ti += h
            self.ts.append(ti)
        return ui, vi

    def graph(self, *args, **kwargs):
        """
        Graph the function with the values obtained from each iteration
        """

        plt.title("Graph of functions")
        plt.plot(self.ts, self.us, label="u", *args, **kwargs)
        plt.plot(self.ts, self.vs, label="v", *args, **kwargs)
        plt.legend()
        plt.grid()
        plt.xlabel("$ t $")
        plt.ylabel("$ u:v $")
        plt.show()

if __name__ == "__main__":
    def f(t, y):
        return 2 * t - 3 * y + 1

    rk = firstorder(f)

    t_i = 1
    y_i = 5
    end = 1.5
    sh = 0.1
    r = rk.solve(t_i, y_i, end, sh)
    print("dy/dt =", r)
    rk.graph('r--', label="Function y")

# if __name__ == "__main__":
#     from math import e
#
#     def f(v):
#         return v
#
#     def g(v, u, t):
#         return 4*v + 6*e**(3*t) - 3*e**(-t)
#
#     u_i = 1
#     v_i = -1
#     t_i = 0
#     sh = 0.1
#     end = 1.5
#
#     rk = RK(f, g)
#
#     r = rk.solve(t_i, u_i, v_i, end, sh)
#     print("u =", r[0])
#     print("v =", r[1])
#     rk.graph()
