import io
from flask import Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Flask
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [8.0, 5.0]
plt.rcParams["figure.autolayout"] = True

app = Flask(__name__)

@app.route('/plot')
def plot_png(
    a: float = 2.0, b: float = 0.0, c: float = 2.0,
    xmin: float = -3.0, xmax: float = 3.0,
    ymin: float = 0.0, ymax: float = 20.0 
):
    user_params = ['a', 'b', 'c', 'xmin', 'xmax', 'ymin', 'ymax'] 
    if all(param in request.args for param in user_params):
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        c = float(request.args.get('c'))
        xmin = float(request.args.get('xmin'))
        xmax = float(request.args.get('xmax'))
        ymin = float(request.args.get('ymin'))
        ymax = float(request.args.get('ymax'))
        
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    # plot function
    x = np.linspace(xmin,xmax)
    y = a*x**2 + b*x + c
    axis.plot(x,y)
    axis.axhline(y=0, color='black', linestyle='-')
    axis.axvline(x=0, color='black', linestyle='-')
    axis.set_ylim(ymin, 1.05 * ymax)
   
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
