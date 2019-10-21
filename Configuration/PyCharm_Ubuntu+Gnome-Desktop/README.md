# 官网打包的 PyCharm 程序在 Ubuntu (gnome) 桌面上安装（注册）为应用程序

## Download & Install

```shell
$ ## download pycharm
$ sudo tar -xzvf pycharm-community-2019.1.3.tar.gz -C /opt/
$ cd /opt/pycharm-community-2019.1.3/bin
$ ./pycharm.sh  # 测试运行
```



## as Application

```shell
$ cd /usr/share/applications/
$ sudo vim PyCharm.desktop
[Desktop Entry]
Name=PyCharm
GenericName=Editor
Comment=PyCharm - A Python IDE
Exec="/opt/pycharm-community-2019.1.3/bin/pycharm.sh" %U
Icon=/opt/pycharm-community-2019.1.3/bin/pycharm.png
Terminal=false
Categories=TextEditor;Development;
StartupNotify=false
Type=Application
~
~
:wq
$ sudo reboot  # 或者注销桌面，重新登录进入桌面
```

