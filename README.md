首先感谢MrSupW的下载器源码
东西算是已经完成了，感觉用aria2就行，这个下载器可以下载磁力也可以下载http/https
想自己做的下载器没有那个好用，只能进行http/https下载，页面也不太好看
所以建议使用aria2就好

#### 背景
就是看不惯迅雷限速,想做一个开源下载器，谁都能用


#### 用法

##### aria2
[从头开始布置aria2,也不麻烦](https://zhuanlan.zhihu.com/p/262699345)  

从代码中下载AriaNg-1.3.7-AllInOne和aria2/aria2这两个文件夹
由于已经都设置好了，先启动aria2/aria2中的HideRun.vbs(这是隐藏cmd窗口运行aria2)，然后启动AriaNg-1.3.7-AllInOne中的index.html，会打开浏览器，界面会显示已连接
![image](https://github.com/keyfall/High-speed-Downloader/assets/21198605/cad6b032-7cc6-4c33-9fff-be3c56dda28b)

新建输入要下载的http地址或者magnet的磁力地址就可以

##### 下载器
支持http/https，多线程
python环境，3.7以上都可以，我用的3.9
安装python3.9教程网上一堆，然后配置pip国内源，就好了
第三方库下载`pip install -r requirements.txt`
启动命令`python app.py`
![image](https://github.com/keyfall/High-speed-Downloader/assets/21198605/20f6a5d0-60a2-4cba-b67b-c009429db619)

