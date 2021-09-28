import requests
import os 
import time


os.system('clear')
cookie=''
def main(): 
    while True: 
        cmd=input(">>>")
        if cmd == "tempdis":
            for x in range(20):
                response=requests.post("https://192.168.1.254/cgi-bin/crestart.ha?1", 
                headers={'Cookie' : f'SessionID={cookie}'}, 
                verify=False)
            print('')
            print('Done')
        elif cmd == "check": 
            res=os.system('ping youtube.com')
            print(res)
        elif cmd == "dis":
            while True:
                response=requests.post("https://192.168.1.254/cgi-bin/crestart.ha?1", 
                headers={'Cookie' : f'SessionID={cookie}'}, 
                verify=False)
                print('')
                print('Done')
        elif cmd == "rdis":
            while True: 
                for x in range(20):
                    time.sleep(30)
                    response=requests.post("https://192.168.1.254/cgi-bin/crestart.ha?1", 
                    headers={'Cookie' : f'SessionID={cookie}'}, 
                    verify=False)
                    print('')
                    print('Done')
    

