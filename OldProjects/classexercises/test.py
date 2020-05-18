from PIL import Image

im = Image.open("basket.jpeg")
im2 = Image.new("RGB",(im.width, im.height))
print (im.width, im.height)


for e in range(im.width):
    for h in range(im.height):
        u = im.getpixel((e,h))
        if(u[0] == 255 ):
            im2.putpixel((e,h),(255, 0, 0))
            print(str(e) + ' ' + str(h))
            print ('orange')
        else:
            im2.putpixel((e,h), im.getpixel((e,h)))
            continue

im2.save('marked2.jpg')
#print(im.getpixel((20, 40)))
