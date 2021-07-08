import os
import sys
import uuid

from PIL import Image, ImageDraw, ImageFont


def gen_image(text):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    font = ImageFont.truetype(os.path.join(BASE_DIR, "font", "JetBrainsMono-Medium.ttf"), 12)
    content_list = text.split("\n")
    count = len(content_list)
    longest_line = max(content_list, key=len, default='')
    # 确定画布的长宽
    width = font.getsize(longest_line)[0] + 20
    max_height = 0
    for i in content_list:
        max_height = max(font.getsize(i)[1], max_height)
    height = max_height * count + 20
    im = Image.new("RGB", (width, height), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    x = 10
    y = 10
    for line in content_list:
        # draw the line on the image
        dr.text((x, y), line, font=font, fill="#000000")
        # update the y position so that we can use it for next line
        y = y + max_height
    file_name = "{}.png".format(str(uuid.uuid4()))
    im.save(os.path.join(BASE_DIR, "image", file_name))
    print(file_name)


if __name__ == '__main__':
    # with open("test.log", 'rb') as f:
    #     content = f.read().decode()
    #     # \t的对齐有问题，替换成空格
    #     content = content.replace("\t", "    ")
    # gen_image(content)
    content = sys.argv[1]
    content = content.replace("\t", "    ")
    gen_image(content)
