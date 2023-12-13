#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 如果当前运行环境是python2，则退出。
import sys
if sys.version_info.major != 3:
    print('\033[91m[ERROR] This script is for python3 only.\033[0m')
    exit(0)

# 如果当前系统不是Linux，则退出。
import platform
if platform.system() != 'Linux':
    print('\033[91m[ERROR] This script is for debian only.\033[0m')
    exit(0)

# 如果没有sudo权限，则申请sudo权限。
import os
if os.getuid() != 0:
    os.system('sudo ' + ' '.join(sys.argv))
    exit(0)

print("======== 欢迎使用izmj/itoys替换apt源脚本 ========")

# 如果没有source.list文件，则退出。
if not os.path.exists('/etc/apt/sources.list'):
    print('\033[91m[ERROR] 文件[/etc/apt/sources.list]未找到！\033[0m')
    exit(0)

# 如果没有备份，则备份。
if not os.path.exists('/etc/apt/sources.list.izmj.bak'):
    print('>>> 备份[/etc/apt/sources.list] --> [/etc/apt/sources.list.izmj.bak]')
    os.system('cp /etc/apt/sources.list /etc/apt/sources.list.izmj.bak')
else:
    print('>>> 文件[/etc/apt/sources.list.izmj.bak]已经存在，跳过备份。')
    # 如果多次替换，可能会搜索不到关键字，导致替换失败，所以每次替换前，先恢复备份。
    os.system('cp /etc/apt/sources.list.izmj.bak /etc/apt/sources.list')

# 选择源。
source_table = [
    ["阿里源", "https://mirrors.aliyun.com"],
    ["清华源", "https://mirrors.tuna.tsinghua.edu.cn"],
    ["中科大源", "https://mirrors.ustc.edu.cn"],
    ["华为源", "https://mirrors.huaweicloud.com"],
    ["浙大源", "https://mirrors.zju.edu.cn"],
    ["搜狐源", "https://mirrors.sohu.com"],
    ["网易源", "https://mirrors.163.com"]
]

print('\n======== Ubuntu的apt镜像源一览：======== ')
for i in range(len(source_table)):
    print('  ' + str(i + 1) + '. ' + source_table[i][0] + ' (' + source_table[i][1] + ')')
print('  ' + str(len(source_table) + 1) + '. ' + '自定义')
source_choice = input('请选择源：')

source_url = ''
if source_choice == str(len(source_table) + 1):
    source_url = input('请输入源的URL：')
    if source_url == '':
        print('\033[91m[ERROR] 自定义源的URL不能为空！\033[0m')
        exit(0)
    else:
        print('>>> 已选择源：' + source_url)
else:
    if source_choice == '':
        print('\033[91m[ERROR] 选择的源不存在！\033[0m')
        exit(0)
    source_choice_int = int(source_choice)
    if (source_choice_int > 0 and source_choice_int <= len(source_table)):
        source_url = source_table[source_choice_int - 1][1]
        print('>>> 已选择源：' + source_table[source_choice_int - 1][0] + ' (' + source_table[source_choice_int - 1][1] + ')')
    else:
        print('\033[91m[ERROR] 选择的源不存在！\033[0m')
        exit(0)

# 替换源
confirm = input('是否确认替换源？(y/n)')
if confirm == 'y':
    print('>>> 替换中...')
    os.system('sed -i "s#http.*.ubuntu.com#'+ source_url +'#g" /etc/apt/sources.list')
    print('>>> 替换完成！')
else:
    print('>>> 已取消替换！')
    exit(0)

# 更新源
confirm = input('是否更新软件信息？(y/n)')
if confirm == 'y':
    print('>>> 更新中...')
    os.system('apt update')
    print('>>> 更新完成！')
else:
    print('>>> 已取消更新！')
    exit(0)

# 更新软件
confirm = input('是否升级软件？(y/n)')
if confirm == 'y':
    print('>>> 升级中...')
    os.system('apt upgrade')
    print('>>> 升级完成！')
else:
    print('>>> 已取消升级！')
    exit(0)

print('======== 感谢使用izmj/itoys替换apt源脚本 ========')