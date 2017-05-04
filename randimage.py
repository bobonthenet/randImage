from PIL import Image
import random
import time
def drawImage():
    testImage = Image.new("RGB", (25,25), (255,255,255))
    pixel = testImage.load()
    for x in range(25):
        for y in range(25):
            red = random.randrange(0,255)
            blue = random.randrange(0,255)
            green = random.randrange(0,255)
            pixel[x,y]=(red,blue,green)
    return testImage
def main():
    for x in range(0, 100):
        finalImage = drawImage()
        filename = 'randimage' + str(x) + '.jpg'
        finalImage.save(filename)
if __name__ == "__main__":
    main()
