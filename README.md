# iToys工具集

#### 介绍

itoys是个人使用的脚本集合。将一些常用的操作整合成脚本，一键执行。

国内维护地址：https://gitee.com/izmj/itoys.git  
国外维护地址：https://github.com/i-zmj/itoys.git

有需求，问题，可新建issue。视心情开发。

本工具不可用于违法，损害他人权益，侵犯隐私，损害国家利益，违反公序良俗等场景。

#### 使用说明

- android
  - sync_dir.py
    - 将手机目录同步到PC目录。
    - 适用于进行开发时，将日志、堆栈等文件同步到手机。
  - clear_dir.py
    - 清空指定手机目录。
    - 适用于删除旧日志、缓存等文件。

- linux
  - replace_apt_source.py
    - 替换ubuntu的apt源，便于加速ubuntu的安装和升级。
    - `/etc/apt/sources.list`将备份到`/etc/apt/sources.list.izmj.bak`。如果备份已经存在，则不重复备份。
    - 需要sudo权限。
    - 脚本原理是搜索http.*.ubuntu.com，替换为国内源（可选，可自定义）。
    - 自定义原地址时，请确保路径与预置的源格式一致。

- git
  - setup.py

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
