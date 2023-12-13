# i-toys

#### 介绍

i-toys是个人使用的脚本集合。将一些常用的操作整合成脚本，一键执行。

#### 使用说明

- replace_apt_source.py
  - 替换ubuntu的apt源，便于加速ubuntu的安装和升级。
  - `/etc/apt/sources.list`将备份到`/etc/apt/sources.list.izmj.bak`。如果备份已经存在，则不重复备份。
  - 需要sudo权限。
  - 脚本原理是搜索http.*.ubuntu.com，替换为指定源https://mirrors.izmj.net。
  - 自定义原地址时，请确保路径与预置的源格式一致。
1.  xxxx
2.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request
