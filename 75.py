from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])
 
show(f)