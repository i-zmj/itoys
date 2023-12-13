# itoys

#### 介绍

itoys是个人使用的脚本集合。将一些常用的操作整合成脚本，一键执行。

国内维护地址：https://gitee.com/izmj/itoys.git
国外维护地址：https://github.com/i-zmj/itoys.git

有需求，问题，可新建issue。视心情开发。

本工具不可用于违法，损害他人权益，侵犯隐私，损害国家利益，违反公序良俗等场景。

#### 使用说明

- Android
  - adb_sync_dir.py
    - 将手机目录同步到PC目录。
    - 需要adb环境。
    - 涉及adb shell su -c 命令，可能需要root权限。
    - 需要搭配adb_sync_dir.json文件进行使用。可以参考adb_sync_dir.json.sample

- Linux
  - replace_apt_source.py
    - 替换ubuntu的apt源，便于加速ubuntu的安装和升级。
    - `/etc/apt/sources.list`将备份到`/etc/apt/sources.list.izmj.bak`。如果备份已经存在，则不重复备份。
    - 需要sudo权限。
    - 脚本原理是搜索http.*.ubuntu.com，替换为国内源（可选，可自定义）。
    - 自定义原地址时，请确保路径与预置的源格式一致。


#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
