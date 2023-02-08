from PIL import Image
import requests


def get_dominant_color(image_path):
    image = Image.open(image_path)
    image = image.resize((20, 20))
    pixels = image.getdata()
    red, green, blue = 0, 0, 0
    count = 0
    for pixel in pixels:
        red += pixel[0]
        green += pixel[1]
        blue += pixel[2]
        count += 1
    red = int(red / count)
    green = int(green / count)
    blue = int(blue / count)
    return red, green, blue

def set_wled_color(red, green, blue):
    url = "http://WLED_HOST/json/state"
    payload = {"on": True, "bri": 255, "transition":5, "seg":[{"col":[[red,green,blue]]}]}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, json=payload, headers=headers)

if __name__ == '__main__':
    image_path = "/tmp/ambient.png"
    red, green, blue = get_dominant_color(image_path)
    set_wled_color(red, green, blue)
