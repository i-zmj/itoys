#!/usr/bin/env python3

import os,sys

# 添加当前目录的上级目录../common到sys.path中，以便导入itoys_common
sys.path.append(os.path.join(os.getcwd(), ".."))

import common.itoys_common as itoys

itoys.check_python_version()

itoys.entry_tool('删除Android目录')

config = itoys.read_config('settings.json')

clear_dirs = []
try:
    clear_dirs = config["android"]["clear_dirs"]
    itoys.echo_tip('根据配置文件，检测到以下Android目录需要清理：')
    for dir in clear_dirs:
        itoys.echo_tip('  ' + dir)
except:
    itoys.exit_tool("settings.json文件中没有找到clear_dirs配置项。")

if '-y' in sys.argv:
    itoys.echo_process('检测到-y参数，跳过清理确认，直接执行。')
else:
    itoys.echo_tip('添加-y参数，可跳过清理确认。')
    choice = itoys.choose('请确认是否清理以上目录？(y/n) ')
    if  choice != 'y':
        itoys.exit_tool_success('取消清理！')

for dir in clear_dirs :
    itoys.adb_shell(f"rm {dir} -rf", True)
    # TODO: 此处需要考虑如何更优雅的获得adb shell命令的返回值

    import subprocess
    check_result_cmd = f"adb shell ls {dir}"
    itoys.echo_process("通过ls命令判断执行结果：" +check_result_cmd)
    result = itoys.adb_shell("ls " + dir, True)
    if "No such file or directory" in result.stderr:
        itoys.echo_success(f"清理{dir}成功")
    else:
        itoys.echo_fail(f"清理{dir}失败。错误提示：{result.stderr}")
    itoys.echo_tip("====================================")