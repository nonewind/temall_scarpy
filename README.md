 # 天猫单一价格监控，通过微信发消息 
 - 微信消息推送 此功能通过方糖实现 详情见 方糖：http://sc.ftqq.com/3.version
 - 由于爬取天猫这个东西需要用到cookie,需要替换自己的cookie   方糖的key也需要换成自己的key
 - 为什么不用selenium？ 因为我的服务器太小了，我怕内存炸了就没有用 【腾讯云学生服务器 1X2G 】
  
 ## 已经实现的功能
 - 爬取天猫页面上的价格并进行提醒  利用re匹配出想要的json，解析成字典，因为商品的不同性质，就使用了几个json地址 对于女朋友来说足够
 - 价格比对：爬取出价格与上一次的价格进行对比，进行提醒


## 需要改进的地方
 - 只是爬取了价格，json文件中的很多东西还没有进行处理
 - 监控一个网址【一个商品】 后期会加上监控多个商品和网址 

## url 编辑规则
 -  https://detail.m.tmall.com/item.htm?id= + 【这里是所需要爬取商品的ID，具体就不多描述】+ &toSite=main
 - 提交了一个示例的logs文件夹以及其中的日志爬取文件
 - 按照上面的规则就可以编辑出一条重定向在30以内的url，满足request库的要求，同样用手机的头去访问 get it！
