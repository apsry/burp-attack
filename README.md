# burp爆破框架

想着burp的一键生成python代码很好用，于是就写了一个简单的登陆爆破脚本

由于是自己用，所有写的很随便



在这里主要讲讲一些应用场景

## 1:关于burp的python插件

直接在extender里面下载即可
![Snipaste_202](https://user-images.githubusercontent.com/55017061/144565771-dff3cce8-5647-4d6f-960b-f0c39747e491.png)



会生成这类的代码

![Snipaste_2021-10-26_21-31-34](https://adsry.oss-cn-beijing.aliyuncs.com/img/Snipaste_2021-10-26_21-31-34.png)





其实和我们平常写的脚本没什么两样，但是有了这个插件会节省我们很多时间。举例一些应用场景

## 2：一些应用场景

比如默认密码爆破，大部分密码爆破都没有做太复杂的校验，所以我们爆破密码就可以直接抓包，然后放到把代码复制过去，调用fofa的api查找同类系统的ip地址。然后导入直接爆破默认密码即可。



比如未授权的简单的文件上传，直接抓包，写入框架，同理。要授权的文件上传也是直接改下代码加入session即可。



比如打CTF的时候批量交flag，批量打目标。



效果如图

![Snipaste_2021-10-26_21-39-35](https://adsry.oss-cn-beijing.aliyuncs.com/img/Snipaste_2021-10-26_21-39-35.png)
