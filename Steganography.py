from PIL import Image
import numpy as np


def open(path: str) -> Image:
    try:
        return Image.open(path)
    except:
        raise


def encrypt(img: Image, msg: str):
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

    print("HELLO WORLD")
    print(list(img_data).index(0))
    print("HELLO WORLD")

    for p in img_data:
        new_num = bin(p)[2:]  # get rid of the 0b
        new_num = new_num.zfill(2)[-2:]  # save the last two bits
        img_chars.append(new_num)

    img_chars = "".join(img_chars)

    for i in range(0, (len(img_chars)//8)*8, 8):
        img_str += chr(int(img_chars[i:i+8], 2))

    return img_str
