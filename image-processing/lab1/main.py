from PIL import Image
import time, os

def calculate(name, formate):

    start = time.time()
    image = Image.open('data/{}.{}'.format(name, formate))
    end = time.time()
    open_time = end-start

    start = time.time()
    if (formate == 'tif'):
        del image.tag_v2[34377]
        del image.tag_v2[33723]
        del image.tag_v2[700]
        image.save('temp.{}'.format(formate), compression='tiff_lzw')
    else:  
        image.save('temp.{}'.format(formate))
    end = time.time()
    save_time = end-start

    start = time.time()
    raw = image.tobytes()
    end = time.time()
    decode_time = end-start

    size = image.size

    start = time.time()
    image2 = Image.frombytes('RGB', size, raw)
    end = time.time()
    encode_time = end-start

    print ("{}: size = {}, open time = {}, save time = {}, decode time = {}, encode time = {}".format(name, os.stat('data/{}.{}'.format(name, formate)).st_size/1000, open_time, save_time, decode_time, encode_time))
    os.remove('temp.{}'.format(formate))

    def rgb_subtraction(name, formate):
        base_image = Image.open('data/original.bmp')
        target_image = Image.open('data/{}.{}'.format(name, formate))

if __name__ == "__main__":
    calculate('original', 'bmp')
    calculate('jpeg', 'jpg')
    calculate('tif-lzw', 'tif')