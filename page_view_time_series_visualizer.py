import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date')
# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot

    df_new = df.reset_index()
    df_new['date'] = pd.to_datetime(df_new['date'])
    fig = plt.figure(figsize=(10,10))
    plt.plot(df_new["date"],df_new["value"])
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['Months'] = [d.strftime('%B') for d in df_bar.date]
    month_order = []
    for x in range(1,13):
        month_order.append(calendar.month_name[x])

    # Draw bar plot

    fig, axes = plt.subplots(figsize=(10,10))
    sns.barplot(ax=axes, x='year', y='value', hue='Months', hue_order=month_order, data=df_bar).set(xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    month_order = []
    for x in range(1,13):
        month_order.append(calendar.month_abbr[x])

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2, figsize=(18,10))
    sns.boxplot(ax=axes[0], x=df_box['year'], y=df_box['value']).set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    sns.boxplot(ax=axes[1], x='month', y='value', data=df_box, order=month_order).set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

