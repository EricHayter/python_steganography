import codecs
from PIL import Image
import numpy as np
import os
import io


n = 10

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
        bit_msg.append(bin(ord(c))[2:])

    # TODO have some sort of issue here with encryption it looks like
    print(bit_msg[0])

    bit_msg = "".join(bit_msg)

    # spliting the binary string every two bits
    bit_msg = [bit_msg[i:i+2] for i in range(0, len(bit_msg), 2)]

    print(bit_msg[0:n])

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
        img_chars.append(bin(p)[-2:])
        
    print(img_chars[:n])

    img_chars = "".join(img_chars)
    for i in range(0, len(img_chars), 7):
        print(chr(int(img_chars[i:i+7],2)))
        img_str += chr(int(img_chars[i:i+7],2))
        if i > 70:
            break

    return img_str        



