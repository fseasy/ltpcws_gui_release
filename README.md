#！！ ABANDON

##已被废弃

**请使用基于QT(C++)开发的版本: [LTPCWS_UI using QT](https://github.com/memeda/ltpcws_qt)**

LTPCWS_GUI
====
0.update
---
windows平台统一编译为x86版本，兼容64位，可运行在Windows xp及以上系统(若不能运行，请先安装vcredist_x86.exe以包含运行时环境)
1.关于本程序
---
本程序是基于LTPCWS中otcws , otcws-customized程序的GUI外壳，主要用于DEMO演示。<br/>
程序采用python + tkinter 开发，使用pyinstaller完成在windows_X86、windows_X64 ，Linux(Ubuntu)_amd64平台上二进制程序转换。由于编译平台限制及其他原因，基于MAC OSX以及其他平台的二进制转换版本未能完成。希望在后续补充。<br/>
本程序已在windows_x64 , Ubuntu_amd64完成测试，但仍然可能存在不可预知的BUG。希望在后续不断完善。
本程序的稳定性不代表LTPCWS的稳定性。<br/>
    
2.使用方法
---
windows 64 位 ： 直接下载ltpcws-gui-win_x64.zip文件，解压后运行ltpcws-gui.exe即可<br/>
windows 32 位 :  直接下载ltpcws-gui-win_x86.zip文件，解压后运行ltpcws-gui.exe即可<br/>
Linux(Ubuntu) 64 : 直接下载ltpcws-gui-linux_amd64.tar.gz文件，解压后运行ltpcws-gui或在控制台输入 path/to/ltpcws-gui 即可<br/>
All : 下载source文件夹下文件，安装python 2.7.x(开发基于2.7.8)运行环境<br/> [Python2.7.8](https://www.python.org/download/releases/2.7.8/) , 在控制台输入python path/to/ltpcws-gui.py即可<br/>
     
