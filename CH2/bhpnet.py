import sys
import socket
import getopt
import threading
import subprocess

#gloabal var
listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0




def usage():
    print "BHP Net Tool"
    print
    print "用法: bhpnet.py -t target_host -p port"
    print "-l --listen               -在[host]:[port]監聽連入連線"
    print "-e --execute=file_to_run  -接到連線時執行指定檔案"
    print "-c --command              -啟動命令列shell "
    print "-u --upload=destination   -接到連線時上傳檔案並寫出[destination]"
