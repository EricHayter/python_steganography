from PIL import Image
import os
import io


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

    # turning our message into a binary representation
    msg = msg.encode('ascii')
    for c in msg:
        bit_msg.append(bin(c)[2:])

    # TODO check around here if the image can even contain the message
    bit_msg = "".join(bit_msg)
    # spliting the binary string every two bits
    bit_msg = [bit_msg[i:i+2] for i in range(0, len(bit_msg), 2)]

    # could be better performance here since we shouldn't in theory require all of the pixels to be encodedS
    for p in rgb_data:
        r_value = bin(p[0])[2:]  # stripping the leading '0b'
        g_value = bin(p[1])[2:]
        b_value = bin(p[2])[2:]
        bit_data.append([r_value, g_value, b_value])

    for idx, b in enumerate(bit_msg):
        new_color = int(bit_data[idx//3][idx % 3][:-2] + b, 2) # converting the binary to an integer
        bit_data[idx//3][idx % 3] = bytes(new_color) # converting the integer to bytes

    bit_data = "".join(bit_data)
    bit_data = bit_data.encode()
    secret_img = Image.open(io.BytesIO(bit_data))
    secret_img.show()

    return bit_data
