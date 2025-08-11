from PIL import Image, ImageOps; import os; import sys;
def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    try:
        with Image.open(sys.argv[1]) as img:
            shirt = Image.open("shirt.png")
            size = shirt.size

            if sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jepg") or sys.argv[1].endswith(".png"):
                imgName1, imgExten1 = os.path.splitext(sys.argv[1])
            else:
                sys.exit("Invalid input")   

            if sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jepg") or sys.argv[2].endswith(".png"):
                imgName2, imgExten2 = os.path.splitext(sys.argv[2])
            else:
                sys.exit("Invalid output")    

            if imgExten1 == imgExten2:
                img = ImageOps.fit(img , size)
                img.paste(shirt, shirt)
                img.save(sys.argv[2])
            else:
                sys.exit("Input and output have different extensions")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    
if __name__ == "__main__":
    main()
