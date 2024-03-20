'''
想要完成这个功能，有两个技术点要解决:
- 遍历文件夹及其子文件夹，找出所有的文件目录
- 获取文件的大小
'''
import os

"""
    找出path目录下文件大小大于filesize的文件
    :param path:
    :param filesize:
    :return:
"""
def get_big_file(path,filesize):
    not_find = True
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            target_file = os.path.join(dirpath, filename)
            if not os.path.isfile(target_file):
                continue
            size = os.path.getsize(target_file)
            if size > filesize:
                size = size //(1024*1024)
                size = '{size}M'.format(size=size)
                print(target_file,size)
                not_find = False
    if not_find:
        print('未找到 {} 路径下，大于 {} M 的文件。'.format(path, filesize / 1024 / 1024))

'寻找大于 /Users/ivest 路径下大于 500 M 的文件'
if __name__ == '__main__':
    get_big_file('/Users/ivest', 500*1024*1024)