import Steganography


def main():
    PATH = "Panda.jpg"


    original_img = Steganography.open(PATH)
    img = Steganography.encrypt(original_img, "Hello world")
    img_map = Steganography.heat_map(original_img,img)
    img_map.show()

if __name__ == "__main__":
    main()
