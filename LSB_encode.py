from PIL import Image  # 导入PIL库
# 加密程序 位于LSB_encode.py文件 第31行


def turn_into_ASCII():  # 将text文字转为ASCII码并将其分离
    global file
    f = open('encode_test.txt')  # 打开text文件
    strw = ''
    for line in f:
        file = line
    for st in file:
        num = ord(st)
        strw = strw + ' ' + str(num)
    strw = strw.split(" ")  # 分离每个信息的码
    strw.remove('')
    f.close()
    return strw


def standard(str1):  # 标准化统一为8位二进制数
    return str1.zfill(8)


def get_to_2(message_str):  # 将码转为二进制
    message = int(message_str)
    message_20b = str(bin(message))
    message_2 = standard(message_20b.replace('0b', ''))  # 去掉二进制开头0b
    return message_2


def encode_num(rgb_imge, infmessage):  # 将加密信息插入图片的RGB数据中
    """加密程序"""
    global r, b, g
    score = 0
    count = 0
    lenth = len(infmessage)
    for i in range(rgb_imge.size[0]):  # 获取图片每个像素的RGB值
        if score == 1:
            break
        for j in range(rgb_imge.size[1]):  # 获取水印的每个像素值
            rgb = rgb_imge.getpixel((i, j))
            if count == lenth or score == 1:
                score = 1
                break
            for b in range(0, 3):
                temp = rgb[b]
                temp_1 = str(get_to_2(temp))
                t = list(temp_1)
                t[-1] = infmessage[count] # 替换加密值
                temp_1 = ''.join(t)
                temp_2 = int(temp_1, 2) # 得到相应的加密后RGB
                count += 1
                if b == 0:
                    r = temp_2
                    if count == lenth:
                        score = 1
                        break
                if b == 1:
                    g = temp_2
                    if count == lenth:
                        score = 1
                        break
                if b == 2:
                    b = temp_2
                    if count == lenth:
                        score = 1
                        break
            rgb_imge.putpixel((i, j), (r, g, b))
    rgb_imge.save('encoded_image.png')


s = turn_into_ASCII()
inf = ''
for a in range(len(s)):
    inf += get_to_2(s[a])
img = Image.open('encode_image.png')  # 打开图片文件
rgb_img = img.convert('RGB')  # 转换文件为RGB格式
encode_num(rgb_img, inf)
print("key:" + str(int(len(inf))))
