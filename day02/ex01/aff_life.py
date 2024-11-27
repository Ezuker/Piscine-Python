import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def display(csv: pd.DataFrame) -> None:
    fig, ax = plt.subplots()
    france_data = csv.loc[csv['country'] == 'France']
    france_data = france_data.drop("country", axis="columns")
    france_data = france_data.T
    france_data.plot(ax=ax, legend=False)
    ax.set_title("France Life expectancy Projections")
    ax.set_ylabel("Life expectancy")
    ax.set_xlabel("Year")
    plt.show()


def main():
    try:
        csv = load("life_expectancy_years.csv")
    except FileNotFoundError:
        return
    display(csv)


if __name__ == '__main__':
    main()
