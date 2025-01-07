import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Reshape a list

    Args:
        family (list): list to reshape
        start (int): start of reshaping
        end (int): end of reshaped

    Returns:
        list: The reshaped list
    """
    try:
        np_array = np.array(family)
        print(f"My shape is {np_array.shape}")
        np_array = np_array[start:end]
        print(f"My new shape is {np_array.shape}")
    except IndexError as e:
        print(f"Index Error {e}")
        return []
    return np_array.tolist()
