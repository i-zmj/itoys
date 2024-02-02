
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform
import os

source_content = '''[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
'''

print('======== 欢迎使用izmj/itoys替换pip源脚本 ========')

pip_ini = ''
user_dir = os.path.expanduser("~")
if platform.system() == "Windows":
    pip_ini = os.path.join(user_dir, 'pip/pip.ini')
elif platform.system() == "Linux":
    pip_ini = os.path.join(user_dir, '.pip/pip.conf')

pip_ini = os.path.abspath(pip_ini)
if os.path.exists(pip_ini):
    print(f'{pip_ini} pip的配置文件已经存在！为了保证安全，请手动添加下列内容:\n')
    print(source_content)
else:
    print(f'创建pip配置文件{pip_ini}...')
    os.system(f'mkdir -p {os.path.dirname(pip_ini)}/')
    with open(pip_ini, 'w') as f:
        f.write(source_content)
    print('>> 已成功替换源！请重新运行pip命令安装！')

print('======== 感谢使用izmj/itoys替换pip源脚本 ========')
