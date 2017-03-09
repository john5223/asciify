from PIL import Image
import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))


'''
TODO: implement celery for CPU tasks
'''

def image_to_ascii(img, max_height=None, scale=None, factor=None):

    img = Image.open(img)

    if max_height and not isinstance(max_height, float):
        max_height = float(max_height)
    if scale and not isinstance(scale, float):
        scale = float(scale)
    if factor and not isinstance(factor, float):
        factor = float(factor)

    width, height = img.size
    if not scale and not max_height:
        max_height = 50

    SC = scale or .5
    GCF = factor or 1
    WCF = (7/4)
    if max_height and height > float(max_height):
        SC = 1 / (height / float(max_height))

    S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
    img = np.sum( np.asarray( img.resize(S) ), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)

    ascii_art = "\n".join( ("".join(r) for r in chars[img.astype(int)]) )
    return ascii_art




if __name__ == '__main__':
    f = 'tests/earth.png'
    f = 'tests/map.jpg'
    art = image_to_ascii(img, factor=1.2, max_height=50)
    print( art )
