import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    # label='orignial'
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color = 'green')

    # Create first line of best fit
    # label ='1880-2050'
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    ser1 = pd.Series([int(i) for i in range(1880,2051)])
    plt.plot(ser1, reg1.slope * ser1 + reg1.intercept, color = 'blue')


    # Create second line of best fit
    # label='recent year'
    ser2 = pd.Series([int(i) for i in range(2000,2051)])
    recent = df[df['Year'] >= 2000]
    
    reg2 = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])

    plt.plot(ser2, reg2.slope * ser2 + reg2.intercept, color='red')

    # Add labels and title
    plt.xlabel('Year')

    plt.ylabel('Sea Level (inches)')
    
    plt.title("Rise in Sea Level")
    # plt.legend(fontsize="medium")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()