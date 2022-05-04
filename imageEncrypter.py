import Steganography


def main():
    PATH = "Balloon.jpg"

    original_img = Steganography.open(PATH)
    original_img.show()
    img = Steganography.encrypt(original_img, "Hello else is weird")
    message = Steganography.decrypt(img)  # everything is working right now
    # might want to fit in a automatic word finder not sure yet


if __name__ == "__main__":
    main()
