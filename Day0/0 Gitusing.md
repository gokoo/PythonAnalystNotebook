# Day1

## 任务目标 ：学习使用Git上传文件至GitHub，Jupyter Notebook基础环境搭建

### **笔记**
1. Git 在shell下切换username和email的指令
    
    ```shell
    git config --global user.name "username"

    git config --global user.email "example@com"
    ```
2. sshKeygen生成公钥添加权限

    生成自己的公钥，按选择点击回车，生成的id_rsa和id_rsa.pub在 ” ~/.ssh“ 文件目录下(OSX系统下，Win在用户主目录里找 到.ssh目录)

    ```shell
    ssh-keygen -t rsa -C "youremail@example.com"
    ```
***
### 参考资料

[视频版 Bilibili](https://www.bilibili.com/video/av10475153?from=search&seid=11281184335048850372)

[网页版GitBook](https://git-scm.com/book/zh/v2)

[网页版廖雪峰](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)

文档版

[Git.pdf](https://github.com/gokoo/PythonAnalystNotebook/blob/master/Day0/git.pdf)  **Win7环境**

[两小时学会Git玩转GitHub.pdf](https://github.com/gokoo/PythonAnalystNotebook/blob/master/Day0/两小时学会Git玩转GitHub.pdf) **Windows环境。但是讲了原理的知识**

