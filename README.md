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
