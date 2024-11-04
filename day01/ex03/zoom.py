from PIL import Image
import numpy as np
from load_image import ft_load


def ft_zoom(im_array: list) -> None:
	new_im = im_array[100:500, 450:850]
	im = Image.fromarray(new_im)
	im = im.convert('L')
	new_im = np.array(im)
	print(f"The new shape after slicing: {new_im.shape}")
	print(new_im)
	im.show()
	return


if __name__ == '__main__':
	im_array = ft_load("animal.jpeg")
	ft_zoom(im_array)