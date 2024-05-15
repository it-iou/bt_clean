# 宝塔面板一键优化补丁

#### 介绍

**自用的宝塔面板一键优化补丁，主要有以下优化项目：**

1. 去除宝塔面板强制绑定账号
2. 去除各种删除操作时的计算题与延时等待
3. ~~去除创建网站自动创建的垃圾文件（index.html、404.html、.htaccess）~~
4. 关闭未绑定域名提示页面，防止有人访问未绑定域名直接看出来是用的宝塔面板
5. 关闭活动推荐与在线客服
6. 去除自动校验文件与上报信息定时任务
7. 去除面板日志与网站绑定域名上报

#### 使用说明

**适用于宝塔 Linux 面板 7.7 版本的命令 ：**

> 国外GitHub源：

>>```
>>wget -O optimize.sh https://raw.githubusercontent.com/it-iou/bt_clean/master/optimize.sh && bash optimize.sh
>>```

> 国内Gitee源：

>>```
>>wget -O optimize.sh https://gitee.com/itiou/bt_clean/raw/master/optimize.sh && bash optimize.sh
>>```

**一键升（降）级到宝塔7.7版本命令：**

> 国外GitHub源：

>>```
>>curl https://raw.githubusercontent.com/it-iou/bt_clean/master/update6.sh|bash
>>```

> 国内Gitee源：

> > ```
>>curl https://gitee.com/itiou/bt_clean/raw/master/update6.sh|bash
> > ```

**适用于宝塔 Linux 面板 >=7.9 版本的命令：**

> 国外GitHub源：

>>```
>>wget -O optimize.sh https://raw.githubusercontent.com/it-iou/bt_clean/master/optimize_new.sh && bash optimize.sh
>>```

> 国内Gitee源：

>>```
>>wget -O optimize.sh https://gitee.com/itiou/bt_clean/raw/master/optimize_new.sh && bash optimize.sh
>>```
**适用于宝塔国际版 aaPanel 的命令：**

> 国外GitHub源：

>>```
>>wget -O optimize.sh https://raw.githubusercontent.com/it-iou/bt_clean/master/optimize_aapanel.sh && bash optimize.sh
>>```

> 国内Gitee源：

>>```
>>wget -O optimize.sh https://gitee.com/itiou/bt_clean/raw/master/optimize_aapanel.sh && bash optimize.sh
>>```
**适用于宝塔 Windows 面板的命令：**

> 国外GitHub源：

>>```
>>wget -O optimize.sh https://raw.githubusercontent.com/it-iou/bt_clean/master/optimize.py -O C:/optimize.py && "C:\Program Files\python\python.exe" C:/optimize.py
>>```

> 国内Gitee源：

>>```
>>wget https://gitee.com/itiou/bt_clean/raw/master/optimize.py -O C:/optimize.py && "C:\Program Files\python\python.exe" C:/optimize.py
>>```

## 致谢

这里仅做一备份修改自用，感谢原作者：

- https://github.com/chenjinnian/bt_clean
- https://github.com/DsTansice/bt_clean
- http://www.cccyun.cc/
