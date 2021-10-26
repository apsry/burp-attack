import requests
import sys

session = requests.session()
path=sys.path[0]
print(path)
def attack():
    for line in open(path+ "\\url.txt", encoding='utf-8'):
        #print(line)
        burp0_url = 'http://' + str(line).replace('\n','') + ''
        print(burp0_url)
        burp0_cookies = {}
        burp0_headers = {}
        try:
            response=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        except:
            pass
        f=open(path+ '\\result.txt','a', encoding='utf-8')
        print(burp0_url+'\n')
        print(response.text)
        f.write(burp0_url+'\n')
        f.write(response.text)
        f.write('\n\n')
        f.close()
   
if __name__ == '__main__':
    attack()


