# 官网打包的二进制 Typora 在 Ubuntu (gnome) 上安装为应用程序（可被选择为默认程序）



## Download & Install
```shell
$ cd Downloads/Software
$ wget https://typora.io/linux/Typora-linux-x64.tar.gz
$ tar -xzvf Typora-linux-x64.tar.gz
$
$ sudo mv Typora-linux-x64 /opt/
$ 
$ cd /opt/Typora-linux-x64/
$ ./Typora  # 运行 typora 看能否正常运行
```

## as Application
```shell
$ cd /usr/share/applications/
$ sudo vim Typora.desktop
[Desktop Entry]
Name=Typora
GenericName=Editor
Comment=Typroa - a markdown editor
Exec="/opt/Typora-linux-x64/Typora" %U
Icon=/opt/Typora-linux-x64/resources/app/asserts/icon/icon_256x256.png
Terminal=false
Categories=Markdown;
StartupNotify=false
Type=Application

:wq
$ 
$ sudo reboot
```

## Reference

[将应用程序添加到gnome3的全局菜单中（并支持修改为默认程序）](https://blog.csdn.net/ytingone/article/details/50349394)