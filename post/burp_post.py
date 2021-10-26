import requests
import sys


session = requests.session()
path=sys.path[0]
print(path)
def attack():
    for line in open(path+ "\\url.txt", encoding='utf-8'):
        host=str(line).replace('\n','')
        print(host)
        burp0_url = host + ""
        burp0_headers = {}
        burp0_json={}
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
