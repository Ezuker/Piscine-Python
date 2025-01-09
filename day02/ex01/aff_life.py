import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def display(csv: pd.DataFrame) -> None:
    """Display the life expectancy via plt

    Args:
        csv (pd.DataFrame): The csv file
    """
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
    """Basic main function
    """
    try:
        csv = load("life_expectancy_years.csv")
        assert isinstance(csv, pd.DataFrame)
    except AssertionError:
        return
    try:
        display(csv)
    except KeyError as e:
        print(f"KeyError Error occured {e}")
    except KeyboardInterrupt as e:
        print(f"Keyboard close the graph {e}")
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    main()
