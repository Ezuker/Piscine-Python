from PIL import Image
import numpy as np


def ft_load(path: str) -> Image:
	try:
		im = Image.open(rf"{path}")
		if im.mode != "RGB":
			raise TypeError("Not RGB image")
	except TypeError as e:
		print(f"Image Error: {e}")
		return
	except FileNotFoundError as e:
		print(f"Image Error: {e}")
		return
	array = np.array(im)
	print(f"The shape of image is: {array.shape}")
	print(array)
	return array

def main():
	ft_load("./animwaal.jpeg")


if __name__ == '__main__':
	main()