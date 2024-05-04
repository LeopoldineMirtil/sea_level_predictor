import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file-use file path if getting error
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    #x = Year and the y = CSIRO Adjusted Sea Level
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    #get slope and y-int for 1st line
    m1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level']).slope

    b1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level']).intercept

    #get years 1880-2050
    yr = range(1880, 2051) 

    #plot 1st line of best fit
    plt.plot(yr, (m1*yr)+b1, color='r')


    # Create second line of best fit
    #filter df for 2000-2013 
    fil_df = df.loc[(df['Year'] >= 2000) & (df['Year']<=2013)]

    #calc slope and intercept from filtered data for 2nd line
    m2 = linregress(fil_df['Year'], fil_df['CSIRO Adjusted Sea Level']).slope  
    b2 = linregress(fil_df['Year'], fil_df['CSIRO Adjusted Sea Level']).intercept


    #plot 2nd line of best fit: years 2000 - 2050
    yr2 = range(2000, 2051) 
    plt.plot(yr2, (m2*yr2)+b2, color='orange')

    ##get xtick vals to cover req plot range (1850 - 2075)
    x_tx = list(range(1850, 2100, 25)) 
    xt = []
    for n in x_tx:
        xt.append(float(n))
    
    plt.xticks(xt) #set xtick values on plot

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()