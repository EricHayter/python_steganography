from PIL import Image
import numpy as np

'''
TODO
- create a difference picture to find the differences in picture
- add a shift option to the decryption
- add optional parameters to the encrypt and decrypt functions for shifts
- add functionality to pictures that may not have 8 bit RGB
'''

def spectrum(start_clr:[], end_clr:[], number_of_colors:int):
    start_clr = np.asarray(start_clr)
    end_clr = np.asarray(end_clr)
    clr_diff = (end_clr - start_clr)/(number_of_colors-1)
    return [start_clr+i*clr_diff for i in range(0,number_of_colors)]

def open(path: str) -> Image:
    try:
        return Image.open(path)
    except:
        raise


def encrypt(img: Image, msg: str) -> Image:
    img_data = np.asarray(img)
    img_dim = img_data.shape
    bit_msg = []

    # turning our message into a binary representation
    for c in msg:
        bit_msg.append(bin(ord(c))[2:].zfill(8))

    bit_msg = "".join(bit_msg)

    # spliting the binary string every two bits
    bit_msg = [bit_msg[i:i+2] for i in range(0, len(bit_msg), 2)]

    # flatten for ease of use
    img_data = img_data.flatten()

    for idx, bit in enumerate(bit_msg):
        new_val = int(bin(img_data[idx])[2:-2] + bit, 2)
        img_data[idx] = new_val

    img_data = img_data.reshape(img_dim)

    return Image.fromarray(img_data)

def decrypt(img: Image) -> str:
    img_chars = []
    img_str = ""
    img_data = np.asarray(img)

    img_data = img_data.flatten()

    for p in img_data:
        new_num = bin(p)[2:]  # get rid of the 0b
        new_num = new_num.zfill(2)[-2:]  # save the last two bits
        img_chars.append(new_num)

    img_chars = "".join(img_chars)

    for i in range(0, (len(img_chars)//8)*8, 8):
        img_str += chr(int(img_chars[i:i+8], 2))

    return img_str

def heat_map(img1: Image, img2: Image):
    BLACK_TO_WHITE = spectrum([0,0,0],[255,255,255],10)


    img1_data = np.asarray(img1)
    img2_data = np.asarray(img2)

    # get the dimensions of the image
    IMG_DIM = img2_data.shape

    # find the difference in RGB values
    diff = img1_data - img2_data

    # flattening for ease of use
    diff = diff.reshape(-1,3)


    diff = np.asarray(list(map(lambda p: BLACK_TO_WHITE[sum(p)],diff))).astype('uint8')

    diff = diff.reshape(IMG_DIM)

    return Image.fromarray(diff)

def check_same_image(img1: Image, img2: Image) -> bool:
    if img1 is img2:
        return True
    else:
        return False