import urllib
from PIL import ImageFile


def getsizes(uri):
    # get file size *and* image size (None if not known)
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
            return size, p.image.size
            break
    file.close()
    #logic?? 
    return size, None



print getsizes("https://ichef.bbci.co.uk/news/320/cpsprodpb/C4C3/production/_106617305_d38dd71e-05a8-4fb6-9027-8bede8eb01af.jpg")
print getsizes("https://img.bleacherreport.net/img/images/photos/003/818/044/hi-res-8364d715a1abc21f773b583a12688f28_crop_north.jpg?h=53&w=80&q=70&crop_x=center&crop_y=top")
print getsizes("https://img.buzzfeed.com/buzzfeed-static/static/2019-05/30/16/campaign_images/buzzfeed-prod-web-06/heres-how-much-prison-time-lori-loughlin-is-actua-2-4686-1559248406-7_dblbig.jpg")
print getsizes("")
print getsizes("")
print getsizes("")
print getsizes("")




#format return: (size in bytes, dimensions in  pixels)
