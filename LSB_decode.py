from PIL import Image
# 解密程序 位于LSB_decode.py文件 第31行


def get_to_10(message_str):  # 将码转为十进制
    message_2 = int(message_str, 2)
    return message_2


def standard(str1):  # 标准化统一为8位二进制数
    return str1.zfill(8)


def get_to_2(message_str):  # 将码转为二进制
    message_20b = str(bin(message_str))
    message_2 = standard(message_20b.replace('0b', ''))  # 去掉二进制开头0b
    return message_2


def cut_txt(txt, num, labels=None):
    if labels is None:
        labels = []
    if len(txt) > num:
        labels.append(txt[:num])
        return cut_txt(txt[num:], num, labels)
    else:
        labels.append(txt)
        return labels


def encode_num(rgb_imge, count):  # 将加密信息插入图片的RGB数据中
    """解密程序"""
    key_temp = ''
    length = 0
    score = 0
    for i in range(rgb_imge.size[0]):  # 获取图片每个像素的RGB值
        for j in range(rgb_imge.size[1]):  # 获取水印的每个像素值
            rgb = rgb_imge.getpixel((i, j))
            if length == count or score == 1:
                break
            for b in range(0, 3):
                if length == count:
                    score = 1
                    break
                temp = str(bin(rgb[b]))
                length = length + 1
                key_temp += temp[-1]
    for s in cut_txt(key_temp,8):
        f = open('decoded_test.txt', 'a')
        f.write(chr(get_to_10(s)))
        f.close()


key = input("key:")
key_1 = int(key)
img = Image.open('encoded_image.png')  # 打开图片文件
rgb_img = img.convert('RGB')  # 转换文件为RGB格式
encode_num(rgb_img, key_1)
