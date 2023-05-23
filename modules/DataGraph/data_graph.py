#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


class DataGraph():
    def __init__(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1)
        self.left_bound = None
        self.right_bound = None
        self.down_bound = None
        self.up_bound = None
        self.first = True

        return
    
    def scatter(self, x, y, **kwargs):
        self.ax.scatter(x, y, **kwargs)

        self.__update_bounds(x, y)

        return
    
    def __update_bounds(self, x, y):
        if self.first:
            self.left_bound = x.min() - 1
            self.right_bound = x.max() + 1
            self.down_bound = y.min() - 1
            self.up_bound = y.max() + 1

            self.first = False
        else:
            self.left_bound = min(self.left_bound, x.min() - 1)
            self.right_bound = max(self.right_bound, x.max() + 1)
            self.down_bound = min(self.down_bound, y.min() - 1)
            self.up_bound = max(self.up_bound, y.max() + 1)
        
        return
    
    def __set_range(self, start, stop):
        if start is None:
            if self.left_bound is None:
                assert('WARNING: start point is unknown.')
            start = self.left_bound
        
        if stop is None:
            if self.right_bound is None:
                assert('WARNING: stop point is unknown.')
            stop = self.right_bound
        
        return start, stop
    
    def __linear(self, X, slope, biases):
        Y = np.zeros_like(X)
        for index, x in enumerate(X):
            Y[index] = slope * (x - biases[0]) + biases[1]
        return Y

    def draw_line(self, slope, biases, start=None, stop=None, num=2880, **kwargs):
        start, stop = self.__set_range(start, stop)

        X = np.linspace(start=start, stop=stop, num=num)
        Y = self.__linear(X, slope, biases)

        self.ax.plot(X, Y, **kwargs)

        return X, Y

    def divide_into_2_regions(self, slope, biases, start=None, stop=None, num=2880, alpha=0.1, **kwargs):
        start, stop = self.__set_range(start, stop)

        X = np.linspace(start=start, stop=stop, num=num)
        Y = self.__linear(X, slope, biases)

        self.ax.fill_between(X, Y, self.down_bound - 1, color='green', alpha=alpha)
        self.ax.fill_between(X, Y, self.up_bound + 1, color='blue', alpha=alpha)

        return X, Y
    
    def xlabel(self, xlabel):
        self.ax.set_xlabel(xlabel)
    
    def ylabel(self, ylabel):
        self.ax.set_ylabel(ylabel)
        
    def show(self):
        plt.xlim(self.left_bound, self.right_bound)
        plt.ylim(self.down_bound, self.up_bound)

        self.ax.set_aspect('equal', adjustable='box')
        self.fig.tight_layout()
        plt.show()

        return

