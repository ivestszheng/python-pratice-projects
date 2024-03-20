from PIL import Image

"""
  1. 首先，要准备一个字符集
  2. 其次，要将图片转成灰度图，所谓灰度图就是黑白照片，这个过程中还要缩小图片，每张图片缩小的比例都不尽相同，要根据图片的实际情况来决定，这样就得到了一张缩小后的黑白照片
  3. 接下来要做的事情就是把灰度值转成字符，灰度值大于240的，我都转成空字符串，这样看着舒服，其余的，按比例映射到字符集上。
"""

char_set = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. """

im = Image.open("source.png")
im = im.resize((50, 50), Image.Resampling.LANCZOS)
im = im.convert("L")
im.save("t.jpeg")


def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray/((256.0 + 1)/len(char_set)))]


text = ""
for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j,i))
        if isinstance(gray, tuple):
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])
        text += get_char(gray)
    text += '\n'

with open('pic.txt', 'w')as f:
    f.write(text)

f.close()