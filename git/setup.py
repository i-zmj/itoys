#!/usr/bin/env python3

# 如果当前运行环境是python2，则退出。
import sys,os

if sys.version_info.major != 3:
    print('\033[91m[ERROR] This script is for python3 only.\033[0m')
    exit(0)

def exit_common(msg):
    print(msg)
    print('======== 感谢使用 izmj/itoys 更新设置工具 ========')
    exit(0)

print("======== 欢迎使用 izmj/itoys 更新设置工具 ========")

# 循环执行
while True:
    print("\n>>> 菜单：")
    print("   1. 更新Repo库基础信息(repo_info.json)仓库信息")
    print("   0. 退出")

    choice = input('\n请选择：')
    if choice == '0':
        break
    elif choice == '1':
        if os.path.exists('repo_info.json'):
            print('\n>>> 检测到repo_info.json文件')
        else:
            exit_common('\033[91m[ERROR] 没有检测到repo_info.json文件，请参考repo_info.json.sample创建repo_info.json文件。\033[0m')

        # 读取repo_info.json文件
        import json
        with open('repo_info.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
            if not config:
                exit_common('\033[91m[ERROR] repo_info.json文件格式错误。请参考repo_info.json.sample创建repo_info.json文件。\033[0m')
            
            # 读取repo_info.json文件中的repo_url
            update_url = config['update_url']
            print('\n>>> 读取到repo_url：' + update_url)
            if update_url:
                # 发起网络请求，下载到repo_info_update.json
                import requests
                try:
                    r = requests.get(update_url)

                    if r.status_code != 200:
                        exit_common('\033[91m[ERROR] update_url访问失败。无法进行更新！\033[0m')
                    else:
                        print('\n>>> update_url请求成功')
                        
                        config_new = json.loads(r.text)
                        if not config_new:
                            exit_common('\033[91m[ERROR] update_url返回数据格式错误。无法进行更新！\033[0m')
                except:
                    exit_common('\033[91m[ERROR] repo_url访问失败。无法进行更新！\033[0m')

                # 读取repo_info_update.json文件中的version
                if config['version'] != config_new['version']:
                    print('\n>>> 检测到repo_info_update.json文件版本号不一致:')
                    print('    当前版本: ' + config['version'])
                    print('    服务器版本: ' + config_new['version'])

                    choice = input('\n是否更新repo_info.json文件？(y/n)')
                    if choice == 'y':
                        # 更新repo_info.json文件
                        with open('repo_info.json', 'w', encoding='utf-8') as f:
                            f.write(r.text)
                            print('>>> repo_info.json文件已更新')
                    else:
                        print('>>> 已取消更新repo_info.json文件')
                else:
                    print('\n>>> 检测到repo_info_update.json文件版本号一致，无需更新')

print('\n======== 感谢使用 izmj/itoys 更新设置工具 ========')