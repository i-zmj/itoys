#!/usr/bin/env python3

import os,sys
# 添加当前目录的上级目录../common到sys.path中，以便导入itoys_common
sys.path.append(os.path.join(os.getcwd(), ".."))

import common.itoys_common as itoys

itoys.check_python_version()
itoys.entry_tool('同步Android目录')

# 读取settings.json文件
config = itoys.read_config('settings.json')
    
device_id = ''
# 读取android/sync_source_dirs数组
sync_source_dirs = config['android']['sync_source_dirs']

# 读取pc、sync_target_dir数组
sync_target_dir = config['pc']['sync_target_dir']

device_id = config['android']['device_id']

itoys.echo_tip('根据配置文件，检测到以下Android目录需要同步：')
for source_dir in sync_source_dirs:
    itoys.echo_tip('  ' + source_dir)
itoys.echo_tip('同步目标目录：' + sync_target_dir)

if device_id != '':
    itoys.echo_process('指定设备ID：' + device_id)

itoys.echo_process('检测adb环境是否可用')

# 检查adb是否可用
if os.system('adb version') != 0:
    itoys.exit_tool('adb命令不可用，请检查adb设置。')

itoys.echo_success('adb环境正常')

if '-y' in sys.argv:
    itoys.echo_process('检测到-y参数，跳过同步确认，直接执行。')
else:
    itoys.echo_tip('添加-y参数，可跳过确认。')
    choice = input("是否执行同步？(y/n) ")
    if choice != 'y':
        itoys.exit_tool_success('取消同步！')

itoys.echo_process('获取Android目录读写权限')

for source_dir in sync_source_dirs:
    result = itoys.adb_shell(f"chmod 777 {source_dir} -R", True);
    if result.returncode != 0:
        itoys.echo_fail(f"执行 chmod 777 {source_dir} -R 失败。错误提示：{result.stderr}")

# 检查pc目录是否存在
if not os.path.exists(sync_target_dir):
    choice = input("目标目录不存在，是否创建？(y/n)")
    if choice != 'y':
        itoys.echo_success('取消同步！')
        itoys.exit_tool()
    else:
        os.makedirs(sync_target_dir)
else:
    if '-d' in sys.argv:
        itoys.echo_process('检测到-d参数，跳过PC目录清空确认，直接执行。')
        if (os.path.exists(sync_target_dir)):
            import shutil
            shutil.rmtree(sync_target_dir)
            os.makedirs(sync_target_dir)
    elif '-D' in sys.argv:
        itoys.echo_process('检测到-D参数，跳过PC目录清空确认，不执行。')
    else:
        itoys.echo_tip('添加-d参数，可跳过PC目录清空确认。添加-D参数，则不清空PC目录。')
        choice = itoys.choose('请确认是否清空PC目录？(y/n) ')
        if  choice == 'y':
            if (os.path.exists(sync_target_dir)):
                import shutil
                shutil.rmtree(sync_target_dir)
                os.makedirs(sync_target_dir)
        else:
            itoys.echo_success('取消清空PC目录！')

# 执行adb pull
itoys.echo_process('开始同步')
for source_dir in sync_source_dirs:
    if device_id != '':
        os.system('adb -s ' + device_id + 'pull ' + source_dir + ' ' + sync_target_dir)
    else:
        os.system('adb pull ' + source_dir + ' ' + sync_target_dir)

# 执行完毕
itoys.echo_success('同步完毕！')

# 是否需要打开目标目录

if '-o' in sys.argv:
    itoys.echo_success('检测到-o参数，跳过目录打开确认，直接打开。')
elif '-O' in sys.argv:
    itoys.echo_success('检测到-O参数，跳过目录打开确认，不打开。')
    print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
    exit(0)
else:
    itoys.echo_tip('添加-o参数，则直接打开目录。添加-O参数，则不打开目录。')
    choice = input('是否打开目标目录？(y/n)')
    if choice != 'y':
        itoys.echo_success('不打开目标目录！')
        print('======== 感谢使用izmj/itoys同步Android目录脚本 ========')
        exit(0)

import platform
if  platform.system() == 'Windows':
    os.system('explorer.exe /root,' + sync_target_dir)
else:
    os.system('open'+ sync_target_dir)

itoys.echo_success('打开完毕！')
itoys.exit_tool()