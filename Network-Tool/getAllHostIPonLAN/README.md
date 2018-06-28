# Developer Document

  reserve place

*Overview*

[TOC]

## Contents

  N/A

## v0.0.1 basic uage

work path tree:

```none
/
|-- getAllHostIPonLAN/
|          |-- Example/
|          |     `-- main.py
|          |-- getAllHostIPonLAN.py
|          |-- setup.py
|          |
|          |-- libraries/
|          |       |-- Makefile
|          |        `- nmap-<version>.tar.bz2
|           `- README.md
 `- README.md
```

### getAllHostIPonLAN/

  安装该库：

```shell
$ python3 setup.py sdist
$ sudo python3 setup.py install
```

### libraries -> nmap

  从 nmap source code 编译出 nmap 不需要 什么特别的依赖， 全新的 Ubuntu LTS 16.04 系统可以编译通过

（在 libraries 目录下运行 `$ make`）

### Install 完整命令
```shell
<path>/ $ git clone https://github.com/AceLin2016/LINUX.git
<path>/ $ cd LINUX/Network-Tool/getAllHostIPonLAN/
<path>/LINUX/Network-Tool/getAllHostIPonLAN/ $ cd libraries
<path>/LINUX/Network-Tool/getAllHostIPonLAN/libraries/ $ make
...running compiler...
<path>/LINUX/Network-Tool/getAllHostIPonLAN/libraries/ $ sudo cp ./bin/nmap /usr/local/bin/
<path>/LINUX/Network-Tool/getAllHostIPonLAN/libraries/ $ cd ../
<path>/LINUX/Network-Tool/getAllHostIPonLAN/ $ python3 setup.py sdist
<path>/LINUX/Network-Tool/getAllHostIPonLAN/ $ sudo python3 setup.py install
<path>/LINUX/Network-Tool/getAllHostIPonLAN/ $ ## Tester:
<path>/LINUX/Network-Tool/getAllHostIPonLAN/ $ ./Example/main.py 192.168.1.0/24 ON ## 这一行在下面 "usage" 解释 
```

### usage

  使用 getAllHostIPonLAN/ 下的 Example/main.py 测试
```shell
$ ./Example/main.py 192.168.1.0/24 ON
$ ## 程序名           网段           以标准输出结果？ON/OFF
$ ## OFF 的情况下， 在 /tmp/ 目录下， 
$ ## 分别有 proc_net_arp.txt & namp_-sP.txt 文件
```

## Note

  
