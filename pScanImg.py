import Image
#import ImageFilter
def processScanImg(filename):
    ori = Image.open(filename)
    newImg = Image.new(size = ori.size,
                       mode = ori.mode,
                       color=(255, 255, 255))
    #gaussianblur = ImageFilter.GaussianBlur(radius= 1)
    #ori = ori.filter(gaussianblur)
    for x in range(1, ori.size[0]-1):
        for y in range(1,ori.size[1]-1):
            #pixel = ori.getpixel((x,y))
            #if(isBlack(pixel)) or isSurBlack((x,y), ori)):
            #if(isSurBlack((x,y), ori)):
            if(isBlack(ori.getpixel((x,y)))):
                newImg.putpixel((x,y), (0,0,0))
    return newImg

def isBlack(pixel):
    return pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100 and pixel[2] - pixel[0] < 50

def isSurBlack(xy, img):
    for x in range(-1,1):
        for y in range(-1,1):
            pixel = img.getpixel((xy[0]+x, xy[1]+y))
            if(isBlack(pixel)):
                return True
    return False


if __name__ == "__main__":
    filename = '/home/gary_li/Dropbox/Documents/Notes/DataStreamClustering/tt.jpg'
    newImg =  processScanImg(filename)
    newImg.show()

