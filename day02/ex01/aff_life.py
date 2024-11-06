import matplotlib.pyplot as plt
# import seaborn as sb
from load_csv import load
import pandas as pd

def display(csv : pd.DataFrame) -> None:
	country_data = csv[csv['country'] == 'France'].drop(columns=['country']).T
	country_data.columns = ['Life expectancy']
	country_data['Year'] = country_data.index.astype(int)

	years = country_data['Year']
	life_expectancy = country_data['Life expectancy']

	fig, ax = plt.subplots()
	plt.title("France Life expectancy Projections")
	ax.set_xlabel("Year")
	ax.set_ylabel("Life expectancy")
	ax.step(years, life_expectancy, where='mid')
	plt.show()

def main():
	try:
		csv = load("life_expectancy_years.csv")
	except FileNotFoundError:
		return
	display(csv)


if __name__ == '__main__':
	main()