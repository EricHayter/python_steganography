import Steganography

def main():
    steg = Steganography.open("C:/Users/hayte/python_steganography/Balloon.jpg")
    img = Steganography.encrypt(steg, "Something else is weird")
    print(Steganography.decrypt(img))

if __name__ == "__main__":
    main()