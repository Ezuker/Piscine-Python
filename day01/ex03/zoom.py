from PIL import Image, ImageDraw, ImageFont
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt

def ft_zoom(im: Image) -> None:
	im_array = np.array(im)
	print(im_array.shape)
	im_array = im_array[100:500, 450:850, 0:1]
	im_array = np.squeeze(im_array)
	im = Image.fromarray(im_array)
	new_im = np.array(im)
	print(f"The new shape after slicing: {new_im.shape}")
	print(new_im)
	plt.imshow(new_im, cmap='gray')
	plt.axis('on')
	plt.show()
	return


def main():
	try:
		im = ft_load("animal.jpeg")
		ft_zoom(im)
	except FileNotFoundError:
		return
	except TypeError:
		return
	except Exception:
		return

if __name__ == '__main__':
	main()