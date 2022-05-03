import Steganography


def main():
    PATH = "Balloon.jpg"

    steg = Steganography.open(PATH)
    img = Steganography.encrypt(steg, "Hello else is weird")
    message = Steganography.decrypt(img)  # everything is working right now
    # might want to fit in a automatic word finder not sure yet


if __name__ == "__main__":
    main()
