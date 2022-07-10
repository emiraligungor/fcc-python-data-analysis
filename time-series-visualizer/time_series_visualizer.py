import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean data
df = df[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(20, 6))
    ax = plt.plot(df.index, df['value'])

    # Adding the title
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    # Adding the labels
    plt.ylabel("Page Views")
    plt.xlabel("Date")

    # Save image and return fig (don't change this part)
    plt.savefig("line_plot.png")
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    # Draw bar plot
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    df_bar["Year"] = pd.DatetimeIndex(df_bar.index).year
    df_bar["Month"] = pd.DatetimeIndex(df_bar.index).month

    df_bar = df_bar.groupby(["Year", "Month"])["value"].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(15, 10)).figure

    plt.title("")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    lg = plt.legend(title="Months", fontsize=15, labels=months)
    title = lg.get_title()
    title.set_fontsize(17)

    # Save image and return fig (don't change this part)
    plt.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = [d.year for d in df_box.date]
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))
    # 1
    sns.boxplot(x="year", y="value", data=df_box, palette="tab10", ax=ax[0]).set(
        title="Year-wise Box Plot (Trend)", xlabel="Year", ylabel="Page Views"
    )

    # 2
    sns.boxplot(
        x="month",
        y="value",
        data=df_box,
        order=[
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ],
        palette="tab10",
        ax=ax[1],
    ).set(
        title="Month-wise Box Plot (Seasonality)", xlabel="Month", ylabel="Page Views"
    )

    fig.show()

    # Save image and return fig (don't change this part)
    fig.savefig("box_plot.png")
    return fig
