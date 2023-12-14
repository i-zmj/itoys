#!/usr/bin/env python3

def entry_tool(name) :
    print(f'\n======== 欢迎使用 iToys >> {name} << 脚本 ========\n')

def echo_process(msg) :
    print(f'>>> {msg} ...')

def echo_fail(msg) :
    print(f'\033[91m>>> [FAIL] {msg}\033[0m')

def echo_success(msg) :
    print(f'\033[92m>>> [SUCCESS] {msg}\033[0m')

def echo_tip(msg) :
    print(f'\033[93m>>> [TIP] {msg}\033[0m')

def exit_tool_success(msg=''):
    if msg != "":
        echo_success(msg)
    print('\n======== 感谢使用 iToys 脚本 ========\n')
    exit(0)

def exit_tool(msg=''):
    if msg != "":
        echo_fail(msg)
    print('\n======== 感谢使用 iToys 脚本 ========\n')
    exit(0)

def choose(msg) :
    print("")
    return input(msg)
def check_python_version() :
    # 如果当前运行环境是python2，则退出。
    import sys
    if sys.version_info.major != 3:
        exit_tool('\033[91m[FAIL] 本脚本仅支持Python 3下运行！\033[0m')

def check_config_exists(file) :
    import os
    if not os.path.exists(file):
        exit_tool(f'\n\033[91m[FAIL] {file}未找到。请重命名{file}.sample，并设置正确内容。\033[0m')

def read_config(file) :
    check_config_exists(file)
    file_encoding = 'ascii'
    import chardet
    with open('settings.json', 'rb') as f:
        data = f.read()
        file_encoding = chardet.detect(data)['encoding']

    import json
    with open('settings.json', 'r', encoding=file_encoding) as f:
        config = json.load(f)
        if not config:
            exit_tool('settings.json文件格式错误。请重命名settings.json.sample，并设置正确内容。')
        return config
    
def adb_shell(cmd,sudo=False) :
    import subprocess
    shell_cmd = ''
    if sudo:
        shell_cmd = f"adb shell su -c '{cmd}'"
    else:
        shell_cmd = f"adb shell '{cmd}'"
    echo_process("执行：" + shell_cmd)
    return subprocess.run(shell_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)