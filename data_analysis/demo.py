from bokeh.plotting import figure, output_file, show
import numpy as np
import math

x = np.arange(0, math.pi*2, 0.05)
a = 0.5

y = np.sin(x)
for n in range(5):
    if(n > 0):
        y1 = np.sin(n*x)/n
        y += y1

p = figure(title = "sine wave example", x_axis_label = 'x', y_axis_label = 'y')
p.line(x, y, legend = "sine", line_width = 2)
output_file("sine.html")
show(p)