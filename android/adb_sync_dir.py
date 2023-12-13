#!/usr/bin/env python3

# 如果当前运行环境是python2，则退出。
import sys
if sys.version_info.major != 3:
    print('\033[91m[ERROR] This script is for python3 only.\033[0m')
    exit(0)

print("======== 欢迎使用izmj/itoys同步Android目录脚本 ========")

# 如果当前目录下没有adb_sync_dir.json文件，则创建ini，并退出。
import os
if not os.path.exists('adb_sync_dir.json'):
    print('\033[91m[ERROR] adb_sync_dir.json未找到。请重命名adb_sync_dir.json.sample，并设置正确内容。\033[0m')
    exit(0)

# 读取adb_sync_dir.json文件
import json

device_id = ''

# 检测文件格式
file_encoding = 'ascii'
import chardet
with open('adb_sync_dir.json', 'rb') as f:
    data = f.read()
    file_encoding = chardet.detect(data)['encoding']

with open('adb_sync_dir.json', 'r', encoding=file_encoding) as f:
    config = json.load(f)
    if not config:
        print('\033[91m[ERROR] adb_sync_dir.json文件格式错误。请重命名adb_sync_dir.json.sample，并设置正确内容。\033[0m')
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)
    
    # 读取android/sync_source_dirs数组
    sync_source_dirs = config['android']['sync_source_dirs']

    # 读取pc、sync_target_dir数组
    sync_target_dir = config['pc']['sync_target_dir']

    device_id = config['android']['device_id']

print('>>> 根据配置文件，检测到以下Android目录需要同步：\n')
for source_dir in sync_source_dirs:
    print('  ' + source_dir)
print('\n>>> 同步目标目录：' + sync_target_dir)

if device_id != '':
    print('\n>>> 指定设备ID：' + device_id)

print('\n>>> 检测adb环境是否可用')

# 检查adb是否可用
if os.system('adb version') != 0:
    print('\033[91m[ERROR] adb命令不可用，请检查adb设置。\033[0m')
    print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
    exit(0)

print('\n>>> adb环境正常')

if '-y' in sys.argv:
    print('\n>>> 检测到-y参数，跳过同步确认，直接执行。')
    auto_sync = True
else:
    choice = input("\n添加-y参数，可跳过确认。\n是否执行同步？(y/n) ")
    if choice != 'y':
        print('>>> 取消同步！')
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)

print('\n>>> 获取Android目录读写权限')

for source_dir in sync_source_dirs:
    if os.system(f"adb shell su -c 'chmod 777 {source_dir} -R'") != 0:
        print(f"\033[91m[ERROR] adb shell su -c 'chmod 777 {source_dir} -R' 失败。\033[0m")
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)

# 检查pc目录是否存在
if not os.path.exists(sync_target_dir):
    choice = input("目标目录不存在，是否创建？(y/n)")
    if choice != 'y':
        print('>>> 取消同步！')
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)
    else:
        os.makedirs(sync_target_dir)

# 执行adb pull
print('\n>>> 开始同步...')
for source_dir in sync_source_dirs:
    if device_id != '':
        os.system('adb -s ' + device_id + 'pull ' + source_dir + ' ' + sync_target_dir)
    else:
        os.system('adb pull ' + source_dir + ' ' + sync_target_dir)

# 执行完毕
print('\n>>> 同步完毕！')

# 是否需要打开目标目录

if '-o' in sys.argv:
    print('\n>>> 检测到-o参数，跳过目录打开确认，直接打开。')
elif '-O' in sys.argv:
    print('\n>>> 检测到-O参数，跳过目录打开确认，不打开。')
    print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
    exit(0)
else:
    print('\n添加-o参数，则直接打开目录。添加-O参数，则不打开目录。')
    choice = input('是否打开目标目录？(y/n)')
    if choice != 'y':
        print('\n>>> 不打开目标目录！')
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)

import platform
if  platform.system() == 'Windows':
    os.system('explorer.exe /root,' + sync_target_dir)
else:
    os.system('open'+ sync_target_dir)

print('\n>>> 打开完毕！')
print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')