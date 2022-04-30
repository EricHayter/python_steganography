import Steganography

def main():
    steg = Steganography.open("C:/Users/hayte/python_steganography/Balloon.jpg")
    pixel_value = Steganography.encrypt(steg, "Hello world")[0]


if __name__ == "__main__":
    main()