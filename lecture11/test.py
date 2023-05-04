frequencies=[155, 167, 168, 170, 159, 181]

from plotly.graph_objs import Bar, Layout
from plotly import offline
# Visualize the results.
x_values=list(range(1,6+1))
data=[Bar(x=x_values,y=frequencies)]
x_axis_config={'title': 'result'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='Rolling one D6 1000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
