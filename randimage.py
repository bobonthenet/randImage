from PIL import Image
import random
from sys import argv

def drawImage(width, height):
    testImage = Image.new("RGB", (width,height), (255,255,255))
    pixel = testImage.load()
    for x in range(width):
        for y in range(height):
            red = random.randrange(0,255)
            blue = random.randrange(0,255)
            green = random.randrange(0,255)
            pixel[x,y]=(red,blue,green)
    return testImage
def main():
    for x in range(0, int(argv[3])):
        finalImage = drawImage(int(argv[1]), int(argv[2]))
        filename = 'randimage' + str(x) + '.jpg'
        finalImage.save(filename)
if __name__ == "__main__":
    main()
