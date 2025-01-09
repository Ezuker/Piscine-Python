from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


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
        return f'{x/1e6:.1f}m'
    elif abs(x) >= 1e3:
        return f'{x/1e3:.1f}k'
    else:
        return f'{x:.0f}'


def show_graph(income: pd.DataFrame, life: pd.DataFrame):
    """Show the graph between two pd.DataFrame

    Args:
        income (pd.DataFrame): income data
        life (pd.DataFrame): life expectancy data
    """
    fig, ax = plt.subplots()
    income = income["1900"]
    life = life["1900"]

    income = income.T
    life = life.T

    print(income)
    print(life)
    ax.scatter(x=income, y=life)
    ax.set_title("1900")
    ax.set_ylabel("Life Expectancy")
    ax.set_xlabel("Gross domestic product")
    plt.xscale('log')
    ax.xaxis.set_major_formatter(FuncFormatter(format_func))
    plt.show()


def main():
    """Basic main function
    """
    try:
        income_data = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_data = load("life_expectancy_years.csv")
        assert isinstance(income_data, pd.DataFrame)
        assert isinstance(life_data, pd.DataFrame)
    except AssertionError:
        return
    try:
        show_graph(income_data, life_data)
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
