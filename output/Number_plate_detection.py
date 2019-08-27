
from PIL import Image
import requests
import cv2
from io import BytesIO
import json
import pandas as pd
with open('Indian_Number_plates.json', 'r') as f:
    data = f.readlines()

    data = [json.loads(line) for line in data]
#df=pd.DataFrame(data)
#print(df["content"])
i=0
for distro in data:
    i=i+1
    url=distro["content"]
    print(url)

    im = Image.open(requests.get(url, stream=True).raw)
    #im.save(str(i) + ".png")
    #im.show()

    x1=distro["annotation"][0]['points'][0]["x"]
    y1=distro["annotation"][0]['points'][0]["y"]
    x2=distro["annotation"][0]['points'][1]["x"]
    y2=distro["annotation"][0]['points'][1]["y"]
    width=distro["annotation"][0]['imageWidth']
    height=distro["annotation"][0]['imageHeight']
    coords=(x1*width, y1*height, x2*width, y2*height)
    target=im.crop(coords)

    #target.save(str(i)+"cropped.png")
   # im.show()
print(i)
