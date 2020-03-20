# 修复误删 /var/lib/dpkg/info/ 文件夹问题

错误消息：
```shell
$ sudo apt install <some-software>
...
dpkg: 警告: 无法找到软件包 <XXXXX>:amd64 的文件名列表文件，现假定该软件包目前没有任何文件被安装在系统里。
...
$
```

修复：
```shell
$ su root
password:
# ./recover_dpkg_info.sh
```

