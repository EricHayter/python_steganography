import Steganography

def main():
    steg = Steganography.open("C:/Users/hayte/python_steganography/Balloon.jpg")
    pixel_value = Steganography.encrypt(steg, "Hello world")[8064]
    print(pixel_value)


if __name__ == "__main__":
    main()