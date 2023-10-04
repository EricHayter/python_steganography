"""
Encrypts messages within images
"""

from PIL import Image
import numpy as np

def spectrum(start_clr: [], end_clr: [], number_of_colors: int) -> np.array:
    # convert each color to a numpy array
    start_clr = np.asarray(start_clr)
    end_clr = np.asarray(end_clr)

    # finds the scalar value that needs to be added to each color
    clr_diff = (end_clr - start_clr) / (number_of_colors - 1)

    # list comprehension that adds the scalar value to the starting color
    return [start_clr + i * clr_diff for i in range(0, number_of_colors)]


# make this take in a mathematical function to select where the flipped bits should be
# maybe flatten it again so that it is as nxmx3 array with each value containing 
# some value from 0,255 
# max value of changing shouldn't really be forced to be 4 might be too obvious
def encrypt(img: Image.Image, msg: str):
    """
    encrypts a image object given a string as a message to be encrypted
    """
    img_data = np.asarray(img)
    img_dim = img_data.shape
    img_data = img_data.flatten()
    bit_msg = ''.join([bin(ord(ch))[2:] for ch in msg])

    # spliting the binary string every two bits
    bit_msg = [bit_msg[i : i + 2] for i in range(0, len(bit_msg), 2)]

    for idx, bit in enumerate(bit_msg):
        new_val = int(bin(img_data[idx])[2:-2] + bit, 2)
        img_data[idx] = new_val

    img_data = img_data.reshape(img_dim)
    return Image.fromarray(img_data)


# take in the same function as a "key" to decrypt and keep decrypting until you 
# go '\0' sort of like a c-style string
def decrypt(img) -> str:
    """
    docstring
    """
    img_chars = []
    img_str = ""
    img_data = np.asarray(img)

    img_data = img_data.flatten()

    for p in img_data:
        new_num = bin(p)[2:]  # get rid of the 0b
        new_num = new_num.zfill(2)[-2:]  # save the last two bits
        img_chars.append(new_num)

    img_chars = "".join(img_chars)

    for i in range(0, (len(img_chars) // 8) * 8, 8):
        img_str += chr(int(img_chars[i : i + 8], 2))

    return img_str


def heat_map(
    img1: Image.Image,
    img2: Image.Image,
    color_scheme=spectrum([0, 0, 0], [255, 255, 255], 10),
    binary=False,
) -> Image.Image:
    """
    docstring
    """
    # add error-handling if the user gives a dumb gradient

    img1_data = np.asarray(img1).astype(np.float)
    img2_data = np.asarray(img2).astype(np.float)

    # get the dimensions of the image
    img_dim = img2_data.shape

    # find the difference in RGB values
    diff = np.abs(img1_data - img2_data).astype(np.uint8)

    # flattening for ease of use
    diff = diff.reshape(-1, 3)

    if binary:
        diff = np.asarray(
            list(
                map(lambda p: color_scheme[-1] if sum(p) > 0 else color_scheme[0], diff)
            )
        ).astype(np.uint8)
    else:
        diff = np.asarray(list(map(lambda p: color_scheme[sum(p)], diff))).astype(
            np.uint8
        )

    diff = diff.reshape(img_dim)

    return Image.fromarray(diff)
