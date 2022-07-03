from datetime import datetime
import requests
import json
import sys
import configparser
import ctypes
import socket
import time

############################## init ##############################
inipath = "./pc_timer.ini"
ini = configparser.ConfigParser()
ini.read(inipath, 'UTF-8')

#[SETTINGS]
webhook_url = ini['SETTINGS']['webhook_url']

##################################################################

def send_msg(text):
    main_content = {'content': text}
    headers      = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json.dumps(main_content), headers=headers)

def main(args):

    host_name = socket.gethostname()
    datetime_now = datetime.now()
    msg = str(datetime_now.strftime('%Y年%m月%d日 %H:%M:%S\n'))

    if args[1] == "START":
        msg += host_name + "をスリープから復帰させました。"
        send_msg(msg)


    elif args[1] == "STOP":
        msg += host_name + "をスリープさせます。"
        send_msg(msg)
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)

    else:
        sys.exit(1)

    sys.exit(0)

if __name__ == '__main__':
    sys.exit(main(sys.argv))