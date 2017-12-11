#!/usr/bin/env python3

import numpy as np
from numpy import pi

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Slider, TextInput
from bokeh.plotting import figure

# from bokeh.client import push_session
# from bokeh.driving import cosine
# from bokeh.plotting import figure, curdoc

N = 200
x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)
source = ColumnDataSource(data=dict(x=x, y=y))

plot = figure(plot_height=400, plot_width=400, title="my sine wave",
              tools="crosshair,pan,reset,save,wheel_zoom",
              x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

text = TextInput(title="title", value="my sine wave")
offset = Slider(title="offset", value=0.0, start=-5.0, end=5.0, step=0.1)
amplitude = Slider(title="amplitude", value=1.0, start=-5.0, end=5.0, step=0.1)
phase = Slider(title="phase", value=0.0, start=0.0, end=2*np.pi)
freq = Slider(title="frequency", value=1.0, start=0.1, end=5.1, step=0.1)


def update_title(attrname, old, new):
    plot.title.text = text.value

text.on_change('value', update_title)

def update_data(attrname, old, new):

    a = amplitude.value
    b = offset.value
    w = phase.value
    k = freq.value

    x = np.linspace(0, 4*np.pi, N)
    y = a * np.sin(k*x + w) + b

    source.data = dict(x=x, y=y)


for w in [offset, amplitude, phase, freq]:
    w.on_change('value', update_data)


inputs = widgetbox(text, offset, amplitude, phase, freq)

curdoc().add_root(row(inputs, plot, width=800))
curdoc().title = "Sliders"

session.show

#x = np.linspace(0, 4*pi, 80)
#y = np.sin(x)

#p = figure()
#r1 = p.line([0, 4*pi], [-1, 1], color="firebrick")
#r2 = p.line(x, y, color="navy", line_width=4)

#session = push_session(curdoc())

#@cosine(w=0.03)
#def update(step):
    
#    r2.data_source.data["y"] = y * step
#    r2.glyph.line_alpha = 1 - 0.8 * abs(step)

#curdoc().add_periodic_callback(update, 50)
#session.show(p)
#session.loop_until_closed()



