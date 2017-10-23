import plotly.plotly as py
# (*) Useful Python/Plotly tools
import plotly.tools as tls
# (*) Graph objects to piece together plots
from plotly.graph_objs import *
import numpy as np  # (*) numpy for math functions and arrays
import matplotlib.pyplot as plt
x = np.arange(0, 10)
y = np.sin(np.exp(x**2))
plt.plot(x, y)
fig = plt.gcf()

py.iplot_mpl(fig, strip_style=True,
             filename='s6_damped_oscillation-default-style')
