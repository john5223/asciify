import io
from asciify import tasks

from PIL import Image
from .ascii_results import earth_art
from .ascii_results import map_art


def test_ascii_to_text_map():
    img_file = 'tests/images/map.jpg'
    art = tasks.image_to_ascii(img_file, factor=3, max_height=50)
    print("-----")
    print(art)
    print("-----")
    assert(art == map_art)


def test_ascii_to_text_globe():
    img_file = 'tests/images/earth.png'
    art = tasks.image_to_ascii(img_file, factor=2, max_height=50)
    print("-----")
    print(art)
    print("-----")
    assert(art == earth_art)


def test_bytes_io():
    f = 'tests/images/earth.png'
    image_bytes = open(f, 'rb').read()
    image_byteio = io.BytesIO(image_bytes)
    art = tasks.image_to_ascii(image_byteio, factor=2, max_height=50)

    print("-----")
    print(art)
    print("-----")
    assert art
