import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x_val = df['Year']
    y_val = df['CSIRO Adjusted Sea Level']
    plt.scatter(x_val,y_val)

    # Create first line of best fit
    line_model = linregress(x_val,y_val)
    x_pred1 = pd.Series(range(1880,2051))
    y_pred1 = line_model.intercept + x_pred1*line_model.slope
    plt.plot(x_pred1,y_pred1)

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000,2051))
    y_pred2 = res2.intercept + x_pred2*res2.slope
    plt.plot(x_pred2,y_pred2)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
