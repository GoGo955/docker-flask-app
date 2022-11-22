# ue_cld_programming
## Overview
Repository prepared for Cloud Programming class (University of Economics in Katowice). It contains simple flask app, that displays parabola plot based on the parameters provided - otherwise, the default plot is displayed.

In current version, all parameters are required to create a customized plot - supplementing them partially will display default plot.  

## Instructions

- to clone repository, run in your destination folder:
```
git clone https://github.com/GoGo955/docker-flask-app.git
```
- After cloning - in the location of repository - open PowerShell.
- To build the image, run:
```
docker build -t flask_plot_app:v1.0 . 
```
- Afterwards, run the container with:
```
docker run --rm -it -p 5000:5000 flask_plot_app:v1.0
```
- Check, how the app works on default settings (parameters):
```
http://localhost:5000/plot
```
- To use custom parameters, you should provide all of them. Check how app works with all parameters - you can experiment with adjusting the param values:
```
http://localhost:5000/plot?a=2&b=7&c=3&xmin=-10&xmax=10&ymin=-5&ymax=5
```
- to close, press ctrl+C in console.
- to remove image, type in console:
```
docker image rm flask_plot_app:v1.0 
```

