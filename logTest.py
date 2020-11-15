import urllib
from PIL import ImageFile

def getsizes(uri):
    # get file size *and* image size (None if not known)
    MIN_SIZE = 980 #pixels, one dimension 
    file = urllib.urlopen(uri)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while 1:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            #check this out
            #internet may be too slow to scrape
            # return p.image.size[0]
            if p.image.size[0] < MIN_SIZE:
                return 'dropped'
            else:
                return 'kept' 

    file.close()
    #logic??  
    # if size[1] < MIN_SIZE:
    #     return 'dropped'
    # else:
    #     return 'kept'
    
    #print( size, None)

print getsizes("https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/217627.jpg")
print getsizes("https://img.buzzfeed.com/buzzfeed-static/static/2019-05/24/15/enhanced/buzzfeed-prod-web-05/original-16432-1558725118-8.png?crop=1237:648;59,25")
print getsizes("https://img.buzzfeed.com/buzzfeed-static/static/2019-05/30/16/campaign_images/buzzfeed-prod-web-06/heres-how-much-prison-time-lori-loughlin-is-actua-2-4686-1559248406-7_dblbig.jpg")
print getsizes("")
print getsizes("")
print getsizes("")

#format return: (size in bytes, dimensions in  pixels)