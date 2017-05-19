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
    print "Usage:bhpnet.py -t target_host -p port"
    print "-l --listen         "