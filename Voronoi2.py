#!/usr/bin/env python
# coding: utf-8

# Essai Github

# In[ ]:


from scipy.spatial import Voronoi

import matplotlib.pyplot as plt

data_points = [[0,0], [1,4], [2,3], [4,1], [1,1], [2,2], [5,3]]

vor = Voronoi(data_points)

from scipy.spatial import voronoi_plot_2d

voronoi_plot_2d(vor)
plt.show()   # plot the figure

