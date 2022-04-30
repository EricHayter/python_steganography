from PIL import Image
import os


def open(path: str) -> Image:
    try:
        return Image.open(path)
    except:
        raise


def encrypt(img: Image, msg: str):
    img_size = img.size
    rgb_data = list(img.getdata())
    bit_data = []
    bit_msg = []

    msg = msg.encode('ascii')
    for c in msg:
        bit_msg.append(bin(c))

    #print(bit_msg[0])

    for p in rgb_data:
        r_value = bin(p[0])[2:]  # stripping the leading '0b'
        g_value = bin(p[1])[2:]
        b_value = bin(p[2])[2:]
        bit_data.append([r_value, g_value, b_value])

    return bit_data
