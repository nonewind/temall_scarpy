 # 天猫单一价格监控，每天一次，通过微信发消息

 - 方糖：http://sc.ftqq.com/3.version
 - 由于爬取天猫这个东西需要用到cookie,需要替换自己的cookie
 - 方糖的key也需要换成自己的key
 - 为什么不用selenium？ 因为我的服务器太小了，我怕内存炸了就没有用
  
 ## 已经实现的功能
 - 爬取天猫页面上的价格并进行提醒
 - 识别不通过的商品请求的网页头 
 - 价格比对：爬取出价格与上一次的价格进行对比，进行提醒


## 未实现的功能
 - 目前天猫有个促销价格和优惠没有找到是哪个js文件，所以暂时先不写【搞一个单独的模块】

