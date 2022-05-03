import Steganography

def main():
    steg = Steganography.open("C:/Users/hayte/python_steganography/Balloon.jpg")
    img = Steganography.encrypt(steg, "Hello else is weird")
    print(Steganography.decrypt(img)) # everything is working right now
    # might want to fit in a automatic word finder not sure yet

if __name__ == "__main__":
    main()