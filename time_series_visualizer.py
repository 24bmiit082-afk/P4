import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import stats

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')
df.sort_index(inplace=True)

# Clean data by removing top and bottom 2.5%
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Make a copy of the data
    df_line = df.copy()
    
    # Draw line plot
    ax.plot(df_line.index, df_line['value'], color='#1f77b4', linewidth=1)
    
    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Format the plot
    fig.tight_layout()
    
    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Make a copy of the data
    df_bar = df.copy()
    
    # Add columns for year and month
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    # Group by year and month, calculate mean
    df_bar_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create bar plot
    df_bar_grouped.plot(kind='bar', ax=ax, width=0.8)
    
    # Set title and labels
    ax.set_title('Monthly Average Daily Page Views')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_xticklabels(df_bar_grouped.index, rotation=45)
    
    # Set legend
    month_labels = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
    ax.legend(labels=month_labels, title='Months', bbox_to_anchor=(1.05, 1), loc='upper left
