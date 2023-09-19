import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    dfx = df['Year']
    dfy = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(dfx, dfy)

    # Create first line of best fit
    line_1 = linregress(dfx, dfy)
    x_1 = pd.Series([i for i in range(dfx.min(), 2051)])
    y_1 = line_1.slope*x_1 + line_1.intercept
    plt.plot(x_1, y_1, 'r')

    # Create second line of best fit
    df2000 = df.loc[df['Year'] >= 2000]
    df20x = df2000['Year']
    df20y = df2000['CSIRO Adjusted Sea Level']

    line_2 = linregress(df20x, df20y)
    x_2 = pd.Series([i for i in range(df20x.min(), 2051)])
    y_2 = line_2.slope*x_2 + line_2.intercept
    plt.plot(x_2, y_2, 'g')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()