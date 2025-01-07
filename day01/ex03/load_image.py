from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
	"""Load an image with RGB color and return a np.array

	Args:
		path (str): path of the image

	Returns:
		list: Return a list of RGB values of the Image
	"""
	assert isinstance(path, str), "Arg is not a str"
	with Image.open(path) as im:
		if im.mode != "RGB":
			raise TypeError("Not RGB image")
		array = np.array(im)
		print(f"The shape of image is: {array.shape}")
		print(array)
		return array
