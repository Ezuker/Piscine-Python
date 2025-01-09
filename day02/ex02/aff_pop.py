import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter
from load_csv import load


def convert(x):
    """Convert string to int
    eg: 24.2M -> 24 200 000

    Args:
        x (string): string to be converted

    Returns:
        int: The result in int format
    """
    tens = {'k': 1e3, 'm': 1e6, 'b': 1e9, 'K': 1e3, 'M': 1e6, 'B': 1e9}
    def f(x): return int(float(x[:-1]) * tens[x[-1]])
    x = f(x)
    return x


def format_func(x, p):
    """
    Convert number to K (thousands) or M (millions) format
    Parameters:
    x (float): Number to format
    p (int): Precision (not used in this implementation)
    Returns:
    str: Formatted string
    """
    if abs(x) >= 1e6:
        return f'{x/1e6:.1f}M'
    elif abs(x) >= 1e3:
        return f'{x/1e3:.1f}K'
    else:
        return f'{x:.0f}'


def display(csv: pd.DataFrame):
    """Function that compare two life expectancy countries

    Args:
        csv (pd.DataFrame): Csv File
    """
    fig, ax = plt.subplots()
    france_data = csv.loc[csv['country'] == 'France']
    saudi_data = csv.loc[csv['country'] == 'Saudi Arabia']

    saudi_data = saudi_data.drop("country", axis="columns")
    france_data = france_data.drop("country", axis="columns")

    saudi_data = saudi_data.T
    france_data = france_data.T

    france_data = france_data.rename(columns={58: "France"})
    saudi_data = saudi_data.rename(columns={151: "Saudi Arabia"})

    france_data = france_data[:251]
    saudi_data = saudi_data[:251]

    france_data = france_data['France'].apply(convert)
    saudi_data = saudi_data['Saudi Arabia'].apply(convert)
    france_data.plot(ax=ax, legend="France")
    saudi_data.plot(ax=ax, legend="Saudi Arabia")
    ax.set_title("Population Projections")
    ax.set_ylabel("Population")
    ax.set_xlabel("Year")
    plt.legend(loc='lower right')
    ax.yaxis.set_major_formatter(FuncFormatter(format_func))
    plt.show()


def main():
    """Basic main function
    """
    try:
        csv = load("population_total.csv")
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
