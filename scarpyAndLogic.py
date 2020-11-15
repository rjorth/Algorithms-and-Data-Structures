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
            return p.image.size
        else:
            'pass' 

    file.close()
    #logic??  
    # if size[1] < MIN_SIZE:
    #     return 'dropped'
    # else:
    #     return 'kept'
    
    #print( size, None)

print getsizes("https://media.allure.com/photos/5bb50d1dcc060a2d2fb93644/1:1/w_500%2Cc_limit/EL-Estee%2520Lauder%2520Power%2520Pack.jpg")
print getsizes("https://media.allure.com/photos/5bb68095cd42342856353ca0/16:9/w_400%2Cc_limit/Lede-Wunder%2520and%2520GHD.jpg")
print getsizes("https://media.allure.com/photos/5b76e93a46200866eeffd8bd/16:9/w_1280%2Cc_limit/allure-skin-care-glossary.jpg")
print getsizes("https://media.allure.com/photos/5c2f8f164325fe2d62c09442/16:9/w_1280,c_limit/Mario%2520Badescu%2520social.png")
print getsizes( "https://media.allure.com/photos/5c2f8ee42f6b312cc3de012d/16:9/w_1280%2Cc_limit/Mario%252520Badescu%252520lead.png")

#format return: (size in bytes, dimensions in  pixels)
