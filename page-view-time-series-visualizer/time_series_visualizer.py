import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df =pd.read_csv('fcc-forum-pageviews.csv',index_col='date',parse_dates=True)

# Clean data
df = df[(df['value'].quantile(0.025)<df['value']) & (df['value'].quantile(0.975)>df['value'])]


def draw_line_plot():
    # Draw line plot
    df_copy0 = df.copy()
    fig=plt.figure(figsize=(15, 6), facecolor='white')
    plt.plot(df_copy0['value'], 'r-')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=15)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Page Views', fontsize=15)




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_copy1 = df.copy()
    group = df_copy1.reset_index()
    group["year"] = group["date"].dt.year
    group["month"] = group["date"].dt.month
    group = group.groupby(['year', 'month']).mean(numeric_only=True)
    group = group.reset_index()
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    group['month_name'] = group['month'].apply(lambda x: month_order[x - 1])
    pivot_df = group.pivot(index='year', columns='month_name', values='value')

    pivot_df = pivot_df[month_order]

    # Draw bar plot
    ax = pivot_df.plot(kind="bar", figsize=(10, 8))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    fig = ax.get_figure()




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(25, 12))
    sns.boxplot(ax=axes[0], data=df_box, x='year', y='value', hue='year', palette='Set3', legend=False)
    axes[0].set_xlabel('Year', fontsize=16)
    axes[0].set_ylabel('Page Views', fontsize=16)
    axes[0].set_title('Year-wise Box Plot (Trend)', fontsize=16)
    sns.boxplot(ax=axes[1], data=df_box, x='month', y='value', hue='month', palette='Set3', order=month_order, legend=False)
    axes[1].set_xlabel('Month', fontsize=16)
    axes[1].set_ylabel('Page Views', fontsize=16)
    axes[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=16)




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
