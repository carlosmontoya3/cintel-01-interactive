import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render
import seaborn as sns

# Set title for webpage
ui.page_opts(title="Montoya Histogram and Scatterplot", fillable=True)

# Create sidebar with a slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui. input_slider function is called with 5 arguments:
    # 1. A string id ("number_of_bins") that uniquely identifies this input
    # 2. A string label ("Number of Bins") to be displayed alongside the slider
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initial value of the slider
    ui.input_slider("number_of_bins", "Number of Bins", 0, 100, 20)


@render.plot(alt="A histogram showing random distribution")
def histogram():
    # Set random seed
    np.random.seed(19680801)
    # Generate random data:
    # - np.random.randn generates 'count_of_points' samples from a standard normal distribution.
    # - Each sample is then scaled by 15 (to increase the spread) and shifted by 100 (to center the distribution around 100).
    x = 100 + 15 * np.random.randn(437)
    # Create a histogram of the random data using hist() function
    # - The first argument is the data array.
    # - The second argument specifies the number of bins, dynamically set by the input slider's current value.
    # - The 'density' parameter, when True, normalizes the histogram so that the total area under the histogram equals 1.
    plt.hist(x, input.number_of_bins(), density=True, color='orange')

@render.plot(alt="A scatterplot showing random distribution")
def scatterplot():
    np.random.seed(19680801)
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)
    sns.scatterplot(x=x, y=y, color='blue')
