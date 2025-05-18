import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='scatter')

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    df_year = df['Year'].sort_values()
    df_year = np.arange(df_year.min(), 2051)
    y_pred1 = slope * df_year + intercept
    ax.plot(df_year, y_pred1, 'r-', label='Best fit (All data)')

    # Create second line of best fit
    dfcopy = df.copy()
    dfcopy = dfcopy[dfcopy['Year'] >= 2000]
    df_year2 = dfcopy['Year'].sort_values()
    df_year2 = np.arange(df_year2.min(), 2051)
    slope2, intercept2, r_value, p_value, std_err = linregress(dfcopy['Year'], dfcopy['CSIRO Adjusted Sea Level'])
    y_pred2 = slope2 * df_year2 + intercept2
    ax.plot(df_year2, y_pred2, 'g--', label='Best fit (2000 onwards)')

    # Add labels and title

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
