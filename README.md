# orangepi_cmds

升级pip3 后，如出现如下错误：

```
ImportError: cannot import name 'main'
```

则手动修改pip3:

```
nano /usr/bin/pip3
```

更改为：

```
from pip import __main__

if __name__ == '__main__':
    sys.exit(__main__._main())
```

之后，安装flask即可。

```
pip3 install flask
```

为了支持orangepi的GPIO，需要安装一些必要的基础库。

```
sudo apt-get install python-dev
```

```
git clone https://github.com/duxingkei33/orangepi_PC_gpio_pyH3
cd orangepi_PC_gpio_pyH3
python setup.py install
```


### 开机自动启动

```
nano /etc/rc.local
```

```
su - root -c "sh ~/orangepi_cmds/start.sh &"
```
