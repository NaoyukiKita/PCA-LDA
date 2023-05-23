#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


class EvalGraph():
    def __init__(self):
        self.fig, self.ax = plt.subplots(nrows=1, ncols=1)

    def draw_curve(self, function, start, stop, num=2880, **kwargs):
        X = np.linspace(start=start, stop=stop, num=num)
        Y = np.zeros_like(X)

        for index, x in enumerate(X):
            Y[index] = function(x, **kwargs)
        
        max_index = np.argmax(Y)
        max_x = X[max_index]
        max_y = Y[max_index]

        self.ax.plot(X, Y)

        self.ax.scatter(max_x, max_y, color='black', marker='x')

        return max_x, max_y
    
    def xlabel(self, xlabel):
        self.ax.set_xlabel(xlabel)
    
    def ylabel(self, ylabel):
        self.ax.set_ylabel(ylabel)
    
    def show(self):
        plt.show()


# In[ ]:


if 'get_ipython' in globals():
    import subprocess
    subprocess.run(['jupyter', 'nbconvert', '--to', 'python', '*.ipynb'])
    print('Saved as eval_graph.py')

