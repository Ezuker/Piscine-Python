from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
	try:
		im = Image.open(rf"{path}")
		if im.mode != "RGB":
			raise TypeError("Not RGB image")
	except TypeError as e:
		print(f"Image Error: {e}")
		im.close()
		return
	except FileNotFoundError as e:
		print(f"Image Error: {e}")
		return
	array = np.array(im)
	print(f"The shape of image is: {array.shape}")
	print(array)
	im.close()
	return array