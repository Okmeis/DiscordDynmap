# author: Okmeis
# date: 18.10.2022
# version 1.0.0
# desc: This file exists to download pictures which are fragments of the minecraft livemap
#       and returns a combined image of your wished map area.

from PIL import Image
import io
import requests
import DiscordDynmapConfig as Config



def downloadArea(url):
    headers = {
        "User-Agent": "DynmapExtractor/1.1.1.1",
    }
    # Send GET request
    response = requests.get(url, headers=headers)
    # Save the image
    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        print(response.status_code)


def prepareURL(x, y):
    url = Config.url + "tiles/" + Config.mapname + "/flat/" + Config.anotherParameter + "/" + str(x) + "_" + str(y) + ".jpg"
    return url


def getSection():
    down = Config.down
    top = Config.top
    left = Config.left
    right = Config.right
    imgList = []
    
    #create Matrix:
    for x in range(0, top-down+1):
        imgList.append([])
        for y in range(0, right-left+1):
            imgList[x].append(0)
    #insert in the right place
    for y in range(left, right+1):
        for x in range(down, top+1):
            img = downloadArea(prepareURL(y, x))
            imgList[top-x][y-left] = img
    
    imgAmountY = len(imgList)
    imgAmountX = len(imgList[0])
    x, y = imgList[0][0].size
    resultImage =  Image.new('RGB',(imgAmountX*x, imgAmountY*y), (250,250,250))
    
    for yPos in range(0,imgAmountY):
        for xPos in range(0,imgAmountX):
            resultImage.paste(imgList[yPos][xPos],(xPos*x,yPos*y))
    
    return resultImage
