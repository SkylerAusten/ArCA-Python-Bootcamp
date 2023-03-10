
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
from IPython.display import HTML
from plotly.offline import init_notebook_mode, iplot
import scipy
import os

pokemon = pd.read_csv("pokemon.csv")

app = Flask(__name__)
 
@app.route('/')

def hello_world():
    # https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html
    labels = {"hp":"Pokemon HP"}
    hp_histogram = px.histogram(pokemon, x="hp", marginal="rug",
                   hover_data=pokemon.columns, title="Pokemon HP Histogram", labels=labels)
    hp_histogram.update_layout(yaxis_title="Count") 
    return iplot(hp_histogram)
 
if __name__ == '__main__':
    app.run()