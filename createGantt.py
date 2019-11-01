import pandas as pd
from datetime import date
import matplotlib.dates as mpdt
from ganttFunctions import getColourMap, \
    getPlotDates, getPlotBars, getColourBarMinMax, \
    getPlotColours, getPlotColourBar, getPlotProperties, \
    getYAxisDetails, getDeadlines

def create_gantt(min_date, max_date):
    # Import study details and sort
    df = pd.read_csv('ProjectList.csv')
    df = df.sort_values(by=['sponsor'],ascending=False)

    # Get plotting dates details
    dateStart, dateEnd = getPlotDates(df)

    # Get y axis details (labels and positions)
    ylabels, ypos, ydict = getYAxisDetails(df)

    # Get the blue colour map
    blueCols = getColourMap()

    ## Get colours for plots
    # Find maximum number of samples for colour bar limits
    maxSmps = df['n'].max()
    minSmps = df['n'].min()
    bottomSample, topSample = getColourBarMinMax(minSmps,maxSmps)

    # Find colours for each study based on relative position of colour
    # Depends on version of pandas (0.24.0)
    #sampleN = df.total.to_numpy()
    sampleN = df['n'].values
    plotColours = getPlotColours(blueCols,sampleN,bottomSample,topSample)

    # Get axes and plot gantt bars
    progress = df['perc_complete'].values
    fig, ax, ax2 = getPlotBars(ypos,dateStart,dateEnd,plotColours,progress)

    # Get axes properties - can select a date range
    # ax = getPlotProperties(ax,ydict,minDate="14-Jul-19",maxDate="31-May-20")
    ax = getPlotProperties(ax,ydict,minDate=min_date,maxDate=max_date)

    # Plot today's date
    today_date = date.today()
    today_date = mpdt.date2num(today_date)
    ax.plot([today_date,today_date],[-0.1,3.5],color='r',alpha=1,zorder=-1,linestyle="--",linewidth=0.5)

    # Plot the submission dates
    subDates, subYPos = getDeadlines(df,ydict)

    ax.scatter(subDates, subYPos,zorder=2,color="purple",edgecolor="w",marker="*",s=300,label="Submission Date")
    ax.legend()

    # Get colour bar properties
    cbar = getPlotColourBar(ax2,blueCols,bottomSample,topSample)

    # Title and save figure
    ax.set_title("Clinical Testing Gantt Chart",fontsize=16)
    return fig
