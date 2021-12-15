---
title: 使用终端运行第三方包教程
date: 2019-04-20 10:15:26
---

这个教程是关于怎么用终端运行和安装第三方包，比如说you-get

## Win版操作 

### 1 如果你只安装了原版Python

打开终端的方法就是，先按win+R，然后出现运行界面，再输入cmd，回车就可以看到终端了。

这个时候，终端显示的是初始的电脑中的地址，直接在里面输入pip install you-get

（如果你要安装别的包，就把you-get换成你要安装的包的名字）

如果要卸载，那就在里面输入pip uninstall you-get

另外一种打开终端的方法就是，再任意的文件夹的地址栏，删掉地址，输入cmd，就可以打开位于当前文件夹的终端。

运行you-get的时候，就是在终端输入you-get 加上视频的网络地址，you-get和视频的网络地址中间要有空格。视频会被下载到终端里面显示的那个文件夹里去。

### 2 如果你只安装了Anaconda

可以用Anaconda prompt打开针对Anaconda的终端。

在里面输入pip install you-get 就可行了 （如果你要安装别的包，就把you-get换成你要安装的包的名字）

如果要卸载，那就在里面输入pip uninstall you-get

运行you-get的时候，就是在终端输入you-get 加上视频的网络地址，you-get和视频的网络地址中间要有空格。视频会被下载到终端里面显示的那个文件夹里去。

### 3 如果你同时安装了原版Python和Anaconda

请修改Anaconda的安装文件，比如我安装在E盘，那就修改E:\Anaconda\Scripts里面的pip.exe和pip-script.exe改成condapip.exe和condapip-script.exe，这样在给Anaconda安装第三方包的时候就要输入

condapip install you-get

对于原版Python，就还是输入pip install you-get

这样可以避免冲突，安装的第三包就分开到两个程序里去了。

## Mac版操作

针对Mac，我只安装了Anaconda，打开终端也有两种方式，第一种方式请参考元胞自动机的教程。

第二种方式，请在你的Launchpad里打开“其他”，里面有终端Terminal可以直接打开。

安装第三方包也是输入pip install you-get