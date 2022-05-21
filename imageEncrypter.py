import Steganography
import numpy as np


def main():
    PATH = "Panda.jpg"

    original_img = Steganography.open(PATH)

    original_img.show()

    with open("romeoandjuliet.txt") as str:
        str = "".join(str.readlines()).replace("\n", "")
        img = Steganography.encrypt(original_img, str)

    img.show()

    img_map = Steganography.heat_map(
        original_img, img, Steganography.spectrum([200, 200, 255], [0, 0, 200], 10)
    )
    img_map.save("./heat_map.png")


if __name__ == "__main__":
    main()
