from PIL import Image
import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_zoom(im: Image) -> list:
    """Zoom into the image and show it with matplotlib

    Args:
        im (Image): Image to be zoomed in

    Returns:
        list: Return a list of the RGB (R) format reshaped
    """
    im_array = np.array(im)
    print(im_array.shape)
    im_array = im_array[100:500, 450:850, 0:1]
    im_array = np.squeeze(im_array)
    im = Image.fromarray(im_array)
    new_im = np.array(im)
    print(f"The new shape after slicing: {new_im.shape}")
    print(new_im)
    return new_im


def ft_transpose(im: list) -> None:
    """Transpose the matrice and show the image rotated

    Args:
        im (list): The RGB (R) format list of the image
    """
    new_im = [[im[n][i] for n in range(len(im))] for i in range(len(im[0]))]
    # Same as
    # new_im = [[0 for _ in range(len(im))] for _ in range(len(im[0]))]
    # for i in range(len(im)):
    # 	for j in range(len(im[0])):
    # 		new_im[j][i] = im[i][j]
    plt.imshow(new_im, cmap='gray')
    plt.axis('on')
    plt.show()
    plt.close()


def main():
    """Basic main function
    """
    try:
        im = ft_load("animal.jpeg")
        np_array = ft_zoom(im)
        ft_transpose(np_array)
    except TypeError as e:
        print(f"Image Error: {e}")
        return
    except FileNotFoundError as e:
        print(f"Image Error: {e}")
        return
    except AssertionError as e:
        print(f"Image Error {e}")
        return


if __name__ == '__main__':
    main()
