# 学习笔记

## **Anaconda的安装集成jupyter notebook**

### 环境搭建
[黄博的环境搭建教程](https://zhuanlan.zhihu.com/p/59027692)  **下载的时候要注意Python的版本**

**安装完成可能会遇到```conda```命令不起作用的情况可以按照如下方法解决：**
> conda Mac 安装 conda命令行不起作用的解决办法。

>问题：在终端输入conda 无法识别这个命令。

>检查环境变量：```sudo vi ~/.bash_profile```

>如果环境变量中没有conda那么要手动添加```export PATH="/Users/anaconda3/bin:$PATH"```（这里要填写自己的路径!!）。

>刷新环境变量：```source ~/.bash_profile```

### 代码规范
[黄博Code prettify插件教程](https://zhuanlan.zhihu.com/p/59763076)

**注意，在执行```jupyter contrib nbextension install --user```的时候如果报错首先要退出所有的jupyter的进程，然后以管理员权限运行此行命令。**

### 多版本Python兼容切换

> 目前尝试过下载Aconda3.*然后添加配置Python2.7的运行环境。
```shell
#Aconda指定Python2.7的环境安装 命名随意
conda create -n 'Your env name' python=2.7
```
```shell
sudo python -m ipykernel install -user
```
> 之后在localhost里面的jupyter notebook顶部就可以切换3.*和2.7的运行环境了。

### 处理jupyter notebook里面import找不到库的问题
>找不到哪个库，就切换到terminal用```pip install```所需要的库，然后重启服务。


## **jupyter notebook使用笔记**

**快捷键总览**
![](https://pic2.zhimg.com/80/v2-111934f9949bc31eb8864c6ed4c60c05_hd.jpg)

