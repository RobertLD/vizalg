from flask import Flask, redirect, url_for, render_template
import plotly
import plotly.graph_objs as go
import plotly.express as px
from random import randint

import pandas as pd
import numpy as np
import json

app = Flask(__name__)

# generate the animated plot for the array values
def create_plot(unsorted):

    # Animation function uses name matching
    # TODO: Use custom algorithm to fill graphable dataframe with values, and them read them using 
    # plotly express.

    figure = px.bar(unsorted, x=range(0,len(unsorted)), y = unsorted, range_y=[0,1100], width = 1000, height = 500)

  
    graphJSON = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

def selectionSort(unsorted):


    return 0


# Generates the landing page
# TODO: Convert index.html to be more of a landing page then a placeholder for
# graphs

#@app.route("/")
#def home():
#    bar = create_plot()
#    return render_template("index.html", content=bar)

@app.route("/selectionsort")
def selsort():
    # generate array of random values to
    array = np.random.randint(1,1000, 1000)
    #for i in range(0,1000):
    #    array[i] = randint(0,1000)
    bar = create_plot(array)
    return render_template("index.html", unsorted = bar)


if __name__ == "__main__":
    app.run(debug=True)
