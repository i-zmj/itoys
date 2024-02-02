import os
import chardet
import codecs
import sys

folder_path = sys.argv[1]

print("# Folder -->", folder_path)

# 创建转换函数
def convert2utf_bom(path):

    for filename in os.listdir(path):
        
        cur_path = os.path.join(path, filename)

        # 判断是否是文本文件
        if os.path.isfile(cur_path) and (filename.endswith('.cpp') or filename.endswith('.h')):
            # 自动识别文件编码
            with open(cur_path, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
            if encoding == 'UTF-8-SIG':
                print("\033[32m# Skip -->", cur_path, "(", encoding, ")\033[0m")
            else:
                print("\033[31m# Convert -->", cur_path, "(", encoding, " --> UTF-8-SIG)\033[0m")

                # 转换文件编码
                with codecs.open(cur_path, 'r', encoding) as f:
                    content = f.read()
                with codecs.open(cur_path, 'w', 'UTF-8-SIG') as f:
                    f.write(content)
        # 如果是文件夹，递归
        elif os.path.isdir(cur_path):
            convert2utf_bom(cur_path)

convert2utf_bom(folder_path)#

print("# Done!")