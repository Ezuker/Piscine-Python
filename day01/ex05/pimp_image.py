from PIL import Image, ImageDraw, ImageFont
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array: list) -> list:
	"""
	Inverts the color of the image received.
	"""
	new_arr = [[255 - array[i][j] for j in range(len(array[0]))] for i in range(len(array))]
	np_array = np.array(new_arr)
	im = Image.fromarray(np_array)
	im.show()
	return np_array
	

def ft_red(array: list) -> list:
	np_array = np.array(array)
	np_array[:, :, 1] = 0
	np_array[:, :, 2] = 0
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array


def ft_green(array: list) -> list:
	np_array = np.array(array)
	np_array[:, :, 0] = 0
	np_array[:, :, 2] = 0
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array


def ft_blue(array: list) -> list:
	np_array = np.array(array)
	np_array[:, :, 0] = 0
	np_array[:, :, 1] = 0
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array


def ft_grey(array: list) -> list:
	"""
	Apply grey filter
	"""
	np_array = np.array(array)
	np_array = np.mean(np_array, axis=2)
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array