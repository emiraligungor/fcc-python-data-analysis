import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv", float_precision="legacy")

    # Create scatter plot
    plt.figure(1, figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    bfline1 = linregress(df["Year"], df[df.columns[1]])
    x_bfline1 = np.arange(df["Year"].min(), 2050, 1)
    y_bfline1 = bfline1.intercept + x_bfline1 * bfline1.slope 

    plt.plot(x_bfline1, y_bfline1, color="yellow",label="fit all")

    # Create second line of best fit
    df_start_2000 = df[df["Year"] >= 2000]
    bfline2 = linregress(df_start_2000["Year"], df_start_2000[df.columns[1]])

    x_bfline2 = np.arange(2000, 2050, 1)
    y_bfline2 =  bfline2.intercept + x_bfline2 * bfline2.slope 

    plt.plot(x_bfline2, y_bfline2, color="red",label="fit all")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
