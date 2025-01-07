from PIL import Image
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array: list) -> list:
	"""Invert the color of the Image received in parameters

	Args:
		array (list): The list of RGB value of the Image

	Returns:
		list: The inverted values of RGB
	"""
	new_arr = [[255 - array[i][j] for j in range(len(array[0]))] for i in range(len(array))]
	np_array = np.array(new_arr)
	im = Image.fromarray(np_array)
	im.show()
	return np_array
	

def ft_red(array: list) -> list:
	"""
	Removes the green and blue channels from an RGB image array, keeping only the red channel.

	Args:
		array (list): A 3D list representing an RGB image (height, width, 3).

	Returns:
		list: A 3D list with only the red channel preserved.
	"""
	np_array = np.array(array)
	np_array[:, :, 1] = 0
	np_array[:, :, 2] = 0
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array


def ft_green(array: list) -> list:
	"""
	Removes the red and blue channels from an RGB image array, keeping only the green channel.

	Args:
		array (list): A 3D list representing an RGB image (height, width, 3).

	Returns:
		list: A 3D list with only the green channel preserved.
	"""
	np_array = np.array(array)
	np_array[:, :, 0] = 0
	np_array[:, :, 2] = 0
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array


def ft_blue(array: list) -> list:
	"""
	Removes the red and green channels from an RGB image array, keeping only the blue channel.

	Args:
		array (list): A 3D list representing an RGB image (height, width, 3).

	Returns:
		list: A 3D list with only the blue channel preserved.
	"""
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

	Args:
		array (list): A 3D list representing an RGB image (height, width, 3).

	Returns:
		list: A 3D list with only the blue channel preserved.
	"""
	np_array = np.array(array)
	np_array = np.mean(np_array, axis=2)
	np_array = np_array.astype(np.uint8)
	im = Image.fromarray(np_array)
	im.show()
	return np_array