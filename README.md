websocket-client-max31856-9801.service  
=======================================  
is UNIT made by setting 
  
websocket-client-max31856-9801.sh  
=================================  
Start to work when 192.168.3.8:9801 can ping back.  
Is called from service  
  
setting.sh  
==========  
Prepares to serve service  
  concrete:  
    Make websocket-client-max31856-9801.service on its directoryi.  
    Put symbolic link of websocket-client-max31856-9801.service within "/etc/systemd/system/".  
    Change its mode to 640  

websocket/  
==========  
This is module from github  
  
max31856.py  
==========  
This is module copied by renewmax.sh
  
renewmax.sh  
===========  
If you need a new version of max31856.py, you should type "./renewmax.sh".  
  
  
  
How to use  
==========  
  Start Service  
  =============  
  There are 2 way to start measuring temperature.  
    sudo reboot  
     or  
    systemctl start websocket-client-max31856-9801  
    
  Make Service  
  ============  
  Type next 2 lines.  
    ./setting.sh  
    sudo reboot  

LICENSE  
=======  
There is third party's LICENSE in "websocket/".  
Others are under MIT license.  
  
説明  
====  
Raspberry Pi 3B+ と Max31856モジュールを利用します。  
ウェブソケットサーバーの9801番ポート(default)に接続して  
一秒ごとに温度を送ります。  
書式はサーバーにあわせてあります。  
toCを頭に付けた後、温度文字列を送っています。  




